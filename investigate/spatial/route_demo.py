from __future__ import annotations
from typing import List, Tuple, Dict, Optional
import networkx as nx
from .schema import Edge

DEFAULT_WEIGHTS = {
    "no_sidewalk": 3.0, "narrow": 1.0, "damaged": 0.8,
    "obstruction": 0.5, "no_shade": 1.2, "unlit": 0.4,
}


def node_key(pt: List[float]) -> Tuple[float, float]:
    return (round(pt[0], 6), round(pt[1], 6))


def walkability_cost(edge: Edge, weights: Dict[str, float] = DEFAULT_WEIGHTS,
                     hour: Optional[str] = None) -> float:
    penalty = 0.0
    if edge.has_sidewalk == "no":
        penalty += weights["no_sidewalk"]
    if edge.width_m is not None and edge.width_m < 1.85:
        penalty += weights["narrow"]
    if edge.surface == "damaged":
        penalty += weights["damaged"]
    if edge.obstruction is not None:
        penalty += weights["obstruction"] * (2 - edge.obstruction) / 2.0
    if hour is not None and edge.shade_modeled is not None:
        shade = edge.shade_modeled.get(hour)
        if shade is not None:
            penalty += weights["no_shade"] * (1.0 - shade)
    if edge.lit == 0:
        penalty += weights["unlit"]
    return max(edge.length_m, 0.1) * (1.0 + penalty)


def build_graph(edges: List[Edge], weights: Dict[str, float] = DEFAULT_WEIGHTS,
                hour: Optional[str] = None) -> nx.Graph:
    g = nx.Graph()
    for e in edges:
        if len(e.geometry) < 2:
            continue
        u, v = node_key(e.geometry[0]), node_key(e.geometry[-1])
        w = walkability_cost(e, weights, hour)
        if not g.has_edge(u, v) or w < g[u][v]["weight"]:
            g.add_edge(u, v, weight=w, edge_id=e.id, length_m=e.length_m)
    return g


def most_walkable_path(g: nx.Graph, start: Tuple, end: Tuple) -> Tuple[List, float]:
    path = nx.shortest_path(g, start, end, weight="weight")
    cost = nx.shortest_path_length(g, start, end, weight="weight")
    return path, cost
