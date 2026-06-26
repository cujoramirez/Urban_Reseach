from __future__ import annotations
from typing import List, Dict, Any
from urllib.parse import urlencode
from .schema import Edge, Node, line_length_m
from .geo import in_bbox, line_in_bbox, BBOX

BASE = "https://jakartasatu.jakarta.go.id/server/rest/services"
SERVICES = {
    "JPO_Bina_Marga": f"{BASE}/JPO_Bina_Marga/MapServer/0",
    "DBM_JALAN": f"{BASE}/DBM_JALAN_BARAT/MapServer/0",
    "Penggunaan_Lahan": f"{BASE}/Penggunaan_Lahan/MapServer/0",
    "NDVI_Jakarta_2022": f"{BASE}/NDVI_Jakarta_2022/MapServer/0",
    "UHI": f"{BASE}/UHI/MapServer/0",
    "LST": f"{BASE}/LST/MapServer/0",
}


def build_query_url(service: str, bbox=BBOX) -> str:
    w, s, e, n = bbox
    params = {
        "where": "1=1", "outFields": "*", "f": "geojson",
        "geometry": f"{w},{s},{e},{n}", "geometryType": "esriGeometryEnvelope",
        "inSR": "4326", "outSR": "4326", "spatialRel": "esriSpatialRelIntersects",
    }
    return f"{SERVICES.get(service, service)}/query?{urlencode(params)}"


def arcgis_points_to_nodes(geojson: Dict[str, Any], node_type: str) -> List[Node]:
    level = 1 if node_type == "jpo" else 0
    out: List[Node] = []
    for i, f in enumerate(geojson.get("features", [])):
        g = f.get("geometry") or {}
        if g.get("type") != "Point" or not in_bbox(g["coordinates"]):
            continue
        name = (f.get("properties") or {}).get("NAMA", "")
        out.append(Node(id=f"js-{node_type}-{i}", geometry=g["coordinates"],
                        type=node_type, level=level, source="jakartasatu", notes=name))
    return out


def arcgis_lines_to_edges(geojson: Dict[str, Any], kind: str) -> List[Edge]:
    out: List[Edge] = []
    for i, f in enumerate(geojson.get("features", [])):
        g = f.get("geometry") or {}
        if g.get("type") != "LineString" or not line_in_bbox(g["coordinates"]):
            continue
        coords = g["coordinates"]
        props = f.get("properties") or {}
        out.append(Edge(id=f"js-{kind}-{i}", geometry=coords, kind=kind,
                        street_name=props.get("NAMA", ""), length_m=line_length_m(coords),
                        source="jakartasatu", confidence="med"))
    return out


def fetch_geojson(url: str) -> Dict[str, Any]:
    import requests
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    return r.json()
