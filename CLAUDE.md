# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A **research workspace**, not an application. It holds the field notes, desk research,
instruments, decisions, and LaTeX reports for an urban-walkability study of the **Sudirman
corridor, Jakarta**. The eventual deliverable is a native iOS app that lives in a *separate*
repo; nothing here is app code. Treat this repo as evidence and reasoning.

There is no build/lint/test pipeline. The only executable tooling is a Python venv used to
extract text from source PDFs.

## Structure follows the CBL stages

- `engage/` — challenge statement, explicit `assumptions.md`, neutral `guiding-questions.md`, and the expert-outreach `proposal/`.
- `investigate/desk-research/` — one Markdown note per source under `notes/` (named `S<n>-...`), aggregated by `SOURCE-INVENTORY.md`, `SYNTHESIS.md`, `CROSS-VALIDATION-FRAMEWORK.md`. Source PDFs live in `sources/` (gitignored — local only).
- `investigate/field/` — `instruments/` (audit sheet, observation tally, intercept/interview scripts), plus `data/`, `photos/`, `transcripts/` (raw outputs, mostly gitignored, kept as `.gitkeep` + README placeholders).
- `act/solution-candidates.md` — held until the data says what to build.
- `report/` — LaTeX (compiled on Overleaf).
- `DECISIONS.md` — append-only decision log.

## Reports (`report/`)

- `main_id.tex` — Bahasa Indonesia, `report` class (BAB I–IV). Primary report.
- `main_en.tex` — English, IEEE conference template. Companion; keep it at least as detailed as `main_id.tex`.
- `refs.bib` — shared bibliography for both.
- Compiled on **Overleaf with pdfLaTeX + Biber** (biblatex). No local build is expected; `report/*.pdf` is gitignored.
- **Gotcha:** babel option must be `indonesian`, never `bahasa` (the latter errors on modern babel).
- Citation keys in `refs.bib` correspond to the `S<n>` desk-research notes — when adding a source, add the note, the inventory entry, and the BibTeX entry together (see the 2026-06-16 merge entry in `DECISIONS.md`).

## PDF text extraction

```bash
source .venv/bin/activate          # Python 3.9 venv, pdfplumber + pdfminer.six
pdf2txt.py investigate/desk-research/sources/<file>.pdf
```

## Working conventions (from README + DECISIONS, enforce these)

- **Locked scope:** the Sudirman corridor *and its immediate back-streets*, referenced by **named streets only**. The research subject is the *contrast* (the "gradient") between the wide Sudirman trotoar and the near-nonexistent sidewalks one block behind. NOT "Jakarta Selatan", NOT a list of station names.
- **No invented data.** Placeholders stay placeholders until real fieldwork fills them. This is a research-stage project — no field findings appear in either report until data is collected.
- **Guard against confirmation bias.** Keep guiding questions neutral and two-sided; assumptions go in `engage/assumptions.md`, never embedded in questions. A specific leading framing ("walk in the road *despite* a good sidewalk" / "*meskipun*…") was flagged by the mentor and keeps creeping back — actively reject it.
- **`DECISIONS.md` is append-only.** Add new dated entries at the bottom; supersede rather than rewrite.
- **This is a team project.** Frame outputs as group decisions, not individual ones.
- **Branding:** present this as independent team research ("Tim Riset Pijak"); keep Apple Developer Academy branding minimal. The team owns the IP.
