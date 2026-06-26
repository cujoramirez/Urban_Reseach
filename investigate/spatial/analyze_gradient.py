from __future__ import annotations
from typing import List, Dict, Any, Optional
import csv
from .schema import Edge


def _mean(vals: List[float]) -> Optional[float]:
    vals = [v for v in vals if v is not None]
    return round(sum(vals) / len(vals), 4) if vals else None


def gradient_by_street(edges: List[Edge]) -> List[Dict[str, Any]]:
    groups: Dict[str, List[Edge]] = {}
    for e in edges:
        groups.setdefault(e.street_name or "(unnamed)", []).append(e)
    rows: List[Dict[str, Any]] = []
    for name, es in groups.items():
        total = sum(e.length_m for e in es)
        swlen = sum(e.length_m for e in es if e.has_sidewalk == "yes")
        rows.append({
            "street_name": name,
            "total_len_m": round(total, 1),
            "sidewalk_len_m": round(swlen, 1),
            "sidewalk_pct": round(100.0 * swlen / total, 1) if total else 0.0,
            "mean_width_m": _mean([e.width_m for e in es]),
            "mean_shade": _mean([float(e.shade) for e in es if e.shade is not None]),
        })
    rows.sort(key=lambda r: r["sidewalk_pct"], reverse=True)
    return rows


def write_gradient_csv(rows: List[Dict[str, Any]], path: str) -> None:
    cols = ["street_name", "total_len_m", "sidewalk_len_m", "sidewalk_pct",
            "mean_width_m", "mean_shade"]
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
