# Pedestrian-Network Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a deterministic, dependency-light Python pipeline that produces a routable, accessibility-tagged pedestrian network GeoJSON for the Sudirman corridor (HI–Semanggi + one block of back-streets), a per-named-street walkability "gradient" table, and a networkx routing proof.

**Architecture:** A small package under `investigate/spatial/`. A shared `schema.py` defines `Edge`/`Node` dataclasses and GeoJSON (de)serialization — every other module produces or consumes these. Source adapters (`fetch_osm`, `fetch_jakartasatu`, `ingest_field`) each output schema objects from one source; `merge.py` conflates them by precedence; `analyze_gradient.py` and `route_demo.py` consume the merged network. All network I/O is isolated in thin `fetch_*` functions; all transforms are pure and unit-tested against fixtures (tests never hit the network).

**Tech Stack:** Python 3.9 (stdlib + `requests` for fetching, `networkx` for routing), `pytest` for tests. Geometry length via a pure-Python haversine (no shapely — keeps the existing py3.9 `.venv` ethos of minimal deps).

## Global Constraints

- **Python 3.9 compatible.** Every module starts with `from __future__ import annotations`; no 3.10+ syntax at runtime.
- **No invented data.** Missing values are `None` / `"unknown"`, never guessed. Absence in a source ≠ ground absence.
- **Provenance precedence:** `field` > `osm` > `jakartasatu` > `tile2net`. Every feature carries `source` and `confidence`.
- **Locked scope:** named streets only; canonical study area = Jl. Jenderal Sudirman (Bundaran HI → Semanggi) + one block of back-streets each side. Working bbox `(W,S,E,N) = (106.808, -6.225, 106.827, -6.1925)`.
- **Tests are offline.** Pure transforms tested with committed JSON fixtures; no test makes a network call.
- **Licensing footer** in `README.md` and any human-readable output: © OpenStreetMap contributors (ODbL); Pemprov DKI / Jakarta Satu; tiles local-only.
- **Segment ID convention:** `SUD-N-03` style, matching `investigate/field/instruments/audit-sheet.md` and `investigate/field/data/`.
- **Commit cadence:** one commit per task, on branch `spatial-pedestrian-network`.

---

## File Structure

```
investigate/spatial/
  __init__.py
  schema.py            # Edge/Node dataclasses, GeoJSON (de)serialize, haversine, validation
  geo.py               # bbox + named-street clipping helpers (pure)
  fetch_osm.py         # Overpass query + osm_json -> Edge/Node
  fetch_jakartasatu.py # ArcGIS REST query + arcgis_json -> Node/Edge
  ingest_field.py      # media-points geojson -> Node; audit csv + segments.geojson -> Edge
  merge.py             # precedence conflation by id
  analyze_gradient.py  # per-street coverage/length/shade table
  route_demo.py        # networkx graph + walkability cost + path
  run_all.py           # orchestrates fetch->merge->analyze->route (network; not unit-tested)
  README.md  SCHEMA.md
  data/                # outputs (committed; small)
  tests/
    __init__.py
    fixtures/          # committed sample JSON
    test_schema.py  test_geo.py  test_fetch_osm.py  test_fetch_jakartasatu.py
    test_ingest_field.py  test_merge.py  test_analyze_gradient.py  test_route_demo.py
requirements-spatial.txt
```

Setup note (run once before Task 1, not a tracked step): `python3 -m venv .venv-spatial && source .venv-spatial/bin/activate && pip install requests networkx pytest`.

---

### Task 1: Schema module (`schema.py`)

**Files:**
- Create: `investigate/spatial/__init__.py` (empty)
- Create: `investigate/spatial/schema.py`
- Create: `investigate/spatial/tests/__init__.py` (empty)
- Test: `investigate/spatial/tests/test_schema.py`
- Create: `requirements-spatial.txt`

**Interfaces:**
- Produces: `Edge`, `Node` dataclasses (fields per spec §4); `edge_to_feature(e: Edge) -> dict`; `node_to_feature(n: Node) -> dict`; `features_to_collection(features: list[dict]) -> dict`; `feature_to_edge(f: dict) -> Edge`; `write_geojson(path: str, features: list[dict]) -> None`; `read_features(path: str) -> list[dict]`; `haversine_m(a: list[float], b: list[float]) -> float`; `line_length_m(coords: list[list[float]]) -> float`; `validate_edge(e: Edge) -> None`. Constants `EDGE_KINDS`, `NODE_TYPES`, `SOURCES`, `SOURCE_RANK`.

- [ ] **Step 1: Write the failing test**

