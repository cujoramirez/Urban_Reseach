# Computational Research Direction (data science / AI / CV / ML)

A candidate pathway that uses the team's own strengths: Gading (AI researcher, computer-vision
specialist) and Kenrich (robotics engineering). It turns the Sudirman walking study from a
manual audit into a **measurable, model-driven** investigation, and lines up a defensible iOS app.

> **Discipline.** This is a *candidate* method pathway, not a committed solution. The Friday
> refinement and the field data still lead (see `../engage/`, `SYNTHESIS.md`,
> `../../act/solution-candidates.md`). Every method below has a real source (S20-S24) and a
> ground-truth check against our own field audit.

> **Timeline.** 3 weeks research, then 3 weeks iOS build. The plan is scoped to a prototype, not
> a production system.

---

## The opening the literature leaves us
S16 (Afkara & Kusuma 2020) modelled walking-vs-ojol/BRT mode choice with discrete choice, and its
own future-work asks to *"consider the characteristics of the pedestrian pathway as a factor"* and
to *"use a multinomial / ML model."* It never measured the pathway itself. **Computer vision
closes that gap:** we can generate per-segment streetscape features (sidewalk presence, effective
width proxy, greenery, shade, obstructions) and feed them into a model, for the whole corridor
*and* the back-streets, at a scale manual audits cannot reach.

## Three method streams, each with a real anchor and a team owner

### 1. Measure the gradient automatically (CV on imagery) -- Gading
- **Tile2Net** (S23, open source, VIDA-NYU): semantic segmentation of aerial tiles into road /
  sidewalk / crosswalk / footpath, then polygons, then a routable centerline network. Run it over
  the Sudirman corridor and the back-streets to **quantify sidewalk presence/continuity, i.e. the
  gradient, with CV** and get a network to route on. Caveat: trained on US cities (Cambridge/DC/
  NYC), so Jakarta needs validation/fine-tuning, which is itself a research contribution.
- **Street-view segmentation** (S21 Nature SR 2024; S22 Project Sidewalk): segment Google Street
  View with DeepLab/SegFormer to derive greenery, sky, sidewalk share, obstructions, and a
  walkability index per point. Project Sidewalk also gives a ready labeling tool + label schema
  (curb ramps, obstacles, surface, missing sidewalk).

### 2. Comfort / heat layer (shade modelling) -- Gading + Kenrich
- **CoolWalks** (S20, Wolf, Vierø & Szell 2025, Sci Rep): compute shade from building footprints +
  heights + sun position, define a sun-avoidance parameter and a CoolWalkability metric, and route
  on a modified network. Jakarta's tropical heat (our weather dimension, S17 SVF) makes a
  **shade-aware comfort layer** the most defensible app feature.

### 3. Model behaviour and comfort (ML) -- Gading
- **ML route/mode choice** (S24 MDPI 2024; cf. S16): replace/extend the binomial logit with
  XGBoost / random forest + **SHAP** to learn what drives walking, using CV features + field data.
  SHAP keeps it interpretable, which matters for an honest report.

### Counting from video (CV) -- Kenrich (optional, robotics/vision)
- Pedestrian detection + counting on short corridor video clips to **automate the 5-minute
  counts** in the tally sheet, freeing the team to observe. Standard detector + tracker; ground-
  truth against a few hand counts.

---

## How CV outputs map to our existing instruments (ground truth keeps it honest)
| CV output | Our field check (ground truth) | Benchmark |
|-----------|-------------------------------|-----------|
| Tile2Net sidewalk presence/width | audit-sheet width measure | 1,85 m (S13) |
| Street-view obstruction/greenery share | audit encroachment + shade | S13; S1 |
| Shade map (CoolWalks) / SVF | on-site temp + shade tally | THI; S17 |
| Auto pedestrian counts | hand counts (5-min) | counts CSV |
| ML comfort/route model | intercept answers | S16 distances |

The rule from `CROSS-VALIDATION-FRAMEWORK.md` holds: where CV and field agree, the finding is
robust; where they disagree, that mismatch is the insight.

## A realistic 3-week research plan
- **Week 1.** Run field audits/intercepts (ground truth). Pull aerial tiles + Google Street View
  for the corridor and back-streets. Get Tile2Net running; first sidewalk-network draft.
- **Week 2.** Segment street view for streetscape features; build a per-segment feature table
  (CV + field). Compute a draft walkability/comfort index and a shade layer (CoolWalks-style).
- **Week 3.** Validate CV against the field audit; fit an interpretable model (XGBoost + SHAP);
  prototype shade/comfort-aware routing on the generated network. Write up for BAB IV.

## Then the iOS app (separate 3-week build, HELD until data confirms)
A **comfort-aware pedestrian navigation** prototype: route on the Tile2Net network, weight edges
by the shade/comfort layer (CoolWalks-style) and by sidewalk quality, with a heat/rain-aware
option. On-device CV (Core ML) is plausible given the team's background, but the feature set must
follow what the fieldwork shows matters. See `../../act/solution-candidates.md`.

## Honesty caveats
- Western-trained CV models need Jakarta validation; report accuracy against our own labels.
- Street-view imagery may be dated; note capture dates.
- A model is a hypothesis generator, not proof; corridor findings still come from data + ground
  truth, not from the model alone.
- Keep the neutrality discipline: do not let an elegant method pre-decide that the corridor is
  (un)comfortable.
