# Design — Sudirman Corridor Pedestrian-Network Database (+ shade modeling + walkability routing proof)

**Date:** 2026-06-25
**Team:** Tim Riset Pijak
**Status:** Draft for review
**CBL stage:** Investigate (spatial / secondary-data desk work, complementing the 2026-06-18 field audit)

---

## 1. Purpose

Build **one artifact** that serves two payoffs at once:

1. **Research evidence** — a quantified picture of the walkability *gradient*: the wide
   Sudirman trotoar versus the near-absent sidewalks one block behind it, plus heat/shade
   exposure along the corridor (problem-level, ties to the 2026-06-18 field findings).
2. **Seed database** for the eventual pedestrian-first map app (a "Google/Apple/Waze for
   pedestrians" — sidewalks, sideroads, walkability, accessibility, facilities, **shade-aware
   routing**). The app itself lives in a **separate repo**; this repo produces the *data
   foundation* it will import.

The artifact is a **routable, accessibility-tagged pedestrian network** of the Sudirman
corridor, aligned to the **OpenSidewalks schema**, with attributes matched 1:1 to the existing
field audit sheet, plus a **modeled shade index** per segment per hour.

## 2. Non-goals (YAGNI)

- **No app UI, mobile, server, or API code** — that is the separate app repo's job.
- **No render-engine lock-in.** Outputs are engine-agnostic data files; the choice of front
  end (**MapLibre native vs Unity vs both**) is an app-repo decision, deliberately *not* made
  here. The data feeds either.
- **No photoreal 3D model.** Shade is computed from **extruded 2.5D massing + canopy**, not a
  modeled city. Low-res is sufficient and correct.
- **No tile-serving infrastructure.** Esri aerial tiles are downloaded *locally* as gap-fill
  input only; gitignored, never redistributed.
- **No city-wide coverage.** Corridor + one block of back-streets each side.
- **No invented attributes.** Unknowns stay `unknown`, never guessed.
- **No new findings in the reports** (`main_id.tex` / `main_en.tex`) until data is validated;
  product/solution framing stays in `act/`, not the report narrative.

## 3. Study area (named-street definition, per locked scope)

**Spine:** Jl. Jenderal Sudirman, **Bundaran HI** (≈ -6.1944, 106.8229) → **Semanggi**
(≈ -6.2185, 106.8135).

**Back-streets — one block each side:**
- **West:** Karet Tengsin / Bendungan Hilir (Benhil) / Gelora cluster.
- **East:** Kendal / Blora / Setiabudi / Karet cluster.

**Working bbox (W, S, E, N)** ≈ `[106.808, -6.225, 106.827, -6.1925]` — a fetch convenience;
the canonical scope is the **named streets** above. Outside-named-street geometry is clipped.
(Explicitly **not** "Jakarta Selatan", **not** a station list.)

## 4. Data model (OpenSidewalks-aligned, matched to the audit sheet)

GeoJSON, two feature types, provenance on every feature.

### 4.1 Edges (LineString) — traversable pedestrian segments

