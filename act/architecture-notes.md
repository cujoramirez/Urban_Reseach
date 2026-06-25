# App Architecture Notes — Native iOS (provisional)

> ⏸️ **HELD, like [`solution-candidates.md`](solution-candidates.md).** This records a *technical
> direction* for the eventual app so we reason once and don't thrash later. It is **not** a
> commitment to build, and **nothing here belongs in the research report** (`report/*.tex` stays
> problem-level). The data leads; this follows. Revisit after fieldwork + synthesis validate the
> problem.

**Scope:** how the *eventual* pedestrian app would be built — **native, light, intuitive,
Apple-HIG-first.** Complements the *method* in
[`../investigate/desk-research/COMPUTATIONAL-DIRECTION.md`](../investigate/desk-research/COMPUTATIONAL-DIRECTION.md)
and the *data foundation* spec
[`../docs/superpowers/specs/2026-06-25-sudirman-pedestrian-network-design.md`](../docs/superpowers/specs/2026-06-25-sudirman-pedestrian-network-design.md).

## Guiding principle: separate the data layer from the render layer

- **Data layer** (this repo, `investigate/spatial/`) — a routable, accessibility- and
  shade-tagged pedestrian network. **Engine-agnostic** (GeoJSON / GeoPackage / `shade_modeled`).
- **Render/app layer** (separate iOS repo) — **native Apple frameworks**. Consumes the data
  files; computes almost nothing heavy at runtime.

Because the two are decoupled, the "Unity vs native" debate is moot: the data feeds either, and
we choose native for weight, battery, and HIG.

## Native stack (default direction)

| Concern | Native choice | Notes |
|---|---|---|
| **Map render** | **MapKit** | Apple's own → smallest binary, best HIG, free. Draw our sidewalk + shade as `MKOverlay`/`MKPolyline`. Mirrors Apple Maps' "Walk" UX (familiar = intuitive). *MapLibre only if we ever need to deeply restyle the basemap.* |
| **Routing** | On-device graph + A\* | Port the `route_demo.py` walkability cost to Swift; runs offline on the small corridor graph. (Valhalla/GraphHopper only if we outgrow the pilot.) |
| **Data store** | **GeoPackage / SQLite** on-device | Bundled for offline; produced by the spec's `export_app.py`. |
| **Sun position** | ~50 lines of pure Swift (NOAA algorithm) | No dependency, no API. Picks/interpolates the shade hour for "now." |
| **3D (if used)** | **RealityKit** (or SceneKit) | *Native replacement for Unity.* Metal-backed directional-light shadows; no third-party runtime. |
| **AR (later)** | **ARKit + RealityKit** | On-demand "see the shaded path ahead." v3 wow. |

## Shade, lightest-first (the feature that motivated "3D")

1. **Precomputed shade + overlays (v1, featherweight).** Offline pipeline writes `shade_modeled`
   per segment per hour → bundled in GeoPackage → app reads a number and tints the route. App
   does ~zero heavy compute. Most battery-friendly, most HIG.
2. **On-device geometric shadow projection** (Swift polygon math over building footprint+height
   along the sun vector) — dynamic at any minute, still light, **no 3D engine**.
3. **RealityKit real-time 3D shadows** — only for an immersive 3D view.
4. **ARKit shade preview** — later.

**We do not need a photoreal 3D model, and we do not need Unity, for shade.** Apple Maps has no
shade routing today — this is novel *and* fully native.

## Why native over Unity / MapLibre defaults

- **Weight/battery:** no Unity runtime (~tens of MB) or third-party GL renderer; precomputed
  data + MapKit is dramatically lighter.
- **HIG/intuitive:** standard SwiftUI controls, SF Symbols, a "**Prefer shade**" toggle and a
  time segmented-control that feel like Apple Maps.
- **Accessibility:** an *accessibility* app should inherit native VoiceOver / Dynamic Type —
  weaker in Unity-built UI. This matters for our exact users.

## Open dependencies (before any of this is real)

- Data foundation (spec Plan 1) and shade modeling (spec Plan 3) must exist and be **validated
  against the 06-18 field shade/heat data**.
- **Building heights** are the main shade-data gap (OSM + `levels×3 m` fallback).
- Every routing/shade signal must still trace back to a real finding in
  [`../investigate/synthesis.md`](../investigate/synthesis.md) — same rule as the candidate list.

— Tim Riset Pijak
