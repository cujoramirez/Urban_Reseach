# Pedestrian-network schema (authoritative)

OpenSidewalks-aligned, matched 1:1 to the field audit sheet
([`../field/instruments/audit-sheet.md`](../field/instruments/audit-sheet.md)). Output is
GeoJSON; every feature carries `source` + `confidence`. Defined in code at `schema.py`.

## Edge (LineString) — traversable pedestrian segment

| Field | Type | Notes / audit-sheet origin |
|---|---|---|
| `id` | string | e.g. `SUD-N-03` (audit Segment ID) |
| `street_name` | string | named street |
| `side` | enum | `N/E` \| `S/W` \| `n-a` |
| `kind` | enum | `sidewalk`\|`footway`\|`crossing`\|`jpo`\|`path`\|`road_shoulder` |
| `level` | int | `0` ground, `+1` overpass/JPO, `-1` underpass (vertical routing) |
| `has_sidewalk` | enum | `yes`\|`no`\|`unknown` (audit #1) |
| `width_m` | float\|null | effective width; std min **1.85 m** (audit #2) |
| `surface` | enum | `intact`\|`damaged`\|`unknown` (audit #3) |
| `obstruction` | 0–2\|null | clear→blocked (audit #4) |
| `obstruction_types` | list | motorbikes, vendors, poles, vegetation… (audit #4) |
| `kerb_ramp` | 0–2\|null | ramp/guiding-block; slope std **≤8% (1:12)** (audit #5) |
| `lit` | 0–2\|null | night lighting (audit #6) |
| `eyes_on_street` | 0–2\|null | crowd / passive surveillance (audit #7) |
| `crossing_spacing_m` | float\|null | std **100–200 m** (audit #8) |
| `shade` | 0–2\|null | field-observed shade; THI discomfort **>27 °C** (audit #9) |
| `shade_modeled` | dict\|null | computed shade fraction per hour, e.g. `{"09":0.8,"12":0.3}` (Plan 3) |
| `drainage` | 0–2\|null | open gutter→covered (audit #10) |
| `length_m` | float | computed (haversine) |
| `source` | enum | `field`\|`osm`\|`jakartasatu`\|`tile2net` |
| `confidence` | enum | `high`\|`med`\|`low` |
| `notes` | string | |

## Node (Point) — feature / barrier

`id`, `type` (`crossing_signalized`\|`crossing_zebra`\|`jpo`\|`curb_ramp`\|`tactile_paving`\|
`bench`\|`shelter`\|`toilet`\|`transit_mrt`\|`transit_tj`\|`barrier`\|`kerb`), `level` (int),
`accessible` (`yes`\|`no`\|`unknown`), `source`, `notes`.

## Provenance precedence

On disagreement: **field > osm > jakartasatu > tile2net**. A higher-rank source is the base;
lower-rank sources fill only genuine gaps. A meaningful `0` score (e.g. `obstruction=0`) is a
real reading and is never treated as missing.