```python
# investigate/spatial/tests/test_schema.py
from investigate.spatial.schema import (
    Edge, Node, edge_to_feature, node_to_feature, features_to_collection,
    feature_to_edge, line_length_m, validate_edge, SOURCE_RANK,
)
import math, pytest

def test_edge_roundtrips_through_geojson_feature():
    e = Edge(id="SUD-N-03", geometry=[[106.82, -6.20], [106.82, -6.201]],
             street_name="Jl. Jenderal Sudirman", side="N/E", kind="sidewalk",
             has_sidewalk="yes", width_m=2.4, source="osm")
    f = edge_to_feature(e)
    assert f["type"] == "Feature"
    assert f["geometry"]["type"] == "LineString"
    assert f["geometry"]["coordinates"] == e.geometry
    assert f["properties"]["has_sidewalk"] == "yes"
    assert "geometry" not in f["properties"]
    back = feature_to_edge(f)
    assert back.id == "SUD-N-03" and back.width_m == 2.4 and back.kind == "sidewalk"

def test_node_to_feature_is_point():
    n = Node(id="jpo-1", geometry=[106.815, -6.218], type="jpo", level=1)
    f = node_to_feature(n)
    assert f["geometry"]["type"] == "Point"
    assert f["properties"]["type"] == "jpo" and f["properties"]["level"] == 1

def test_line_length_m_matches_haversine():
    # ~111 m north-south near the equator for 0.001 deg latitude
    d = line_length_m([[106.82, -6.20], [106.82, -6.201]])
    assert math.isclose(d, 111.0, abs_tol=2.0)

def test_features_to_collection_wraps_list():
    fc = features_to_collection([node_to_feature(Node(id="b1", geometry=[1.0, 2.0], type="bench"))])
    assert fc["type"] == "FeatureCollection" and len(fc["features"]) == 1

def test_validate_edge_rejects_unknown_kind_and_source():
    with pytest.raises(ValueError):
        validate_edge(Edge(id="x", geometry=[[0,0],[0,1]], kind="teleporter"))
    with pytest.raises(ValueError):
        validate_edge(Edge(id="x", geometry=[[0,0],[0,1]], source="vibes"))

def test_source_rank_orders_field_above_osm():
    assert SOURCE_RANK["field"] > SOURCE_RANK["osm"] > SOURCE_RANK["jakartasatu"] > SOURCE_RANK["tile2net"]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest investigate/spatial/tests/test_schema.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'investigate.spatial.schema'`

- [ ] **Step 3: Write minimal implementation**

```python
# investigate/spatial/schema.py
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m pytest investigate/spatial/tests/test_schema.py -v`
Expected: PASS (6 passed)

- [ ] **Step 5: Commit**

```bash
printf "requests\nnetworkx\npytest\n" > requirements-spatial.txt
touch investigate/spatial/__init__.py investigate/spatial/tests/__init__.py
git add investigate/spatial/__init__.py investigate/spatial/schema.py \
        investigate/spatial/tests/__init__.py investigate/spatial/tests/test_schema.py \
        requirements-spatial.txt
git commit -m "feat(spatial): add Edge/Node schema with GeoJSON serialization"
```

---

### Task 2: Geo clipping helpers (`geo.py`)

**Files:**
- Create: `investigate/spatial/geo.py`
- Test: `investigate/spatial/tests/test_geo.py`

**Interfaces:**
- Consumes: nothing.
- Produces: `BBOX` constant `(106.808, -6.225, 106.827, -6.1925)`; `in_bbox(pt: list[float], bbox=BBOX) -> bool`; `line_in_bbox(coords: list[list[float]], bbox=BBOX) -> bool` (True if any vertex inside); `NAMED_STREETS: set[str]` (lowercased canonical names + back-streets); `normalize_street(name: str) -> str`.

- [ ] **Step 1: Write the failing test**

```python
# investigate/spatial/tests/test_geo.py
from investigate.spatial.geo import in_bbox, line_in_bbox, normalize_street, NAMED_STREETS, BBOX

def test_in_bbox_true_for_corridor_point():
    assert in_bbox([106.820, -6.205]) is True

def test_in_bbox_false_outside():
    assert in_bbox([106.700, -6.300]) is False

def test_line_in_bbox_true_if_any_vertex_inside():
    assert line_in_bbox([[106.700, -6.300], [106.820, -6.205]]) is True

def test_normalize_street_lowercases_and_strips():
    assert normalize_street("  Jl. Jenderal SUDIRMAN ") == "jl. jenderal sudirman"

def test_named_streets_includes_sudirman_and_a_backstreet():
    assert "jl. jenderal sudirman" in NAMED_STREETS
    assert any("benhil" in s or "bendungan hilir" in s for s in NAMED_STREETS)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest investigate/spatial/tests/test_geo.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
# investigate/spatial/geo.py
from __future__ import annotations
from typing import List, Tuple

BBOX: Tuple[float, float, float, float] = (106.808, -6.225, 106.827, -6.1925)  # W,S,E,N

NAMED_STREETS = {
    "jl. jenderal sudirman", "jl. jend. sudirman",
    "jl. karet tengsin", "jl. bendungan hilir", "benhil", "jl. gelora",
    "jl. kendal", "jl. blora", "jl. setiabudi", "jl. karet",
}

def in_bbox(pt: List[float], bbox=BBOX) -> bool:
    w, s, e, n = bbox
    return w <= pt[0] <= e and s <= pt[1] <= n

def line_in_bbox(coords: List[List[float]], bbox=BBOX) -> bool:
    return any(in_bbox(p, bbox) for p in coords)

def normalize_street(name: str) -> str:
    return (name or "").strip().lower()
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m pytest investigate/spatial/tests/test_geo.py -v`
Expected: PASS (5 passed)

- [ ] **Step 5: Commit**

```bash
git add investigate/spatial/geo.py investigate/spatial/tests/test_geo.py
git commit -m "feat(spatial): add bbox + named-street clipping helpers"
```

