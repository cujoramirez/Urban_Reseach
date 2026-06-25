from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Optional, List, Dict, Any
import json, math

EDGE_KINDS = {"sidewalk", "footway", "crossing", "jpo", "path", "road_shoulder"}
NODE_TYPES = {
    "crossing_signalized", "crossing_zebra", "jpo", "curb_ramp", "tactile_paving",
    "bench", "shelter", "toilet", "transit_mrt", "transit_tj", "barrier", "kerb",
}
SOURCES = {"field", "osm", "jakartasatu", "tile2net"}
SOURCE_RANK = {"tile2net": 0, "jakartasatu": 1, "osm": 2, "field": 3}


@dataclass
class Edge:
    id: str
    geometry: List[List[float]]            # LineString [[lon,lat], ...]
    street_name: str = ""
    side: str = "n-a"                      # N/E | S/W | n-a
    kind: str = "footway"
    level: int = 0
    has_sidewalk: str = "unknown"          # yes | no | unknown
    width_m: Optional[float] = None
    surface: str = "unknown"               # intact | damaged | unknown
    obstruction: Optional[int] = None      # 0..2
    obstruction_types: List[str] = field(default_factory=list)
    kerb_ramp: Optional[int] = None
    lit: Optional[int] = None
    eyes_on_street: Optional[int] = None
    crossing_spacing_m: Optional[float] = None
    shade: Optional[int] = None
    shade_modeled: Optional[Dict[str, float]] = None
    drainage: Optional[int] = None
    length_m: float = 0.0
    source: str = "osm"
    confidence: str = "med"                # high | med | low
    notes: str = ""


@dataclass
class Node:
    id: str
    geometry: List[float]                  # Point [lon,lat]
    type: str = "barrier"
    level: int = 0
    accessible: str = "unknown"
    source: str = "osm"
    notes: str = ""


def haversine_m(a: List[float], b: List[float]) -> float:
    R = 6371000.0
    lon1, lat1, lon2, lat2 = map(math.radians, [a[0], a[1], b[0], b[1]])
    dlon, dlat = lon2 - lon1, lat2 - lat1
    h = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def line_length_m(coords: List[List[float]]) -> float:
    return sum(haversine_m(coords[i], coords[i + 1]) for i in range(len(coords) - 1))


def _props(obj: Any) -> Dict[str, Any]:
    d = asdict(obj)
    d.pop("geometry", None)
    return d


def edge_to_feature(e: Edge) -> Dict[str, Any]:
    return {"type": "Feature",
            "geometry": {"type": "LineString", "coordinates": e.geometry},
            "properties": _props(e)}


def node_to_feature(n: Node) -> Dict[str, Any]:
    return {"type": "Feature",
            "geometry": {"type": "Point", "coordinates": n.geometry},
            "properties": _props(n)}


def feature_to_edge(f: Dict[str, Any]) -> Edge:
    return Edge(geometry=f["geometry"]["coordinates"], **f["properties"])


def features_to_collection(features: List[Dict[str, Any]]) -> Dict[str, Any]:
    return {"type": "FeatureCollection", "features": features}


def write_geojson(path: str, features: List[Dict[str, Any]]) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(features_to_collection(features), fh, ensure_ascii=False, indent=1)


def read_features(path: str) -> List[Dict[str, Any]]:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh).get("features", [])


def validate_edge(e: Edge) -> None:
    if e.kind not in EDGE_KINDS:
        raise ValueError(f"bad kind: {e.kind}")
    if e.source not in SOURCES:
        raise ValueError(f"bad source: {e.source}")
