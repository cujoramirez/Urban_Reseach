#!/usr/bin/env python3
"""
analyze.py — honest, dependency-free analysis of the walkability field data.

Stdlib only (no numpy/scipy/pandas) so it runs in any Python 3.7+ without installs.
For tiny samples it uses EXACT permutation / conditional tests, which are more
appropriate than a t-test here.

Golden rule (enforced in code): inferential tests run ONLY on MEASURED data, i.e.
rows where scale_source == "stated". Interpreted-from-transcript scores are
descriptive leads, never p-values. Override with --include-interpreted (prints a
loud warning) only for illustration.

Examples
--------
# Descriptive summary of a metric by group (uses measured rows only):
python3 analyze.py --csv data/respondents_2026-06-18.csv --metric comfort_1_10 --group class

# Compare two groups (Mann-Whitney U + exact permutation):
python3 analyze.py --csv data/respondents_2026-06-18.csv --metric heat_1_10 \
        --group class --groups upper_middle bottom

# Correlate two metrics (Spearman); great for comfort vs heat-index after Saturday:
python3 analyze.py --csv data/joined.csv --correlate feels_like_c comfort_1_10

# See the interpreted numbers anyway (illustration only, NOT a finding):
python3 analyze.py ... --include-interpreted
"""
import argparse, csv, math, statistics as st
from itertools import combinations


# ---------- io ----------
def read_rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def numeric(rows, metric, group_col=None, group_val=None, include_interpreted=False):
    """Pull floats for `metric`, optionally filtered to one group, honouring scale_source."""
    out = []
    for r in rows:
        v = (r.get(metric) or "").strip()
        if v == "":
            continue
        if group_col and (r.get(group_col, "").strip() != group_val):
            continue
        src = (r.get("scale_source") or "").strip().lower()
        if src and src != "stated" and not include_interpreted:
            continue
        try:
            out.append(float(v))
        except ValueError:
            continue
    return out


# ---------- stats primitives ----------
def rankdata(vals):
    """Average ranks with tie handling."""
    order = sorted(range(len(vals)), key=lambda i: vals[i])
    ranks = [0.0] * len(vals)
    i = 0
    while i < len(vals):
        j = i
        while j + 1 < len(vals) and vals[order[j + 1]] == vals[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0  # ranks are 1-based
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    return ranks


def _phi(z):
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def mann_whitney(x, y):
    """Return dict with U, p (exact if small else normal approx w/ tie corr), rank-biserial r."""
    n1, n2, N = len(x), len(y), len(x) + len(y)
    combined = x + y
    ranks = rankdata(combined)
    R1 = sum(ranks[:n1])
    U1 = R1 - n1 * (n1 + 1) / 2.0
    U2 = n1 * n2 - U1
    U = min(U1, U2)
    rrb = 1.0 - 2.0 * U1 / (n1 * n2)  # rank-biserial effect size (direction: x vs y)

    # exact conditional p via enumerating all splits of the rank vector (handles ties)
    if math.comb(N, n1) <= 200000:
        idx = list(range(N))
        obs = abs(U1 - n1 * n2 / 2.0)
        extreme = total = 0
        for combo in combinations(idx, n1):
            R = sum(ranks[i] for i in combo)
            u1 = R - n1 * (n1 + 1) / 2.0
            if abs(u1 - n1 * n2 / 2.0) >= obs - 1e-9:
                extreme += 1
            total += 1
        p = extreme / total
        method = "exact (conditional permutation)"
    else:
        # normal approximation with tie correction
        mu = n1 * n2 / 2.0
        # tie term
        from collections import Counter
        ties = Counter(combined)
        tie_sum = sum(t ** 3 - t for t in ties.values())
        sigma2 = (n1 * n2 / 12.0) * ((N + 1) - tie_sum / (N * (N - 1)))
        sigma = math.sqrt(sigma2) if sigma2 > 0 else float("nan")
        z = (abs(U1 - mu) - 0.5) / sigma  # continuity correction
        p = 2.0 * (1.0 - _phi(z))
        method = "normal approx (tie-corrected)"
    return {"U": U, "U1": U1, "p": p, "rank_biserial": rrb, "method": method}


def permutation_diff(x, y, n_perm=100000, statistic="mean"):
    """Two-sided permutation test on difference of means (or medians)."""
    f = st.mean if statistic == "mean" else st.median
    n1, N = len(x), len(x) + len(y)
    combined = x + y
    obs = f(x) - f(y)
    if math.comb(N, n1) <= n_perm:
        # exact: enumerate all splits
        idx = list(range(N))
        extreme = total = 0
        for combo in combinations(idx, n1):
            s = set(combo)
            gx = [combined[i] for i in idx if i in s]
            gy = [combined[i] for i in idx if i not in s]
            if abs(f(gx) - f(gy)) >= abs(obs) - 1e-9:
                extreme += 1
            total += 1
        return {"diff": obs, "p": extreme / total, "method": f"exact permutation ({total} splits)"}
    else:
        import random
        random.seed(42)
        extreme = 0
        for _ in range(n_perm):
            random.shuffle(combined)
            gx, gy = combined[:n1], combined[n1:]
            if abs(f(gx) - f(gy)) >= abs(obs) - 1e-9:
                extreme += 1
        return {"diff": obs, "p": (extreme + 1) / (n_perm + 1),
                "method": f"random permutation ({n_perm} draws)"}


def spearman(x, y):
    rx, ry = rankdata(x), rankdata(y)
    mx, my = st.mean(rx), st.mean(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = math.sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))
    rho = num / den if den else float("nan")
    n = len(x)
    # approximate two-sided p via t-distribution -> normal for simplicity
    if n > 3 and abs(rho) < 1:
        t = rho * math.sqrt((n - 2) / (1 - rho ** 2))
        p = 2.0 * (1.0 - _phi(abs(t)))
    else:
        p = float("nan")
    return {"rho": rho, "p_approx": p, "n": n}