---

### Task 3: OSM adapter (`fetch_osm.py`)

**Files:**
- Create: `investigate/spatial/fetch_osm.py`
- Create: `investigate/spatial/tests/fixtures/osm_sample.json`
- Test: `investigate/spatial/tests/test_fetch_osm.py`

**Interfaces:**
- Consumes: `Edge`, `Node`, `line_length_m` (Task 1); `line_in_bbox` (Task 2).
- Produces: `build_query(bbox) -> str`; `osm_to_edges(osm_json: dict) -> list[Edge]`; `osm_to_nodes(osm_json: dict) -> list[Node]`; `fetch_overpass(query: str, endpoints: list[str]) -> dict` (network).
- Mapping rules: a `way` with `highway=footway` & `footway=sidewalk` → Edge(kind="sidewalk", has_sidewalk="yes"); `highway=footway` → kind="footway"; `highway=crossing` or `footway=crossing` → kind="crossing". `amenity=bench` node → Node(type="bench"); `highway=elevator`/`bridge`+foot → out of scope here. `source="osm"`, `confidence="med"`.

- [ ] **Step 1: Write the failing test**

Create the fixture first:

```json
// investigate/spatial/tests/fixtures/osm_sample.json
{"elements": [
  {"type": "way", "id": 1, "nodes": [10, 11],
   "tags": {"highway": "footway", "footway": "sidewalk", "name": "Jl. Jenderal Sudirman"},
   "geometry": [{"lon": 106.820, "lat": -6.200}, {"lon": 106.820, "lat": -6.201}]},
  {"type": "way", "id": 2, "nodes": [12, 13],
   "tags": {"highway": "footway", "footway": "crossing"},
   "geometry": [{"lon": 106.700, "lat": -6.300}, {"lon": 106.701, "lat": -6.301}]},
  {"type": "node", "id": 20, "lon": 106.821, "lat": -6.2005, "tags": {"amenity": "bench"}}
]}
```

```python
# investigate/spatial/tests/test_fetch_osm.py
import json, os
from investigate.spatial.fetch_osm import build_query, osm_to_edges, osm_to_nodes

FIX = os.path.join(os.path.dirname(__file__), "fixtures", "osm_sample.json")

def load():
    with open(FIX) as fh:
        return json.load(fh)

def test_build_query_contains_bbox_and_footway():
    q = build_query((106.808, -6.225, 106.827, -6.1925))
    assert "footway" in q and "-6.225" in q and "106.827" in q

def test_osm_to_edges_maps_sidewalk_and_crossing_and_clips_bbox():
    edges = osm_to_edges(load())
    # way 2 is outside bbox -> clipped out; only way 1 remains
    assert len(edges) == 1
    e = edges[0]
    assert e.kind == "sidewalk" and e.has_sidewalk == "yes"
    assert e.street_name == "Jl. Jenderal Sudirman"
    assert e.source == "osm" and e.length_m > 100
    assert e.id == "osm-way-1"

def test_osm_to_nodes_maps_bench():
    nodes = osm_to_nodes(load())
    assert len(nodes) == 1 and nodes[0].type == "bench" and nodes[0].source == "osm"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest investigate/spatial/tests/test_fetch_osm.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
# investigate/spatial/fetch_osm.py
from __future__ import annotations
from typing import List, Dict, Any
from .schema import Edge, Node, line_length_m
from .geo import line_in_bbox, in_bbox, BBOX

OVERPASS_ENDPOINTS = ["https://overpass-api.de/api/interpreter",
                      "https://overpass.kumi.systems/api/interpreter"]

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
    for url in (endpoints or OVERPASS_ENDPOINTS):
        try:
            r = requests.post(url, data={"data": query}, timeout=90)
            if r.status_code == 200:
                return r.json()
        except requests.RequestException:
            continue
    raise RuntimeError("all Overpass endpoints failed")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m pytest investigate/spatial/tests/test_fetch_osm.py -v`
Expected: PASS (3 passed)

- [ ] **Step 5: Commit**

```bash
git add investigate/spatial/fetch_osm.py investigate/spatial/tests/test_fetch_osm.py \
        investigate/spatial/tests/fixtures/osm_sample.json
git commit -m "feat(spatial): add OSM Overpass adapter (sidewalk/footway/crossing + amenities)"
```

---

### Task 4: Jakarta Satu adapter (`fetch_jakartasatu.py`)

**Files:**
- Create: `investigate/spatial/fetch_jakartasatu.py`
- Create: `investigate/spatial/tests/fixtures/arcgis_jpo.json`
- Test: `investigate/spatial/tests/test_fetch_jakartasatu.py`

**Interfaces:**
- Consumes: `Node`, `Edge`, `line_length_m` (Task 1); `in_bbox`, `line_in_bbox` (Task 2).
- Produces: `build_query_url(service: str, bbox=BBOX) -> str`; `arcgis_points_to_nodes(geojson: dict, node_type: str) -> list[Node]`; `arcgis_lines_to_edges(geojson: dict, kind: str) -> list[Edge]`; `SERVICES: dict[str,str]` (layer → REST base). All features get `source="jakartasatu"`.

- [ ] **Step 1: Write the failing test**

