from investigate.spatial.schema import (
    Edge, Node, edge_to_feature, node_to_feature, features_to_collection,
    feature_to_edge, line_length_m, validate_edge, SOURCE_RANK,
)
import math, pytest


def test_edge_roundtrips_through_geojson_feature():
    e = Edge(id="SUD-N-03", geometry=[[106.82, -6.20], [106.82, -6.201]],
             street_name="Jl. Jenderal Sudirman", side="N/E", kind="sidewalk",
             has_sidewalk="yes", width_m=2.4, source="osm")
    f = edge_to_feature(e)
    assert f["type"] == "Feature"
    assert f["geometry"]["type"] == "LineString"
    assert f["geometry"]["coordinates"] == e.geometry
    assert f["properties"]["has_sidewalk"] == "yes"
    assert "geometry" not in f["properties"]
    back = feature_to_edge(f)
    assert back.id == "SUD-N-03" and back.width_m == 2.4 and back.kind == "sidewalk"


def test_node_to_feature_is_point():
    n = Node(id="jpo-1", geometry=[106.815, -6.218], type="jpo", level=1)
    f = node_to_feature(n)
    assert f["geometry"]["type"] == "Point"
    assert f["properties"]["type"] == "jpo" and f["properties"]["level"] == 1


def test_line_length_m_matches_haversine():
    # ~111 m north-south near the equator for 0.001 deg latitude
    d = line_length_m([[106.82, -6.20], [106.82, -6.201]])
    assert math.isclose(d, 111.0, abs_tol=2.0)


def test_features_to_collection_wraps_list():
    fc = features_to_collection([node_to_feature(Node(id="b1", geometry=[1.0, 2.0], type="bench"))])
    assert fc["type"] == "FeatureCollection" and len(fc["features"]) == 1


def test_validate_edge_rejects_unknown_kind_and_source():
    with pytest.raises(ValueError):
        validate_edge(Edge(id="x", geometry=[[0, 0], [0, 1]], kind="teleporter"))
    with pytest.raises(ValueError):
        validate_edge(Edge(id="x", geometry=[[0, 0], [0, 1]], source="vibes"))


def test_source_rank_orders_field_above_osm():
    assert SOURCE_RANK["field"] > SOURCE_RANK["osm"] > SOURCE_RANK["jakartasatu"] > SOURCE_RANK["tile2net"]
