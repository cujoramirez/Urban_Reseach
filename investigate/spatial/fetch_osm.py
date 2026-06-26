from __future__ import annotations
from typing import List, Dict, Any
from .schema import Edge, Node, line_length_m
from .geo import line_in_bbox, in_bbox, BBOX

OVERPASS_ENDPOINTS = ["https://overpass-api.de/api/interpreter",
                      "https://overpass.kumi.systems/api/interpreter"]
# Overpass requires a meaningful User-Agent (else 406/429). Be a good citizen.
HEADERS = {"User-Agent": "TimRisetPijak-Walkability/1.0 (urban walkability research)"}


def build_query(bbox=BBOX) -> str:
    w, s, e, n = bbox
    b = f"{s},{w},{n},{e}"
    return (
        "[out:json][timeout:60];("
        f'way["highway"="footway"]({b});'
        f'way["highway"]["sidewalk"]({b});'
        f'way["highway"="pedestrian"]({b});'
        f'node["amenity"~"bench|shelter|toilets|drinking_water"]({b});'
        ");out geom;"
    )


def _coords(way: Dict[str, Any]) -> List[List[float]]:
    return [[p["lon"], p["lat"]] for p in way.get("geometry", [])]


def osm_to_edges(osm_json: Dict[str, Any]) -> List[Edge]:
    edges: List[Edge] = []
    for el in osm_json.get("elements", []):
        if el.get("type") != "way":
            continue
        coords = _coords(el)
        if len(coords) < 2 or not line_in_bbox(coords):
            continue
        tags = el.get("tags", {})
        fw, hw = tags.get("footway"), tags.get("highway")
        if fw == "sidewalk" or tags.get("sidewalk") in ("both", "left", "right", "yes"):
            kind, has = "sidewalk", "yes"
        elif fw == "crossing" or hw == "crossing":
            kind, has = "crossing", "unknown"
        else:
            kind, has = "footway", "unknown"
        edges.append(Edge(
            id=f"osm-way-{el['id']}", geometry=coords, kind=kind, has_sidewalk=has,
            street_name=tags.get("name", ""), surface="unknown",
            length_m=line_length_m(coords), source="osm", confidence="med",
        ))
    return edges


_AMENITY_TO_TYPE = {"bench": "bench", "shelter": "shelter",
                    "toilets": "toilet", "drinking_water": "shelter"}


def osm_to_nodes(osm_json: Dict[str, Any]) -> List[Node]:
    nodes: List[Node] = []
    for el in osm_json.get("elements", []):
        if el.get("type") != "node":
            continue
        pt = [el["lon"], el["lat"]]
        if not in_bbox(pt):
            continue
        amenity = el.get("tags", {}).get("amenity")
        if amenity in _AMENITY_TO_TYPE:
            nodes.append(Node(id=f"osm-node-{el['id']}", geometry=pt,
                              type=_AMENITY_TO_TYPE[amenity], source="osm"))
    return nodes


def fetch_overpass(query: str, endpoints: List[str] = None) -> Dict[str, Any]:
    import requests
    last = "no endpoints tried"
    for url in (endpoints or OVERPASS_ENDPOINTS):
        try:
            r = requests.post(url, data={"data": query}, headers=HEADERS, timeout=90)
            if r.status_code == 200:
                return r.json()
            last = f"{url} -> HTTP {r.status_code}"
        except requests.RequestException as ex:
            last = f"{url} -> {type(ex).__name__}"
    raise RuntimeError(f"all Overpass endpoints failed (last: {last})")
