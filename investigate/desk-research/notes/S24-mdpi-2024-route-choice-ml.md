# S24: Pedestrian route-choice behaviour via machine learning

> **S24 · METHOD (interpretable ML for route choice) · extends S16.** OA; exact figures to verify.

## Citation
*Exploring the Pedestrian Route Choice Behaviors by Machine Learning Models.* ISPRS International
Journal of Geo-Information (2024), 13(5), 146. MDPI. (Open access.)
- URL: https://www.mdpi.com/2220-9964/13/5/146
- Accessed: 2026-06-16 (MDPI fetch 403; details from search index, flag below)

## What it does
Models pedestrian route choice with **machine-learning models** and interprets them with **SHAP**
(SHapley Additive exPlanations) to rank which features drive the choice.

## Method to reuse
Where S16 used a binomial logit, we can fit **XGBoost / random forest** on revealed + stated data
plus CV-derived pathway features, and use **SHAP** to report feature importance honestly. Prior
work finds tree ensembles (XGBoost, LightGBM, random forest) strong for travel-mode/route choice.

## Why it matters for us
Gives an interpretable ML route to the question S16 left open ("add pathway characteristics; use a
richer model"). Interpretability (SHAP) matches our neutrality discipline: we report what the data
weights, not what we assumed.

## Flags
- Open access but fetch was blocked here; pull exact models, dataset, and performance from the full
  text before citing figures. Cross-reference the ML-mode-choice systematic review (ScienceDirect
  S2590123025041866) for method grounding.
