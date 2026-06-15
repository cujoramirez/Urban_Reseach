# Field Data (CSV)

Raw, structured field data. Keep it as **CSV** so anyone can open it in Numbers, Excel, or a
script. **No invented rows** — only real observations go here.

## Conventions

- **One row per observation.** Don't merge multiple observations into one cell.
- **Segment IDs** match the audit sheet, e.g. `SUD-N-03`.
- **Timestamps** in ISO 8601: `2026-06-19T14:30`.
- Leave a cell blank if unknown; don't guess.
- Free text goes in the `notes` column only.
- Keep one file per session/day, named e.g. `counts_2026-06-19.csv`, `audit_2026-06-19.csv`.

## Counts CSV — sample header row

```csv
segment_id,timestamp,pedestrians_on_sidewalk,pedestrians_on_road,est_gender_split,ojol_pickups_under_300m,notes
```

| Column | Meaning |
|--------|---------|
| `segment_id` | Segment being observed (matches audit sheet) |
| `timestamp` | ISO 8601 date+time of the count window |
| `pedestrians_on_sidewalk` | Count walking on the sidewalk during the window |
| `pedestrians_on_road` | Count walking in the road during the window |
| `est_gender_split` | Rough estimate, e.g. `60M/40F` (observed, not asked) |
| `ojol_pickups_under_300m` | Ride-hailing pickups observed within ~300 m |
| `notes` | Anything notable (weather, event, obstruction, etc.) |

## Audit CSV — sample header row

Mirrors the [audit sheet](../instruments/audit-sheet.md); each parameter scored 0–2.

```csv
segment_id,named_street,side,date,auditor,gps_lat,gps_long,photo_ref,day_or_night,sidewalk_present,effective_width_ge_1_5m,surface_intact,obstruction,obstruction_type,kerb_guiding_block,lighting,crowd_eyes_on_street,crossing_within_200m,shade,drainage_open_gutter,total_score,notes
```

> Define a count **window** length (e.g. 5 minutes) and keep it consistent so counts are
> comparable across segments.
