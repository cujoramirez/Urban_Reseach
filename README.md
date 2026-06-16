# Urban Research: Sudirman Walking Experience

**Apple Developer Academy @ BINUS, Cohort 9**
**Urban Innovation Challenge (Challenge 4) · Challenge Based Learning (CBL)**
**Big Idea: "Urban Living Experience"**

> **This is a TEAM project. Decisions and agreement come from the group, not any single member.**

---

## What this repository is

This is our **research workspace**: field notes, reports, instruments, and progress
tracking. There is **no app code here**, the eventual deliverable is a native iOS app,
but that lives in a separate repository. This repo is for the *thinking and the evidence*
that the app will be built on.

Written for everyone on the team, technical or not. If you can read Markdown and open a
folder, you can use this.

---

## The CBL framing

Challenge Based Learning moves through three stages. Our folders mirror them:

| Stage | Folder | What lives here |
|-------|--------|-----------------|
| **Engage** | [`engage/`](engage/) | The challenge statement, our explicit assumptions, and neutral guiding questions. |
| **Investigate** | [`investigate/`](investigate/) | Desk research, field instruments, raw data, and (later) synthesis. |
| **Act** | [`act/`](act/) | Solution candidates, held until the data tells us what to build. |

Reporting lives in [`report/`](report/) (LaTeX, written for Overleaf).

---

## LOCKED scope

**The Sudirman corridor and its immediate back-streets, referenced by named streets only.**

- ✅ The main Sudirman trotoar (wide, proper sidewalk) **and** the near-nonexistent
  sidewalks one block behind it. The *contrast* between these two, the "gradient", is
  the core of our research.
- ❌ **NOT** "Jakarta Selatan" (too broad, explicitly rejected by our mentor).
- ❌ **NOT** a long list of station names.

Always describe locations by **named streets**, not districts or stations.

See [`DECISIONS.md`](DECISIONS.md) for the full reasoning behind this scope.

---

## How to navigate this repo

```
Urban_Research/
├── README.md            ← you are here
├── DECISIONS.md         ← append-only log of every decision we make + why
├── engage/              ← Stage 1: framing the problem
│   ├── challenge-statement.md
│   ├── assumptions.md
│   └── guiding-questions.md
├── investigate/         ← Stage 2: gathering evidence
│   ├── desk-research/   ← one file per source (feeds the literature review)
│   ├── field/           ← instruments, raw data, photos, transcripts
│   └── synthesis.md     ← (kept empty until after fieldwork)
├── act/                 ← Stage 3: what we decide to build
│   └── solution-candidates.md
└── report/              ← LaTeX report (Overleaf)
    ├── main_id.tex      ← Bahasa Indonesia, report class (BAB I-IV)
    ├── main_en.tex      ← English, IEEE conference template
    └── refs.bib         ← shared bibliography
```

---

## Team

Internal working group. **(Fill in your own roles below.)**

| Member | Role | Notes |
|--------|------|-------|
| Gading Aditya Perdana | | |
| Kenrich Heavenly Sandria | | |
| Naufal Ammar Rauf | | |
| Jatayu Muhammad Wicaksono | | |
| Sintani Gina Lestari | | |

**Mentor:** Kak Will Chris

> Internal nickname: "William Cupertino", an inside joke, **not** for external use.
> A formal external name is still being decided (working candidate: *Tim Pijak*).

---

## Ground rules for this repo

1. **No invented data.** Placeholders stay placeholders until real fieldwork fills them.
2. **Keep guiding questions neutral.** Assumptions go in `assumptions.md`, never inside questions.
3. **Log decisions** in `DECISIONS.md` as you make them.
4. **Don't commit large photos** to git, see [`investigate/field/photos/README.md`](investigate/field/photos/README.md).
