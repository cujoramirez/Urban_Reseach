# `investigate/spatial/` — Pedestrian-network foundation

A deterministic, dependency-light pipeline that builds a **routable, accessibility- and
shade-tagged pedestrian network** for the Sudirman corridor (Bundaran HI → Semanggi + one block
of back-streets each side), a per-named-street **walkability gradient** table, and a routing
proof. It serves the research (quantifying the trotoar-vs-back-street gradient) and seeds the
eventual native iOS app (see [`../../act/architecture-notes.md`](../../act/architecture-notes.md)).

Design spec: [`../../docs/superpowers/specs/2026-06-25-sudirman-pedestrian-network-design.md`](../../docs/superpowers/specs/2026-06-25-sudirman-pedestrian-network-design.md).
Schema: [`SCHEMA.md`](SCHEMA.md) (authoritative).

## Run

```bash
python3 -m venv .venv-spatial && source .venv-spatial/bin/activate
pip install -r ../../requirements-spatial.txt
# from the repo root:
python -m pytest investigate/spatial/tests -v        # offline unit tests
python -m investigate.spatial.run_all                # fetch real data -> data/*.geojson, gradient.csv
```

`run_all.py` is the only network-dependent piece (Overpass + Jakarta Satu REST). Everything else
is pure and unit-tested against fixtures.

## Modules

| Module | Responsibility |
|---|---|
| `schema.py` | `Edge`/`Node` model (matches the field audit sheet) + GeoJSON (de)serialization |
| `geo.py` | bbox + named-street clipping |
| `fetch_osm.py` | Overpass → sidewalk/footway/crossing edges + amenity nodes |
| `fetch_jakartasatu.py` | Jakarta Satu ArcGIS REST → JPO/road/land-use/NDVI/UHI/LST |
| `ingest_field.py` | field audit CSV + media points → edges/nodes (the moat layer) |
| `merge.py` | conflate by precedence: **field > osm > jakartasatu > tile2net** |
| `analyze_gradient.py` | per-street sidewalk coverage/length/shade table |
| `route_demo.py` | networkx walkability-cost routing (incl. shade-aware) |
| `run_all.py` | orchestrates the above |

## Honesty & licensing

- **No invented data.** Missing values stay `unknown`/`None`. A segment with no geometry is
  dropped, never given a guessed line.
- **Absence in a source ≠ ground absence.** OSM (and, later, model) gaps are coverage gaps, not
  proof a sidewalk is missing on the ground. Validate against the field audit.
- **Tiles are local-only** (Track B, later plan); never redistributed.
- Attribution: **© OpenStreetMap contributors (ODbL)**; **Pemprov DKI / Jakarta Satu**.

— Tim Riset Pijak
