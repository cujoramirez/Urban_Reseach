"""Dukuh Atas accessible-facility map (accessibility-pivot deliverable).

Fetches OSM for a tight Dukuh Atas bbox and writes a styled GeoJSON with:
  - a facility layer: benches, shelters, toilets (+ accessible toilets), lifts/
    elevators, tactile paving, crossings, drinking water
  - a sidewalk INDICATION layer: blue = sidewalk, gray = footway/path/none

Simplestyle props (marker-color, stroke, stroke-width) make it render cleanly in
geojson.io, and the plain geometry + properties load straight into MapKit.

Network-dependent. Run from the repo root:
  .venv-spatial/bin/python -m investigate.spatial.facility_map
"""
from __future__ import annotations
import os, json
from collections import Counter
from . import fetch_osm

# Tight box around the Dukuh Atas interchange (MRT/KRL/LRT/TJ) — W, S, E, N.
DUKUH_ATAS_BBOX = (106.817, -6.208, 106.828, -6.197)
DATA = os.path.join(os.path.dirname(__file__), "data")

# facility kind -> (label, marker-color)
NODE_STYLE = {
    "elevator": ("Lift", "#6a1b9a"),
    "toilet_accessible": ("Accessible toilet", "#6a1b9a"),
    "toilet": ("Toilet", "#1565c0"),
    "bench": ("Bench", "#2e7d32"),
    "shelter": ("Shelter", "#2e7d32"),
    "water": ("Drinking water", "#00838f"),
    "tactile_paving": ("Tactile paving", "#ef6c00"),
    "crossing": ("Crossing", "#607d8b"),
}


def build_query(bbox=DUKUH_ATAS_BBOX) -> str:
    w, s, e, n = bbox
    b = f"{s},{w},{n},{e}"
    return (
        "[out:json][timeout:90];("
        f'way["highway"~"footway|pedestrian|path"]({b});'
        f'way["highway"]["sidewalk"]({b});'
        f'node["amenity"~"bench|shelter|toilets|drinking_water"]({b});'
        f'node["highway"="elevator"]({b});'
        f'node["railway"="elevator"]({b});'
        f'node["tactile_paving"="yes"]({b});'
        f'node["highway"="crossing"]({b});'
        ");out geom;"
    )


def _in_bbox(pt, bbox=DUKUH_ATAS_BBOX) -> bool:
    w, s, e, n = bbox
    return w <= pt[0] <= e and s <= pt[1] <= n


def _node_kind(t: dict):
    if t.get("highway") == "elevator" or t.get("railway") == "elevator":
        return "elevator"
    if t.get("amenity") == "toilets":
        acc = t.get("wheelchair") == "yes" or t.get("toilets:wheelchair") == "yes"
        return "toilet_accessible" if acc else "toilet"
    if t.get("amenity") == "bench":
        return "bench"
    if t.get("amenity") == "shelter":
        return "shelter"
    if t.get("amenity") == "drinking_water":
        return "water"
    if t.get("tactile_paving") == "yes":
        return "tactile_paving"
    if t.get("highway") == "crossing":
        return "crossing"
    return None


def node_features(osm: dict) -> list:
    feats = []
    for el in osm.get("elements", []):
        if el.get("type") != "node":
            continue
        pt = [el["lon"], el["lat"]]
        if not _in_bbox(pt):
            continue
        t = el.get("tags", {})
        kind = _node_kind(t)
        if not kind:
            continue
        label, color = NODE_STYLE[kind]
        feats.append({
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": pt},
            "properties": {
                "facility": kind, "label": label,
                "accessible": t.get("wheelchair", "unknown"),
                "name": t.get("name", ""),
                "marker-color": color, "marker-size": "small",
            },
        })
    return feats


def edge_features(osm: dict) -> list:
    feats = []
    for el in osm.get("elements", []):
        if el.get("type") != "way":
            continue
        coords = [[p["lon"], p["lat"]] for p in el.get("geometry", [])]
        if len(coords) < 2 or not any(_in_bbox(p) for p in coords):
            continue
        t = el.get("tags", {})
        has = t.get("footway") == "sidewalk" or t.get("sidewalk") in ("both", "left", "right", "yes")
        feats.append({
            "type": "Feature",
            "geometry": {"type": "LineString", "coordinates": coords},
            "properties": {
                "layer": "sidewalk" if has else "path",
                "has_sidewalk": "yes" if has else "unknown",
                "name": t.get("name", ""),
                "stroke": "#1565c0" if has else "#9e9e9e",   # blue vs gray
                "stroke-width": 3 if has else 1,
            },
        })
    return feats


def main() -> None:
    os.makedirs(DATA, exist_ok=True)
    osm = fetch_osm.fetch_overpass(build_query())
    edges, nodes = edge_features(osm), node_features(osm)
    out = os.path.join(DATA, "dukuh_atas_facilities.geojson")
    with open(out, "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection", "features": edges + nodes},
                  f, ensure_ascii=False, indent=1)
    sw = sum(1 for e in edges if e["properties"]["has_sidewalk"] == "yes")
    print(f"[ok] {len(edges)} edges ({sw} sidewalk) + {len(nodes)} facilities -> {out}")
    print("  facilities:", dict(Counter(n["properties"]["facility"] for n in nodes)))


if __name__ == "__main__":
    main()
