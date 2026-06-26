from __future__ import annotations
from typing import List, Dict, Any, Optional, Tuple
import csv, json, os, glob
from .schema import Edge, Node, line_length_m


def _f(v: str) -> Optional[float]:
    v = (v or "").strip()
    if v == "":
        return None
    try:
        return float(v)
    except ValueError:
        return None


def _i(v: str) -> Optional[int]:
    f = _f(v)
    return None if f is None else int(f)


def load_segments(geojson: Dict[str, Any]) -> Dict[str, List[List[float]]]:
    out: Dict[str, List[List[float]]] = {}
    for f in geojson.get("features", []):
        sid = (f.get("properties") or {}).get("segment_id")
        g = f.get("geometry") or {}
        if sid and g.get("type") == "LineString":
            out[sid] = g["coordinates"]
    return out


def _has_sidewalk(v: str) -> str:
    return {"0": "no", "1": "unknown", "2": "yes"}.get((v or "").strip(), "unknown")


def audit_rows_to_edges(rows: List[Dict[str, str]],
                        segments: Dict[str, List[List[float]]]) -> List[Edge]:
    out: List[Edge] = []
    for r in rows:
        sid = (r.get("segment_id") or "").strip()
        coords = segments.get(sid)
        if not coords:                     # no geometry -> do NOT invent it
            continue
        types = [t for t in (r.get("obstruction_types") or "").split(";") if t.strip()]
        out.append(Edge(
            id=sid, geometry=coords, street_name=r.get("street_name", ""),
            side=r.get("side", "n-a"), kind="sidewalk",
            has_sidewalk=_has_sidewalk(r.get("sidewalk_present", "")),
            width_m=_f(r.get("width_m", "")), surface=(r.get("surface") or "unknown").strip(),
            obstruction=_i(r.get("obstruction", "")), obstruction_types=types,
            kerb_ramp=_i(r.get("kerb_ramp", "")), lit=_i(r.get("lighting", "")),
            eyes_on_street=_i(r.get("crowd", "")),
            crossing_spacing_m=_f(r.get("crossing_spacing_m", "")),
            shade=_i(r.get("shade", "")), drainage=_i(r.get("drainage", "")),
            length_m=line_length_m(coords), source="field", confidence="high",
            notes=r.get("notes", ""),
        ))
    return out


def media_points_to_nodes(geojson: Dict[str, Any]) -> List[Node]:
    out: List[Node] = []
    for i, f in enumerate(geojson.get("features", [])):
        g = f.get("geometry") or {}
        if g.get("type") != "Point":
            continue
        p = f.get("properties") or {}
        out.append(Node(id=f"field-media-{i}", geometry=g["coordinates"],
                        type="barrier", source="field",
                        notes=f"{p.get('file', '')} {p.get('time_wib', '')}".strip()))
    return out


def ingest(field_dir: str, segments_path: Optional[str]) -> Tuple[List[Edge], List[Node]]:
    edges: List[Edge] = []
    nodes: List[Node] = []
    segs: Dict[str, List[List[float]]] = {}
    if segments_path and os.path.exists(segments_path):
        with open(segments_path, encoding="utf-8") as fh:
            segs = load_segments(json.load(fh))
    for csv_path in glob.glob(os.path.join(field_dir, "data", "audit_*.csv")):
        with open(csv_path, encoding="utf-8") as fh:
            edges += audit_rows_to_edges(list(csv.DictReader(fh)), segs)
    for gj_path in glob.glob(os.path.join(field_dir, "photos", "media-points_*.geojson")):
        with open(gj_path, encoding="utf-8") as fh:
            nodes += media_points_to_nodes(json.load(fh))
    return edges, nodes
