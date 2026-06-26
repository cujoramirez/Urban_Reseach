import json, os
from investigate.spatial.fetch_jakartasatu import (
    build_query_url, arcgis_points_to_nodes, SERVICES)

FIX = os.path.join(os.path.dirname(__file__), "fixtures", "arcgis_jpo.json")


def test_build_query_url_requests_geojson_and_bbox():
    url = build_query_url("JPO_Bina_Marga")
    assert "f=geojson" in url and "geometryType=esriGeometryEnvelope" in url
    assert "JPO_Bina_Marga" in url


def test_services_map_has_expected_layers():
    for key in ("JPO_Bina_Marga", "DBM_JALAN", "Penggunaan_Lahan", "NDVI_Jakarta_2022"):
        assert key in SERVICES


def test_points_to_nodes_clips_bbox_and_tags_jpo():
    with open(FIX) as fh:
        gj = json.load(fh)
    nodes = arcgis_points_to_nodes(gj, "jpo")
    assert len(nodes) == 1  # outside-bbox feature dropped
    assert nodes[0].type == "jpo" and nodes[0].level == 1 and nodes[0].source == "jakartasatu"