```json
// investigate/spatial/tests/fixtures/arcgis_jpo.json
{"type": "FeatureCollection", "features": [
  {"type": "Feature", "geometry": {"type": "Point", "coordinates": [106.815, -6.218]},
   "properties": {"NAMA": "JPO Semanggi"}},
  {"type": "Feature", "geometry": {"type": "Point", "coordinates": [106.700, -6.300]},
   "properties": {"NAMA": "JPO Outside"}}
]}
```

```python
# investigate/spatial/tests/test_fetch_jakartasatu.py
import json, os
from investigate.spatial.fetch_jakartasatu import build_query_url, arcgis_points_to_nodes, SERVICES

FIX = os.path.join(os.path.dirname(__file__), "fixtures", "arcgis_jpo.json")

def test_build_query_url_requests_geojson_and_bbox():
    url = build_query_url("JPO_Bina_Marga")
    assert "f=geojson" in url and "geometryType=esriGeometryEnvelope" in url
    assert "JPO_Bina_Marga" in url

def test_services_map_has_expected_layers():
    for key in ("JPO_Bina_Marga", "DBM_JALAN", "Penggunaan_Lahan", "NDVI_Jakarta_2022"):
        assert key in SERVICES

def test_points_to_nodes_clips_bbox_and_tags_jpo():
    with open(FIX) as fh:
        gj = json.load(fh)
    nodes = arcgis_points_to_nodes(gj, "jpo")
    assert len(nodes) == 1  # outside-bbox feature dropped
    assert nodes[0].type == "jpo" and nodes[0].level == 1 and nodes[0].source == "jakartasatu"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest investigate/spatial/tests/test_fetch_jakartasatu.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
# investigate/spatial/fetch_jakartasatu.py
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
```

> Note: REST layer indices (`/0`) and the `DBM_JALAN_BARAT` name are best-effort; `run_all.py` logs a warning and skips a layer that 404s rather than failing the run (handled in Task 8).

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m pytest investigate/spatial/tests/test_fetch_jakartasatu.py -v`
Expected: PASS (3 passed)

- [ ] **Step 5: Commit**

```bash
git add investigate/spatial/fetch_jakartasatu.py investigate/spatial/tests/test_fetch_jakartasatu.py \
        investigate/spatial/tests/fixtures/arcgis_jpo.json
git commit -m "feat(spatial): add Jakarta Satu ArcGIS REST adapter"
```

---

### Task 5: Field ingest (`ingest_field.py`)

**Files:**
- Create: `investigate/spatial/ingest_field.py`
- Create: `investigate/spatial/tests/fixtures/audit_sample.csv`
- Create: `investigate/spatial/tests/fixtures/segments_sample.geojson`
- Test: `investigate/spatial/tests/test_ingest_field.py`

**Interfaces:**
- Consumes: `Edge`, `Node` (Task 1).
- Produces: `media_points_to_nodes(geojson: dict) -> list[Node]`; `load_segments(geojson: dict) -> dict[str, list[list[float]]]` (segment_id → coords); `audit_rows_to_edges(rows: list[dict], segments: dict) -> list[Edge]`; `ingest(field_dir: str, segments_path: str|None) -> tuple[list[Edge], list[Node]]` (gracefully returns `[]` for missing inputs).
- Audit CSV columns (from audit-sheet.md): `segment_id,street_name,side,sidewalk_present,width_m,surface,obstruction,obstruction_types,kerb_ramp,lighting,crowd,crossing_spacing_m,shade,drainage,notes`. Scores 0–2; `sidewalk_present` 0/1/2 → has_sidewalk no/unknown/yes.

- [ ] **Step 1: Write the failing test**

```csv
// investigate/spatial/tests/fixtures/audit_sample.csv
segment_id,street_name,side,sidewalk_present,width_m,surface,obstruction,obstruction_types,kerb_ramp,lighting,crowd,crossing_spacing_m,shade,drainage,notes
SUD-N-03,Jl. Jenderal Sudirman,N/E,2,2.4,intact,2,,2,2,2,150,1,2,wide trotoar
KEN-S-01,Jl. Kendal,S/W,0,,unknown,0,parked motorbikes;vendors,0,1,1,,0,0,no sidewalk
```

```json
// investigate/spatial/tests/fixtures/segments_sample.geojson
{"type": "FeatureCollection", "features": [
  {"type": "Feature", "geometry": {"type": "LineString",
    "coordinates": [[106.820, -6.200], [106.820, -6.201]]},
   "properties": {"segment_id": "SUD-N-03"}}
]}
```

```python
# investigate/spatial/tests/test_ingest_field.py
import csv, json, os
from investigate.spatial.ingest_field import (
    load_segments, audit_rows_to_edges, media_points_to_nodes)

HERE = os.path.dirname(__file__)
AUDIT = os.path.join(HERE, "fixtures", "audit_sample.csv")
SEGS = os.path.join(HERE, "fixtures", "segments_sample.geojson")

def test_load_segments_maps_id_to_coords():
    with open(SEGS) as fh:
        segs = load_segments(json.load(fh))
    assert segs["SUD-N-03"][0] == [106.820, -6.200]