# ---------- reporting ----------
def describe(name, v):
    if not v:
        print(f"  {name:<16} n=0  (no data)")
        return
    sd = st.pstdev(v) if len(v) > 1 else 0.0
    print(f"  {name:<16} n={len(v):<3} mean={st.mean(v):.2f}  median={st.median(v):.1f}  "
          f"sd={sd:.2f}  min={min(v):.0f}  max={max(v):.0f}")


def power_note(n1, n2):
    print(f"\n  ⚠️  POWER: n1={n1}, n2={n2}. Tiny samples detect only LARGE effects. "
          f"Report the effect size, treat p as provisional, and don't over-interpret.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--csv", required=True)
    ap.add_argument("--metric", help="numeric column to analyse, e.g. comfort_1_10")
    ap.add_argument("--group", help="grouping column, e.g. class")
    ap.add_argument("--groups", nargs=2, help="two group values to compare, e.g. upper_middle bottom")
    ap.add_argument("--correlate", nargs=2, metavar=("X", "Y"), help="two numeric columns for Spearman")
    ap.add_argument("--include-interpreted", action="store_true",
                    help="ILLUSTRATION ONLY: include scale_source!=stated rows (prints a warning)")
    ap.add_argument("--perm", type=int, default=100000, help="max permutations before sampling")
    args = ap.parse_args()

    rows = read_rows(args.csv)
    print(f"\n=== analyze.py — {args.csv} ({len(rows)} rows) ===")
    if args.include_interpreted:
        print("  🚨 --include-interpreted: results below MIX IN analyst-coded scores. "
              "These are NOT measurements. Do NOT cite p-values from this run as findings.\n")
    else:
        print("  Mode: MEASURED only (scale_source=='stated'). Interpreted rows excluded.\n")

    if args.correlate:
        xcol, ycol = args.correlate
        # pair rows that have both
        xs, ys = [], []
        for r in rows:
            xv, yv = (r.get(xcol) or "").strip(), (r.get(ycol) or "").strip()
            src = (r.get("scale_source") or "").strip().lower()
            if src and src != "stated" and not args.include_interpreted:
                continue
            try:
                xs.append(float(xv)); ys.append(float(yv))
            except ValueError:
                pass
        print(f"Spearman correlation: {xcol} vs {ycol}")
        if len(xs) < 4:
            print(f"  Not enough paired MEASURED rows (n={len(xs)}). Collect more (Saturday).")
            return
        r = spearman(xs, ys)
        print(f"  n={r['n']}  rho={r['rho']:.3f}  p≈{r['p_approx']:.3f}")
        power_note(len(xs), 0)
        return

    if not args.metric:
        ap.error("provide --metric (and optionally --group/--groups) or --correlate")

    if args.group:
        vals = sorted({(r.get(args.group) or "").strip() for r in rows if (r.get(args.group) or "").strip()})
        print(f"Descriptives for '{args.metric}' by '{args.group}':")
        for g in vals:
            describe(g, numeric(rows, args.metric, args.group, g, args.include_interpreted))
    else:
        print(f"Descriptives for '{args.metric}':")
        describe("all", numeric(rows, args.metric, include_interpreted=args.include_interpreted))

    if args.groups:
        ga, gb = args.groups
        x = numeric(rows, args.metric, args.group, ga, args.include_interpreted)
        y = numeric(rows, args.metric, args.group, gb, args.include_interpreted)
        print(f"\nComparison: {ga} (n={len(x)}) vs {gb} (n={len(y)})  —  metric: {args.metric}")
        if len(x) < 2 or len(y) < 2:
            print("  Not enough MEASURED data in one/both groups to test.")
            print("  → This is expected for Field Day 1 (scores were interpreted). Collect ASKED")
            print("    1–10 scales on Saturday, then re-run; the test will fire automatically.")
            return
        mw = mann_whitney(x, y)
        pm = permutation_diff(x, y, n_perm=args.perm)
        print(f"  Mann–Whitney U = {mw['U']:.1f}   p = {mw['p']:.4f}   [{mw['method']}]")
        print(f"     rank-biserial effect size r = {mw['rank_biserial']:+.3f}")
        print(f"  Permutation (Δmean = {pm['diff']:+.3f})   p = {pm['p']:.4f}   [{pm['method']}]")
        power_note(len(x), len(y))


if __name__ == "__main__":
    main()
