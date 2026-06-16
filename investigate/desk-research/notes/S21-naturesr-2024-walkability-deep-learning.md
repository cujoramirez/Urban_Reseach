# S21: Walkability assessment via big data + deep learning

> **S21 · METHOD (CV walkability from imagery) · Gading's CV core.** Verified (Sci Rep, OA).

## Citation
*Comprehensive walkability assessment of urban pedestrian environments using big data and deep
learning techniques.* Scientific Reports (2024), article s41598-024-78041-x, published 2024-11-06.
(Open access.)
- URL: https://www.nature.com/articles/s41598-024-78041-x
- Accessed: 2026-06-16 (HTML fetched via curl ✓; pull author list + exact figures from full text)

## What it does
Assesses walkability by combining **street view imagery** with **deep-learning semantic
segmentation** plus a **discrete choice model**, mixing subjective (perceived) and objective
(physical) evaluation. Cites DeepLab-based pixel segmentation of Google Street View to derive
street elements.

## Method to reuse
Segment street-view panoramas (DeepLab / PSPNet / ResNet-101, or modern SegFormer) into sidewalk,
greenery, sky, vehicles, etc., then convert pixel proportions into per-point walkability features
(greenery visibility, sidewalk share, barrier separation). Detection adds counts of facilities,
vehicles, pedestrians.

## Why it matters for us
Direct template for generating corridor streetscape features from imagery, the variable S16 said
should be modelled but never measured. Feeds the ML model (S24) and the comfort index.

## Flags
- Verified that the paper + method exist; exact accuracy figures and author list still to pull
  from the full text. Western/other-city imagery differs from Jakarta, so validate locally.
