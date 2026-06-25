import json, os
from investigate.spatial.fetch_osm import build_query, osm_to_edges, osm_to_nodes

FIX = os.path.join(os.path.dirname(__file__), "fixtures", "osm_sample.json")


def load():
    with open(FIX) as fh:
        return json.load(fh)


def test_build_query_contains_bbox_and_footway():
    q = build_query((106.808, -6.225, 106.827, -6.1925))
    assert "footway" in q and "-6.225" in q and "106.827" in q


def test_osm_to_edges_maps_sidewalk_and_crossing_and_clips_bbox():
    edges = osm_to_edges(load())
    # way 2 is outside bbox -> clipped out; only way 1 remains
    assert len(edges) == 1
    e = edges[0]
    assert e.kind == "sidewalk" and e.has_sidewalk == "yes"
    assert e.street_name == "Jl. Jenderal Sudirman"
    assert e.source == "osm" and e.length_m > 100
    assert e.id == "osm-way-1"


def test_osm_to_nodes_maps_bench():
    nodes = osm_to_nodes(load())
    assert len(nodes) == 1 and nodes[0].type == "bench" and nodes[0].source == "osm"