def test_audit_rows_to_edges_attaches_attributes_for_known_segment_only():
    with open(SEGS) as fh:
        segs = load_segments(json.load(fh))
    with open(AUDIT) as fh:
        rows = list(csv.DictReader(fh))
    edges = audit_rows_to_edges(rows, segs)
    # KEN-S-01 has no geometry in segments -> dropped (no invented geometry)
    assert len(edges) == 1
    e = edges[0]
    assert e.id == "SUD-N-03" and e.source == "field" and e.confidence == "high"
    assert e.has_sidewalk == "yes" and e.width_m == 2.4 and e.shade == 1
    assert e.obstruction == 2

def test_media_points_to_nodes_reads_real_geojson_shape():
    gj = {"type": "FeatureCollection", "features": [
        {"type": "Feature", "geometry": {"type": "Point", "coordinates": [106.8226, -6.2021]},
         "properties": {"file": "IMG_0201.MOV", "type": "video", "time_wib": "2026-06-18T10:37:43"}}]}
    nodes = media_points_to_nodes(gj)
    assert len(nodes) == 1 and nodes[0].source == "field" and nodes[0].type == "barrier"
    assert "IMG_0201.MOV" in nodes[0].notes
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest investigate/spatial/tests/test_ingest_field.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
# investigate/spatial/ingest_field.py
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

def audit_rows_to_edges(rows: List[Dict[str, str]], segments: Dict[str, List[List[float]]]) -> List[Edge]:
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
                        notes=f"{p.get('file','')} {p.get('time_wib','')}".strip()))
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m pytest investigate/spatial/tests/test_ingest_field.py -v`
Expected: PASS (3 passed)

- [ ] **Step 5: Commit**

```bash
git add investigate/spatial/ingest_field.py investigate/spatial/tests/test_ingest_field.py \
        investigate/spatial/tests/fixtures/audit_sample.csv \
        investigate/spatial/tests/fixtures/segments_sample.geojson
git commit -m "feat(spatial): ingest field audit CSV + media points (no invented geometry)"
```

---

### Task 6: Merge by precedence (`merge.py`)

**Files:**
- Create: `investigate/spatial/merge.py`
- Test: `investigate/spatial/tests/test_merge.py`

**Interfaces:**
- Consumes: `Edge`, `Node`, `SOURCE_RANK` (Task 1).
- Produces: `merge_edges(*edge_lists: list[Edge]) -> list[Edge]`; `merge_nodes(*node_lists: list[Node]) -> list[Node]`. Merge key for edges = `id`. When two edges share an id, the higher-`SOURCE_RANK` edge wins as the base, and any non-`None`/non-`"unknown"` attribute from the higher-rank edge overrides; lower-rank fills only gaps. Nodes dedupe by `id` keeping higher rank.

- [ ] **Step 1: Write the failing test**

```python
# investigate/spatial/tests/test_merge.py
from investigate.spatial.schema import Edge, Node
from investigate.spatial.merge import merge_edges, merge_nodes

def test_merge_edges_field_overrides_osm_for_same_id():
    osm = Edge(id="SUD-N-03", geometry=[[0,0],[0,1]], kind="sidewalk",
               has_sidewalk="unknown", width_m=None, source="osm")
    field = Edge(id="SUD-N-03", geometry=[[0,0],[0,1]], kind="sidewalk",
                 has_sidewalk="yes", width_m=2.4, shade=1, source="field", confidence="high")
    merged = merge_edges([osm], [field])
    assert len(merged) == 1
    m = merged[0]
    assert m.source == "field" and m.has_sidewalk == "yes" and m.width_m == 2.4 and m.shade == 1

def test_merge_edges_lower_rank_fills_gaps_only():
    osm = Edge(id="A", geometry=[[0,0],[0,1]], width_m=3.0, source="osm")
    field = Edge(id="A", geometry=[[0,0],[0,1]], width_m=None, shade=2, source="field")
    m = merge_edges([osm], [field])[0]
    assert m.shade == 2 and m.width_m == 3.0  # osm width fills field's gap

def test_merge_edges_keeps_distinct_ids():
    a = Edge(id="A", geometry=[[0,0],[0,1]], source="osm")
    b = Edge(id="B", geometry=[[1,1],[1,2]], source="osm")
    assert len(merge_edges([a, b])) == 2

def test_merge_nodes_dedupes_by_id_keeping_higher_rank():
    n_osm = Node(id="n1", geometry=[0,0], type="bench", source="osm")
    n_field = Node(id="n1", geometry=[0,0], type="bench", accessible="yes", source="field")
    out = merge_nodes([n_osm], [n_field])
    assert len(out) == 1 and out[0].source == "field" and out[0].accessible == "yes"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest investigate/spatial/tests/test_merge.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
# investigate/spatial/merge.py
from __future__ import annotations
from typing import List, Dict
from dataclasses import fields
from .schema import Edge, Node, SOURCE_RANK

_EMPTY = (None, "", "unknown", "n-a", [], 0.0)

def _meaningful(value) -> bool:
    return value not in _EMPTY

def _combine(high: Edge, low: Edge) -> Edge:
    for f in fields(Edge):
        if f.name in ("id", "geometry", "source", "confidence"):
            continue
        if not _meaningful(getattr(high, f.name)) and _meaningful(getattr(low, f.name)):
            setattr(high, f.name, getattr(low, f.name))
    return high

