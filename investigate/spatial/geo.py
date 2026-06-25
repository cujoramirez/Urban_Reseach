from __future__ import annotations
from typing import List, Tuple

BBOX: Tuple[float, float, float, float] = (106.808, -6.225, 106.827, -6.1925)  # W,S,E,N

NAMED_STREETS = {
    "jl. jenderal sudirman", "jl. jend. sudirman",
    "jl. karet tengsin", "jl. bendungan hilir", "benhil", "jl. gelora",
    "jl. kendal", "jl. blora", "jl. setiabudi", "jl. karet",
}


def in_bbox(pt: List[float], bbox=BBOX) -> bool:
    w, s, e, n = bbox
    return w <= pt[0] <= e and s <= pt[1] <= n


def line_in_bbox(coords: List[List[float]], bbox=BBOX) -> bool:
    return any(in_bbox(p, bbox) for p in coords)


def normalize_street(name: str) -> str:
    return (name or "").strip().lower()
