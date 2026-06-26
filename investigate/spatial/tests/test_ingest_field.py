import csv, json, os
from investigate.spatial.ingest_field import (
    load_segments, audit_rows_to_edges, media_points_to_nodes)

HERE = os.path.dirname(__file__)
AUDIT = os.path.join(HERE, "fixtures", "audit_sample.csv")
SEGS = os.path.join(HERE, "fixtures", "segments_sample.geojson")


def test_load_segments_maps_id_to_coords():
    with open(SEGS) as fh:
        segs = load_segments(json.load(fh))
    assert segs["SUD-N-03"][0] == [106.820, -6.200]


def test_audit_rows_to_edges_attaches_attributes_for_known_segment_only():
    with open(SEGS) as fh:
        segs = load_segments(json.load(fh))
    with open(AUDIT) as fh:
        rows = list(csv.DictReader(fh))
    edges = audit_rows_to_edges(rows, segs)
    # KEN-S-01 has no geometry in segments -> dropped (no invented geometry)
    assert len(edges) == 1
    e = edges[0]
    assert e.id == "SUD-N-03" and e.source == "field" and e.confidence == "high"
    assert e.has_sidewalk == "yes" and e.width_m == 2.4 and e.shade == 1
    assert e.obstruction == 2


def test_media_points_to_nodes_reads_real_geojson_shape():
    gj = {"type": "FeatureCollection", "features": [
        {"type": "Feature", "geometry": {"type": "Point", "coordinates": [106.8226, -6.2021]},
         "properties": {"file": "IMG_0201.MOV", "type": "video", "time_wib": "2026-06-18T10:37:43"}}]}
    nodes = media_points_to_nodes(gj)
    assert len(nodes) == 1 and nodes[0].source == "field" and nodes[0].type == "barrier"
    assert "IMG_0201.MOV" in nodes[0].notes