def merge_edges(*edge_lists: List[Edge]) -> List[Edge]:
    by_id: Dict[str, Edge] = {}
    for edges in edge_lists:
        for e in edges:
            cur = by_id.get(e.id)
            if cur is None:
                by_id[e.id] = e
            elif SOURCE_RANK[e.source] >= SOURCE_RANK[cur.source]:
                by_id[e.id] = _combine(e, cur)
            else:
                by_id[e.id] = _combine(cur, e)
    return list(by_id.values())

def merge_nodes(*node_lists: List[Node]) -> List[Node]:
    by_id: Dict[str, Node] = {}
    for nodes in node_lists:
        for n in nodes:
            cur = by_id.get(n.id)
            if cur is None or SOURCE_RANK[n.source] >= SOURCE_RANK[cur.source]:
                by_id[n.id] = n
    return list(by_id.values())
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m pytest investigate/spatial/tests/test_merge.py -v`
Expected: PASS (4 passed)

- [ ] **Step 5: Commit**

```bash
git add investigate/spatial/merge.py investigate/spatial/tests/test_merge.py
git commit -m "feat(spatial): merge sources by provenance precedence (field>osm>js>tile2net)"
```

---

### Task 7: Gradient analysis (`analyze_gradient.py`)

**Files:**
- Create: `investigate/spatial/analyze_gradient.py`
- Test: `investigate/spatial/tests/test_analyze_gradient.py`

**Interfaces:**
- Consumes: `Edge` (Task 1); `normalize_street` (Task 2).
- Produces: `gradient_by_street(edges: list[Edge]) -> list[dict]` (one row per street: `street_name,total_len_m,sidewalk_len_m,sidewalk_pct,mean_width_m,mean_shade`); `write_gradient_csv(rows: list[dict], path: str) -> None`. Sidewalk length = sum of `length_m` where `has_sidewalk == "yes"`. Means ignore `None`. Rows sorted by `sidewalk_pct` descending.

- [ ] **Step 1: Write the failing test**

```python
# investigate/spatial/tests/test_analyze_gradient.py
from investigate.spatial.schema import Edge
from investigate.spatial.analyze_gradient import gradient_by_street

def test_gradient_computes_pct_and_means_per_street():
    edges = [
        Edge(id="1", geometry=[[0,0],[0,1]], street_name="Jl. Jenderal Sudirman",
             has_sidewalk="yes", width_m=2.4, shade=2, length_m=100.0),
        Edge(id="2", geometry=[[0,0],[0,1]], street_name="Jl. Jenderal Sudirman",
             has_sidewalk="yes", width_m=2.0, shade=1, length_m=100.0),
        Edge(id="3", geometry=[[0,0],[0,1]], street_name="Jl. Kendal",
             has_sidewalk="no", width_m=None, shade=0, length_m=100.0),
    ]
    rows = gradient_by_street(edges)
    sud = next(r for r in rows if r["street_name"] == "Jl. Jenderal Sudirman")
    ken = next(r for r in rows if r["street_name"] == "Jl. Kendal")
    assert sud["sidewalk_pct"] == 100.0 and sud["mean_width_m"] == 2.2 and sud["mean_shade"] == 1.5
    assert ken["sidewalk_pct"] == 0.0 and ken["mean_width_m"] is None
    assert rows[0]["sidewalk_pct"] >= rows[-1]["sidewalk_pct"]  # sorted desc
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest investigate/spatial/tests/test_analyze_gradient.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
# investigate/spatial/analyze_gradient.py
from __future__ import annotations
from typing import List, Dict, Any, Optional
import csv
from .schema import Edge

def _mean(vals: List[float]) -> Optional[float]:
    vals = [v for v in vals if v is not None]
    return round(sum(vals) / len(vals), 4) if vals else None

def gradient_by_street(edges: List[Edge]) -> List[Dict[str, Any]]:
    groups: Dict[str, List[Edge]] = {}
    for e in edges:
        groups.setdefault(e.street_name or "(unnamed)", []).append(e)
    rows: List[Dict[str, Any]] = []
    for name, es in groups.items():
        total = sum(e.length_m for e in es)
        swlen = sum(e.length_m for e in es if e.has_sidewalk == "yes")
        rows.append({
            "street_name": name,
            "total_len_m": round(total, 1),
            "sidewalk_len_m": round(swlen, 1),
            "sidewalk_pct": round(100.0 * swlen / total, 1) if total else 0.0,
            "mean_width_m": _mean([e.width_m for e in es]),
            "mean_shade": _mean([float(e.shade) for e in es if e.shade is not None]),
        })
    rows.sort(key=lambda r: r["sidewalk_pct"], reverse=True)
    return rows

