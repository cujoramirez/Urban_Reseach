from __future__ import annotations
from typing import List, Dict
from dataclasses import fields
from .schema import Edge, Node, SOURCE_RANK

# "Absent" sentinels. NOTE: numeric 0 is intentionally NOT here — a 0 score
# (e.g. obstruction=0 "heavily blocked") is a real reading, not a missing value.
_EMPTY = (None, "", "unknown", "n-a", [])


def _meaningful(value) -> bool:
    return value not in _EMPTY


def _combine(high: Edge, low: Edge) -> Edge:
    for f in fields(Edge):
        if f.name in ("id", "geometry", "source", "confidence"):
            continue
        if not _meaningful(getattr(high, f.name)) and _meaningful(getattr(low, f.name)):
            setattr(high, f.name, getattr(low, f.name))
    return high


def merge_edges(*edge_lists: List[Edge]) -> List[Edge]:
    by_id: Dict[str, Edge] = {}
    for edges in edge_lists:
        for e in edges:
            cur = by_id.get(e.id)
            if cur is None:
                by_id[e.id] = e
            elif SOURCE_RANK[e.source] >= SOURCE_RANK[cur.source]:
                by_id[e.id] = _combine(e, cur)
            else:
                by_id[e.id] = _combine(cur, e)
    return list(by_id.values())


def merge_nodes(*node_lists: List[Node]) -> List[Node]:
    by_id: Dict[str, Node] = {}
    for nodes in node_lists:
        for n in nodes:
            cur = by_id.get(n.id)
            if cur is None or SOURCE_RANK[n.source] >= SOURCE_RANK[cur.source]:
                by_id[n.id] = n
    return list(by_id.values())
