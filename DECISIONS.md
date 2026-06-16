# Decision Log

**Append-only.** Add new decisions at the bottom. Never rewrite or delete past entries —
if a decision changes, add a *new* entry that supersedes the old one and note which one it
replaces. This is our shared memory of *why* the project is the way it is.

## Format

```
### YYYY-MM-DD — Short title
- **Decision:** What we decided.
- **Reasoning:** Why. What problem it solves or what it rules out.
- **Owner:** Who is accountable for it.
```

| Date | Decision | Reasoning | Owner |
|------|----------|-----------|-------|
| _example_ | _what we chose_ | _why_ | _name_ |

---

### 2026-06-15 — Scope narrowed to the Sudirman corridor (named streets only)
- **Decision:** Scope is the **Sudirman corridor and its immediate back-streets**, referenced
  by **named streets only**. We dropped the earlier framing of "Jakarta Selatan" and the
  list of five station names.
- **Reasoning:** Mentor flagged "Jakarta Selatan" as far too broad to study meaningfully in
  the time we have, and a list of stations scatters our attention. The interesting, studyable
  phenomenon is the **contrast** between the wide, proper Sudirman trotoar and the
  near-nonexistent sidewalks one block behind it — the "gradient." A tight, named-street
  scope lets us actually observe both ends of that contrast.
- **Owner:** Team (scope agreed with mentor Kak Will Chris).

### 2026-06-15 — Mentoring outcome: fix confirmation bias in our method
- **Decision:** Overhaul how we ask questions and handle assumptions:
  1. **Split biased guiding questions into neutral, two-sided pairs.** Example: the leading
     "where do pedestrians walk in the road *despite* a good sidewalk" becomes (1) "How do
     pedestrians move through the Sudirman area?" and (2) "Do pedestrians use the sidewalks
     provided?"
  2. **Make assumptions explicit** in their own file (`engage/assumptions.md`) and keep them
     **out** of the guiding questions.
  3. **Add a comfort-factor question** — "what makes walking feel comfortable?" — which we
     had wrongly omitted by assuming discomfort up front.
  4. **Reframe the expert interview around obstacles.** The interview with the former Jakarta
     governor (who ran the 2017–2022 sidewalk program) exists to surface the **obstacles that
     blocked comfortable pedestrian facilities**, not vague "cross-validation."
- **Reasoning:** Mentor flagged heavy confirmation bias — our questions pre-loaded the
  conclusion we wanted. Neutral, two-sided questions and explicit assumptions keep the
  fieldwork honest and let the data surprise us.
- **Owner:** Team.

### 2026-06-16 — Seeded initial desk research (Jakarta/Sudirman) + literature-informed interview bank
- **Decision:** Added an **initial set of six peer-reviewed, open-access sources** to
  `investigate/desk-research/` (one Markdown file each, following the existing template), all
  focused on the **Jakarta / Sudirman corridor**: Mulyadi et al. (2022, Sudirman–Thamrin
  walkability), Apritasari (2020, Thamrin–Sudirman user satisfaction), Afkara & Kusuma (2020,
  MRT walking-distance perception), Arif & Yola (2021, Jakarta sidewalk thermal comfort),
  Putri & Ellisa (2020, informal use of pedestrian space), Napitupulu & Rudiarto (2025, Dukuh
  Atas TOD walkability). Their BibTeX is in `report/refs.bib`. Also added a **literature-informed,
  neutral pedestrian interview bank** at `investigate/field/instruments/pedestrian-interview-bank.md`.
- **Reasoning:** Builds the *pre-knowledge* (for BAB II — Tinjauan Pustaka) **before** fieldwork,
  so our intercept questions are informed by what prior Jakarta studies found mattered — without
  importing their conclusions. The interview bank stays **neutral and two-sided** to preserve the
  confirmation-bias fix above; it **complements** `intercept-script.md` and `guiding-questions.md`,
  it does not replace them.
- **To validate (team):** confirm each source's findings against the full text; check Indonesian
  author-name order in `refs.bib`; agree final intercept wording. These were **seeded for review**,
  not locked. No field data was invented; `synthesis.md` and `act/` remain untouched.
- **Owner:** Team (to review/extend).