def write_gradient_csv(rows: List[Dict[str, Any]], path: str) -> None:
    cols = ["street_name", "total_len_m", "sidewalk_len_m", "sidewalk_pct",
            "mean_width_m", "mean_shade"]
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m pytest investigate/spatial/tests/test_analyze_gradient.py -v`
Expected: PASS (1 passed)

- [ ] **Step 5: Commit**

```bash
git add investigate/spatial/analyze_gradient.py investigate/spatial/tests/test_analyze_gradient.py
git commit -m "feat(spatial): per-street walkability gradient table"
```

---

### Task 8: Routing proof + orchestrator (`route_demo.py`, `run_all.py`, docs)

**Files:**
- Create: `investigate/spatial/route_demo.py`
- Create: `investigate/spatial/run_all.py`
- Create: `investigate/spatial/README.md`
- Create: `investigate/spatial/SCHEMA.md`
- Modify: `DECISIONS.md` (append one dated entry)
- Test: `investigate/spatial/tests/test_route_demo.py`

**Interfaces:**
- Consumes: `Edge` (Task 1); `networkx`.
- Produces: `DEFAULT_WEIGHTS: dict`; `walkability_cost(edge: Edge, weights=DEFAULT_WEIGHTS, hour: str|None=None) -> float`; `build_graph(edges: list[Edge], weights=DEFAULT_WEIGHTS, hour=None) -> networkx.Graph`; `most_walkable_path(g, start: tuple, end: tuple) -> tuple[list, float]`; `node_key(pt: list[float]) -> tuple` (rounds to 6 dp).

- [ ] **Step 1: Write the failing test**

```python
# investigate/spatial/tests/test_route_demo.py
from investigate.spatial.schema import Edge
from investigate.spatial.route_demo import (
    walkability_cost, build_graph, most_walkable_path, node_key, DEFAULT_WEIGHTS)

def test_missing_sidewalk_costs_more_than_present():
    good = Edge(id="g", geometry=[[0,0],[0,1]], has_sidewalk="yes", length_m=100.0)
    bad = Edge(id="b", geometry=[[0,0],[0,1]], has_sidewalk="no", length_m=100.0)
    assert walkability_cost(bad) > walkability_cost(good)

def test_walkable_path_avoids_gap_even_if_longer():
    # direct A->C has no sidewalk; detour A->B->C does. Detour should win.
    A, B, C = [0.0, 0.0], [0.0005, 0.0], [0.001, 0.0]
    edges = [
        Edge(id="AC", geometry=[A, C], has_sidewalk="no", length_m=111.0),
        Edge(id="AB", geometry=[A, B], has_sidewalk="yes", length_m=55.5),
        Edge(id="BC", geometry=[B, C], has_sidewalk="yes", length_m=55.5),
    ]
    g = build_graph(edges)
    path, cost = most_walkable_path(g, node_key(A), node_key(C))
    assert node_key(B) in path  # routed through the sidewalked detour

def test_shade_hour_penalizes_sun_exposed_edge():
    sunny = Edge(id="s", geometry=[[0,0],[0,1]], has_sidewalk="yes", length_m=100.0,
                 shade_modeled={"12": 0.0})
    shady = Edge(id="h", geometry=[[0,0],[0,1]], has_sidewalk="yes", length_m=100.0,
                 shade_modeled={"12": 1.0})
    assert walkability_cost(sunny, hour="12") > walkability_cost(shady, hour="12")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest investigate/spatial/tests/test_route_demo.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Write minimal implementation**

```python
# investigate/spatial/route_demo.py
from __future__ import annotations
from typing import List, Tuple, Dict, Optional
import networkx as nx
from .schema import Edge

DEFAULT_WEIGHTS = {
    "no_sidewalk": 3.0, "narrow": 1.0, "damaged": 0.8,
    "obstruction": 0.5, "no_shade": 1.2, "unlit": 0.4,
}

def node_key(pt: List[float]) -> Tuple[float, float]:
    return (round(pt[0], 6), round(pt[1], 6))

def walkability_cost(edge: Edge, weights: Dict[str, float] = DEFAULT_WEIGHTS,
                     hour: Optional[str] = None) -> float:
    penalty = 0.0
    if edge.has_sidewalk == "no":
        penalty += weights["no_sidewalk"]
    if edge.width_m is not None and edge.width_m < 1.85:
        penalty += weights["narrow"]
    if edge.surface == "damaged":
        penalty += weights["damaged"]
    if edge.obstruction is not None:
        penalty += weights["obstruction"] * (2 - edge.obstruction) / 2.0
    if hour is not None and edge.shade_modeled is not None:
        shade = edge.shade_modeled.get(hour)
        if shade is not None:
            penalty += weights["no_shade"] * (1.0 - shade)
    if edge.lit == 0:
        penalty += weights["unlit"]
    return max(edge.length_m, 0.1) * (1.0 + penalty)

def build_graph(edges: List[Edge], weights: Dict[str, float] = DEFAULT_WEIGHTS,
                hour: Optional[str] = None) -> nx.Graph:
    g = nx.Graph()
    for e in edges:
        if len(e.geometry) < 2:
            continue
        u, v = node_key(e.geometry[0]), node_key(e.geometry[-1])
        w = walkability_cost(e, weights, hour)
        if not g.has_edge(u, v) or w < g[u][v]["weight"]:
            g.add_edge(u, v, weight=w, edge_id=e.id, length_m=e.length_m)
    return g

def most_walkable_path(g: nx.Graph, start: Tuple, end: Tuple) -> Tuple[List, float]:
    path = nx.shortest_path(g, start, end, weight="weight")
    cost = nx.shortest_path_length(g, start, end, weight="weight")
    return path, cost
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m pytest investigate/spatial/tests/test_route_demo.py -v`
Expected: PASS (3 passed)

- [ ] **Step 5: Write the orchestrator + docs**

