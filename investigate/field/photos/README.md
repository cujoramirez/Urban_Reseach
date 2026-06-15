# Field Photos

Photo evidence from the field.

## ⚠️ Do NOT commit raw / large images to git

Raw `HEIC` and large `JPEG`/`PNG` files permanently bloat the repository — once committed,
they stay in git history forever. Instead:

- **Preferred:** keep photos in **external/shared storage** (e.g. the team Google Drive) and
  **link** to them from your notes and from the audit sheet's *photo reference* field.
- **Or:** use **[Git LFS](https://git-lfs.com)** if we decide to version images.

The repo's `.gitignore` already excludes common image formats here. Only this `README.md` and
`.gitkeep` are tracked.

## Privacy

- **Blur faces** in any close-up where individuals are identifiable.
- Avoid capturing identifiable people unnecessarily; we're documenting the *environment*.
- Don't photograph anything sensitive (vehicle plates close-up, private property interiors).

## Naming (for the external store)

Use the segment ID and date, e.g. `SUD-N-03_2026-06-19_01.jpg`, so photos map back to audits.
