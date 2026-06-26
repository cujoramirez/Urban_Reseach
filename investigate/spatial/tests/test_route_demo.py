from investigate.spatial.schema import Edge
from investigate.spatial.route_demo import (
    walkability_cost, build_graph, most_walkable_path, node_key, DEFAULT_WEIGHTS)


def test_missing_sidewalk_costs_more_than_present():
    good = Edge(id="g", geometry=[[0, 0], [0, 1]], has_sidewalk="yes", length_m=100.0)
    bad = Edge(id="b", geometry=[[0, 0], [0, 1]], has_sidewalk="no", length_m=100.0)
    assert walkability_cost(bad) > walkability_cost(good)


def test_walkable_path_avoids_gap_even_if_longer():
    # direct A->C has no sidewalk; detour A->B->C does. Detour should win.
    A, B, C = [0.0, 0.0], [0.0005, 0.0], [0.001, 0.0]
    edges = [
        Edge(id="AC", geometry=[A, C], has_sidewalk="no", length_m=111.0),
        Edge(id="AB", geometry=[A, B], has_sidewalk="yes", length_m=55.5),
        Edge(id="BC", geometry=[B, C], has_sidewalk="yes", length_m=55.5),
    ]
    g = build_graph(edges)
    path, cost = most_walkable_path(g, node_key(A), node_key(C))
    assert node_key(B) in path  # routed through the sidewalked detour


def test_shade_hour_penalizes_sun_exposed_edge():
    sunny = Edge(id="s", geometry=[[0, 0], [0, 1]], has_sidewalk="yes", length_m=100.0,
                 shade_modeled={"12": 0.0})
    shady = Edge(id="h", geometry=[[0, 0], [0, 1]], has_sidewalk="yes", length_m=100.0,
                 shade_modeled={"12": 1.0})
    assert walkability_cost(sunny, hour="12") > walkability_cost(shady, hour="12")
