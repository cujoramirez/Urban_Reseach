from investigate.spatial.schema import Edge, Node
from investigate.spatial.merge import merge_edges, merge_nodes


def test_merge_edges_field_overrides_osm_for_same_id():
    osm = Edge(id="SUD-N-03", geometry=[[0, 0], [0, 1]], kind="sidewalk",
               has_sidewalk="unknown", width_m=None, source="osm")
    field = Edge(id="SUD-N-03", geometry=[[0, 0], [0, 1]], kind="sidewalk",
                 has_sidewalk="yes", width_m=2.4, shade=1, source="field", confidence="high")
    merged = merge_edges([osm], [field])
    assert len(merged) == 1
    m = merged[0]
    assert m.source == "field" and m.has_sidewalk == "yes" and m.width_m == 2.4 and m.shade == 1


def test_merge_edges_lower_rank_fills_gaps_only():
    osm = Edge(id="A", geometry=[[0, 0], [0, 1]], width_m=3.0, source="osm")
    field = Edge(id="A", geometry=[[0, 0], [0, 1]], width_m=None, shade=2, source="field")
    m = merge_edges([osm], [field])[0]
    assert m.shade == 2 and m.width_m == 3.0  # osm width fills field's gap


def test_merge_edges_keeps_distinct_ids():
    a = Edge(id="A", geometry=[[0, 0], [0, 1]], source="osm")
    b = Edge(id="B", geometry=[[1, 1], [1, 2]], source="osm")
    assert len(merge_edges([a, b])) == 2


def test_merge_nodes_dedupes_by_id_keeping_higher_rank():
    n_osm = Node(id="n1", geometry=[0, 0], type="bench", source="osm")
    n_field = Node(id="n1", geometry=[0, 0], type="bench", accessible="yes", source="field")
    out = merge_nodes([n_osm], [n_field])
    assert len(out) == 1 and out[0].source == "field" and out[0].accessible == "yes"


def test_merge_keeps_higher_rank_zero_score_over_lower_rank_value():
    # obstruction=0 means "heavily blocked" -> a meaningful field reading, not "missing".
    field = Edge(id="A", geometry=[[0, 0], [0, 1]], obstruction=0, source="field")
    osm = Edge(id="A", geometry=[[0, 0], [0, 1]], obstruction=2, source="osm")
    m = merge_edges([osm], [field])[0]
    assert m.obstruction == 0  # field's 0 must not be overwritten by osm's 2
