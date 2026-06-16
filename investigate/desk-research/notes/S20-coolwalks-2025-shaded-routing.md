# S20: CoolWalks, shaded routing for active mobility

> **S20 · METHOD (shade-aware routing) · the app-concept anchor.** Verified (arXiv + Sci Rep, OA).

## Citation
Wolf, H., Vierø, A. R., & Szell, M. (2025). *CoolWalks for active mobility in urban street
networks.* Scientific Reports, 15, 14911. arXiv:2405.01225. (Open access.)
- URL: https://arxiv.org/abs/2405.01225 · https://www.nature.com/articles/s41598-025-97200-2
- Accessed: 2026-06-16 (abstract/HTML fetched ✓)

## What it does
Adds shade preference to pedestrian routing. Defines a **sun-avoidance parameter (α)** for how
strongly a walker prefers shade, and a **CoolWalkability** metric for how much shade a network
offers. Inputs: **building footprints, street-network geometry, building heights, sun position**.
Routes on a shade-weighted network.

## Key findings (exact/close)
- On a regular grid with uniform building heights, "CoolWalkability is independent of α" and gives
  no benefit over the shortest path.
- Variation in street geometry and building height creates shade-routing benefit; benefit forms
  concentrated zones and differs between grid-like and irregular networks.
- Results are sensitive to mapped-network precision.

## Why it matters for us
The defensible heat feature for a Jakarta walking app. Pairs with our weather dimension (S17 SVF;
THI threshold) and the shade audit. We can build a shade layer from building footprints + heights
and weight routes by it.

## Flags
- Method/concept verified; we would compute shade for Sudirman ourselves (needs building-height
  data). Validate the shade map against on-site observation.