| Field | Type | Notes / audit-sheet origin |
|---|---|---|
| `id` | string | e.g. `SUD-N-03` (matches audit Segment ID convention) |
| `street_name` | string | named street |
| `side` | enum | `N/E` \| `S/W` \| `n-a` |
| `kind` | enum | `sidewalk`\|`footway`\|`crossing`\|`jpo`\|`path`\|`road_shoulder` |
| `level` | int | vertical level: `0` ground, `+1` overpass/JPO, `-1` underpass (vertical routing) |
| `has_sidewalk` | enum | `yes`\|`no`\|`unknown` (audit #1) |
| `width_m` | float\|null | effective width; std min **1.85 m** (audit #2) |
| `surface` | enum | `intact`\|`damaged`\|`unknown` (audit #3) |
| `obstruction` | 0–2\|null | clear→blocked (audit #4) |
| `obstruction_types` | list | motorbikes, vendors, poles, vegetation… (audit #4) |
| `kerb_ramp` | 0–2\|null | ramp/guiding-block; slope std **≤8% (1:12)** (audit #5) |
| `lit` | 0–2\|null | night lighting (audit #6) |
| `eyes_on_street` | 0–2\|null | crowd / passive surveillance (audit #7) |
| `crossing_spacing_m` | float\|null | std **100–200 m** (audit #8) |
| `shade` | 0–2\|null | **field-observed** shade; THI discomfort **>27 °C** (audit #9) |
| `shade_modeled` | dict\|null | **computed** shade fraction per hour, e.g. `{"09":0.8,"12":0.3,"15":0.6}` (§5, Shade) |
| `drainage` | 0–2\|null | open gutter→covered (audit #10) |
| `length_m` | float | computed |
| `source` | enum | `field`\|`osm`\|`jakartasatu`\|`tile2net` |
| `confidence` | enum | `high`\|`med`\|`low` |
| `notes` | string | |

### 4.2 Nodes (Point) — features & barriers

`id`, `type` (`crossing_signalized`\|`crossing_zebra`\|`jpo`\|`curb_ramp`\|`tactile_paving`\|
`bench`\|`shelter`\|`toilet`\|`transit_mrt`\|`transit_tj`\|`barrier`\|`kerb`), `level` (int),
`accessible` (`yes`\|`no`\|`unknown`), `source`, `notes`.

### 4.3 Provenance & precedence

On disagreement: **field > osm > jakartasatu > tile2net**. `tile2net` geometry is always
`confidence: low`, tagged *candidate to verify in the field* — never authoritative.

## 5. Sources → pipeline modules

All under `investigate/spatial/`. Track A = citable backbone; Track B = exploratory.

**Track A — citable backbone (ship first)**
1. `fetch_osm.py` — Overpass (footway/sidewalk/crossing, `highway` w/ `sidewalk=*`, amenities
   bench/shelter/toilet/drinking_water, transit MRT+TransJakarta, **building footprints +
   `height`/`building:levels`**, trees) → normalized schema → `data/edges_osm.geojson`,
   `data/nodes_osm.geojson`, `data/buildings.geojson`. Mirror fallback (`overpass.kumi.systems`).
2. `fetch_jakartasatu.py` — ArcGIS REST `query?...&f=geojson` clip: `JPO_Bina_Marga`,
   `DBM_JALAN`, `Penggunaan_Lahan`, `NDVI_Jakarta_2022`, `UHI`, `LST` → `data/jakartasatu_*.geojson`.
   NDVI = canopy proxy for shade; UHI/LST = heat context (ties to 06-18 comfort data).
3. `ingest_field.py` — map field outputs into schema: audit CSV → edge attributes;
   `field/photos/media-points_2026-06-18.geojson` → media-attached nodes. **The moat layer**
   (`source: field`, highest confidence).

**Track B — aerial gap-fill (exploratory)**
4. `download_tiles.py` — Esri World Imagery XYZ @ **Z19** (~0.3 m nominal; Esri native ≈0.5 m,
   so Z19 ≈ real limit, Z20 mostly upsampled). Resumable, throttled, `User-Agent`. → `tiles/`
   (gitignored). README carries Esri attribution + ToS note. Est. ~1,000–1,500 tiles.
5. `run_tile2net.py` — **Tile2Net** (pretrained) → predicted sidewalk/crosswalk polygons →
   `data/tile2net_pred.geojson`. Own venv `.venv-cv`. Fallbacks: SAM-2 (assisted digitizing);
   SegFormer/Mask2Former+Swin-L only if fine-tuned (out of pilot scope). *(MapTRv2 rejected —
   vehicle/BEV HD-mapping, not overhead aerial.)*

**Shade computation (pragmatic 2.5D — addresses the "3D" goal without a 3D model)**
6. `compute_shade.py` — inputs: building footprints + heights (Track A #1; fallback
   `levels × 3 m`, default 3 m), tree canopy (NDVI + OSM trees + field shade), and **sun
   position** (solar azimuth/elevation for Jakarta lat/long via `pvlib`/`astral`) at sample
   hours (default 09:00/12:00/15:00 WIB). Cast shadow polygons (`pybdshadow`-style) →
   intersect with edges → write `shade_modeled` fraction per hour onto each edge.
   *Schema is built so SOLWEIG/UMEP (mean radiant temperature) can replace the geometric model
   later without changing consumers.*

**Integration, analysis, routing**
7. `merge.py` — conflate all sources into canonical `data/pedestrian_network.geojson`
   (provenance + precedence §4.3).
8. `analyze_gradient.py` — per-named-street sidewalk coverage/length + mean shade, Sudirman vs
   each back-street → `data/gradient.csv` + Markdown summary. Style follows `field/analyze.py`
   (descriptive, honest about provenance; no inference dressed as a finding).
9. `route_demo.py` — **networkx**: load network, weight edges by **walkability cost** (§6),
   compute a "most-walkable path" (e.g. **Benhil → Bundaran HI**) and a **shade-aware path at
   a chosen hour**, compare vs shortest-distance path. Output route GeoJSON + cost breakdown.
   **Proves the concept; no UI.**

**App-ready export (engine-agnostic)**
10. `export_app.py` — `pedestrian_network.geojson` → **PMTiles** (via `tippecanoe`, render
    layer, bundle-on-device / serverless) **+ GeoPackage/SQLite** (route + query layer). These
    two files are what the app repo imports — consumable by MapLibre *or* Unity (Cesium/ArcGIS
    SDK) alike.

## 6. Walkability cost (routing)

`cost(edge) = length_m × (1 + Σ wᵢ·penaltyᵢ)`; penalties rise for `has_sidewalk=no`, low
`width_m`, `surface=damaged`, high `obstruction`, **low shade for the chosen hour
(`shade_modeled`)**, low `lit`, sparse crossings, and unmatched `level` transitions without a
ramp. Weights `wᵢ` are explicit, documented constants in one place. The walkable/shade-aware
path should visibly diverge from the shortest path at sidewalk gaps and sun-exposed stretches —
that divergence is the demonstrable product value.

## 7. App-ready outputs & render-engine independence

The deliverable data is **decoupled from any renderer**:

- **Render layer:** PMTiles (MapLibre Native reads directly; 2.5D building extrusion + DEM give
  a "3D" look with no modeling). Unity can consume the same data via Cesium/ArcGIS SDK.
- **Route/query layer:** GeoPackage/SQLite on-device (offline) or PostGIS server later.
- **Routing engine (app repo):** Valhalla or GraphHopper (custom pedestrian/shade costing);
  the `route_demo.py` cost model is the reference. For the pilot, embedded A\* suffices.
- **Shade:** `shade_modeled` ships as data; a Unity/AR module can also render it live.

The Unity-vs-native decision is therefore *not blocking* — both front ends import the same files.

## 8. Repo placement & dependencies

```
investigate/spatial/
  README.md  SCHEMA.md
  fetch_osm.py  fetch_jakartasatu.py  ingest_field.py
  download_tiles.py  run_tile2net.py
  compute_shade.py  merge.py  analyze_gradient.py  route_demo.py  export_app.py
  data/      # *.geojson, gradient.csv, *.pmtiles, *.gpkg  (committed; small)
  tiles/     # gitignored (local-only aerial)
requirements-spatial.txt   # requests, shapely, networkx, pvlib/astral, pybdshadow
requirements-cv.txt        # torch, tile2net  (-> .venv-cv)
# tippecanoe via brew (PMTiles)
```

`.gitignore`: `investigate/spatial/tiles/`, `.venv-cv/`, model weights. Existing `.venv`
(py3.9, pdfplumber) untouched.

## 9. Conventions honored (CLAUDE.md / DECISIONS / memory)

- **No invented data**; unknowns stay `unknown`. **OSM/Tile2Net/model absence ≠ ground
  absence** — stated as a limitation.
- **Locked scope**: named streets, the gradient. Not Jakarta Selatan, not a station list.
- **Confirmation-bias guard**: neutral, two-sided attributes; no "people walk in the road
  despite a good sidewalk" pre-baking.
- **No solution bias in the report**: product schema, shade-routing, and stack decisions live in
  `investigate/spatial/` + `act/`; the report narrative stays problem-level.
- **DECISIONS.md** gets one new dated entry (append-only).
- **Team framing** ("Tim Riset Pijak"); ADA branding minimal.
- **Licensing footer** in outputs: © OpenStreetMap contributors (ODbL); Pemprov DKI / Jakarta
  Satu; Esri basemap attribution where used; tiles local-only.

## 10. Validation / testing

- **Fetch sanity:** Overpass returns >0 pedestrian features; valid GeoJSON; required schema
  fields present on every feature.
- **Cross-validation:** Tile2Net predictions vs OSM + field for sidewalk presence (report
  precision/recall; expect canopy/occlusion misses on back-streets).
- **Shade validation:** modeled shade vs **field shade scores (audit #9)** and
  `field/data/weather_2026-06-18.csv` at matching times — report agreement honestly.
- **Routing:** connected path exists Benhil→HI; walkable/shade-aware path cost ordering is sane
  and diverges from the shortest path at a known sidewalk gap / sun-exposed stretch.

## 11. Risks & open questions

- **Building heights** = main shade-data gap. Sudirman towers often height-tagged in OSM;
  back-streets low-rise (fallback `levels × 3 m`, default 3 m). Canopy shade is approximated.
- **Overpass reliability** — mirror fallback.
- **Jakarta Satu REST** — confirm `f=geojson` + bbox `geometry` params per layer; some paginate.
- **Field-data join** — audit CSV needs a geo key (Segment ID → geometry / GPS pin); if missing,
  `ingest_field.py` needs a manual segment→line mapping step. Flag early.
- **Tile2Net on macOS/MPS** — arbitrary Esri XYZ source config may need work; time-boxed.

## 12. Deliverables

- `investigate/spatial/` scripts + `README.md` + `SCHEMA.md`.
- `data/pedestrian_network.geojson` (canonical, with `shade_modeled`), `data/gradient.csv`,
  route-demo output, **`*.pmtiles` + `*.gpkg`** (app-ready, engine-agnostic).
- A desk-research note + `DECISIONS.md` entry.