```python
# investigate/spatial/run_all.py
"""Fetch -> merge -> analyze -> route. Network-dependent; run manually, not in CI."""
from __future__ import annotations
import os, json
from . import fetch_osm, fetch_jakartasatu, ingest_field, merge, analyze_gradient, route_demo
from .schema import edge_to_feature, node_to_feature, write_geojson, feature_to_edge
from .geo import BBOX

DATA = os.path.join(os.path.dirname(__file__), "data")
FIELD = os.path.join(os.path.dirname(__file__), "..", "field")

def main() -> None:
    os.makedirs(DATA, exist_ok=True)
    osm = fetch_osm.fetch_overpass(fetch_osm.build_query(BBOX))
    osm_edges, osm_nodes = fetch_osm.osm_to_edges(osm), fetch_osm.osm_to_nodes(osm)

    js_nodes = []
    try:
        gj = fetch_jakartasatu.fetch_geojson(fetch_jakartasatu.build_query_url("JPO_Bina_Marga"))
        js_nodes = fetch_jakartasatu.arcgis_points_to_nodes(gj, "jpo")
    except Exception as ex:                       # noqa: BLE001 - layer may 404; keep going
        print(f"[warn] Jakarta Satu JPO skipped: {ex}")

    seg_path = os.path.join(DATA, "segments.geojson")
    field_edges, field_nodes = ingest_field.ingest(FIELD, seg_path if os.path.exists(seg_path) else None)

    edges = merge.merge_edges(osm_edges, field_edges)
    nodes = merge.merge_nodes(osm_nodes, js_nodes, field_nodes)
    write_geojson(os.path.join(DATA, "pedestrian_network.geojson"),
                  [edge_to_feature(e) for e in edges] + [node_to_feature(n) for n in nodes])

    rows = analyze_gradient.gradient_by_street(edges)
    analyze_gradient.write_gradient_csv(rows, os.path.join(DATA, "gradient.csv"))
    print(f"[ok] {len(edges)} edges, {len(nodes)} nodes, {len(rows)} streets")

if __name__ == "__main__":
    main()
```

Create `investigate/spatial/README.md` (purpose, run steps, **licensing footer**: © OpenStreetMap contributors (ODbL); Pemprov DKI / Jakarta Satu; tiles local-only; "OSM/model absence ≠ ground absence"). Create `investigate/spatial/SCHEMA.md` (copy of spec §4 tables, marked authoritative). Append to `DECISIONS.md` one new dated entry (bottom, append-only):

```markdown
## 2026-06-25 — Spatial pedestrian-network foundation (Tim Riset Pijak)
Built `investigate/spatial/`: an OpenSidewalks-aligned, routable pedestrian-network
dataset for the Sudirman corridor (HI–Semanggi + one block each side), sourced
field > OSM > Jakarta Satu (Esri/Tile2Net gap-fill deferred to a later plan). Edge
schema mirrors the field audit sheet; provenance + precedence recorded per feature.
Serves the walkability "gradient" analysis now and seeds the (separate-repo) pedestrian
map app later. Reports stay problem-level; product framing lives here and in `act/`.
```

- [ ] **Step 6: Run the full suite + smoke-run the orchestrator**

Run: `python3 -m pytest investigate/spatial/ -v`
Expected: PASS (all tasks' tests green)
Run: `python3 -m investigate.spatial.run_all` (from repo root, venv active)
Expected: prints `[ok] N edges, M nodes, K streets` and writes `data/pedestrian_network.geojson` + `data/gradient.csv` (Jakarta Satu warning is acceptable).

- [ ] **Step 7: Commit**

```bash
git add investigate/spatial/route_demo.py investigate/spatial/run_all.py \
        investigate/spatial/README.md investigate/spatial/SCHEMA.md \
        investigate/spatial/tests/test_route_demo.py investigate/spatial/data/ DECISIONS.md
git commit -m "feat(spatial): shade-aware routing proof + orchestrator + docs"
```

---

## Self-Review

**Spec coverage:** §4 schema → Task 1; §3 scope/bbox → Task 2; §5 Track A (#1 OSM) → Task 3, (#2 Jakarta Satu) → Task 4, (#3 field) → Task 5; §4.3 precedence → Task 6; §5 #8 gradient → Task 7; §5 #9 routing + §6 cost → Task 8; §9 conventions (no invented data, named-street, licensing, DECISIONS) → Tasks 2/5/8. Deferred to later plans (noted up front): §5 Track B (#4–5 tiles/Tile2Net) → Plan 2; Shade `compute_shade.py` → Plan 3; §10 `export_app.py` PMTiles/GeoPackage → Plan 4. `shade_modeled` field + hour-aware cost are present now (Task 1 + Task 8) so Plan 3 only has to populate them.

**Placeholder scan:** No TBD/TODO; every code step shows complete, runnable code; the Jakarta Satu REST layer-index caveat is handled by graceful skip, not a placeholder.

**Type consistency:** `Edge`/`Node` fields used in Tasks 3–8 match Task 1 definitions; `SOURCE_RANK` (Task 1) used in Task 6; `node_key`/`walkability_cost`/`build_graph` signatures consistent within Task 8; `line_length_m`, `in_bbox`, `line_in_bbox` signatures consistent with Tasks 1–2.
