"""Fetch named candidate destinations around Dukuh Atas for the accessibility pilot audit.

Real OSM place names only (no invented data). Writes data/dukuh_atas_places.csv and
prints them grouped by type so the team can curate a ~10-15 place survey shortlist.

Run from repo root:
  .venv-spatial/bin/python -m investigate.spatial.place_shortlist
"""
from __future__ import annotations
import os, csv
from collections import Counter
from . import fetch_osm

BBOX = (106.817, -6.208, 106.828, -6.197)  # Dukuh Atas
DATA = os.path.join(os.path.dirname(__file__), "data")


def query(bbox=BBOX) -> str:
    w, s, e, n = bbox
    b = f"{s},{w},{n},{e}"
    return (
        "[out:json][timeout:90];("
        f'nwr["amenity"~"cafe|restaurant|fast_food|food_court|marketplace|place_of_worship|library|community_centre|cinema|bank"]["name"]({b});'
        f'nwr["shop"~"mall|department_store|supermarket|convenience"]["name"]({b});'
        f'nwr["leisure"~"park|fitness_centre"]["name"]({b});'
        f'nwr["tourism"~"hotel|museum"]["name"]({b});'
        f'nwr["public_transport"="station"]["name"]({b});'
        f'nwr["railway"="station"]["name"]({b});'
        ");out center tags;"
    )


def kind(t: dict) -> str:
    if t.get("railway") == "station" or t.get("public_transport") == "station":
        return "station"
    if t.get("shop") in ("mall", "department_store"):
        return "mall"
    if t.get("shop") == "supermarket":
        return "supermarket"
    if t.get("leisure") == "park":
        return "park"
    if t.get("leisure") == "fitness_centre":
        return "gym"
    if t.get("tourism") == "hotel":
        return "hotel"
    if t.get("tourism") == "museum":
        return "museum"
    if t.get("amenity") in ("cafe", "restaurant", "fast_food", "food_court"):
        return "food"
    if t.get("amenity") == "place_of_worship":
        return "worship"
    if t.get("amenity") == "cinema":
        return "cinema"
    if t.get("amenity") == "library":
        return "library"
    if t.get("amenity") == "marketplace":
        return "market"
    if t.get("amenity") == "community_centre":
        return "community"
    if t.get("amenity") == "bank":
        return "bank"
    return t.get("amenity") or t.get("shop") or t.get("leisure") or "place"


def main() -> None:
    osm = fetch_osm.fetch_overpass(query())
    rows = []
    for el in osm.get("elements", []):
        t = el.get("tags", {})
        name = t.get("name")
        if not name:
            continue
        if el["type"] == "node":
            lon, lat = el.get("lon"), el.get("lat")
        else:
            c = el.get("center", {})
            lon, lat = c.get("lon"), c.get("lat")
        if lon is None:
            continue
        rows.append((name, kind(t), round(lat, 5), round(lon, 5)))
    seen, uniq = set(), []
    for r in rows:
        if r[0] in seen:
            continue
        seen.add(r[0]); uniq.append(r)
    os.makedirs(DATA, exist_ok=True)
    out = os.path.join(DATA, "dukuh_atas_places.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["name", "type", "lat", "lon"])
        w.writerows(sorted(uniq, key=lambda r: (r[1], r[0])))
    print(f"[ok] {len(uniq)} named places -> {out}")
    print(" by type:", dict(Counter(r[1] for r in uniq)))
    for r in sorted(uniq, key=lambda r: (r[1], r[0])):
        print("  ", r[1].ljust(11), r[0])


if __name__ == "__main__":
    main()
