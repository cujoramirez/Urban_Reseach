# S23: Tile2Net, automated sidewalk-network mapping from aerial imagery

> **S23 · METHOD/TOOL (CV gradient measurement + routable network) · the standout for the
> gradient.** Open source; method verified (GitHub + paper).

## Citation
Hosseini, M., et al. (2023). *Mapping the walk: A scalable computer vision approach for generating
sidewalk network datasets from aerial imagery.* Computers, Environment and Urban Systems, 101,
101950. https://doi.org/10.1016/j.compenvurbsys.2023.101950
Code (open source): https://github.com/VIDA-NYU/tile2net
- Accessed: 2026-06-16 (paper + repo confirmed ✓)

## What it does
End-to-end open-source tool. **Semantic segmentation** of orthorectified aerial tiles into
**road / sidewalk / crosswalk / footpath**, converts results to geo-referenced polygons, then
generates a **topologically connected centerline network** (WGS 84 / Web Mercator). Model trained
on Cambridge MA, Washington DC, and New York City; public weights.

## Why it matters for us (high)
1. **Measures the gradient with CV:** sidewalk presence and continuity for the main corridor *and*
   the back-streets, at a scale manual audits cannot reach (fills gap G1 quantitatively).
2. **Outputs a routable network** that a comfort/shade-aware routing prototype (S20) can run on,
   and that an iOS app could consume.

## Why it fits the team
Gading can run/validate/fine-tune the segmentation; the output is standard GIS the app can use.

## Flags
- Trained on US cities; **Jakarta validation/fine-tuning required** (different roofs, tree cover,
  informal layouts). Reporting Jakarta accuracy against our field audit is a genuine contribution.
- Needs sub-meter aerial tiles for Jakarta; check source/licence.
