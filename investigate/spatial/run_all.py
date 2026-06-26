"""Fetch -> merge -> analyze -> route. Network-dependent; run manually, not in CI."""
from __future__ import annotations
import os
from . import fetch_osm, fetch_jakartasatu, ingest_field, merge, analyze_gradient
from .schema import edge_to_feature, node_to_feature, write_geojson
from .geo import BBOX

DATA = os.path.join(os.path.dirname(__file__), "data")
FIELD = os.path.join(os.path.dirname(__file__), "..", "field")


def main() -> None:
    os.makedirs(DATA, exist_ok=True)
    osm = fetch_osm.fetch_overpass(fetch_osm.build_query(BBOX))
    osm_edges, osm_nodes = fetch_osm.osm_to_edges(osm), fetch_osm.osm_to_nodes(osm)

    js_nodes = []
    try:
        gj = fetch_jakartasatu.fetch_geojson(fetch_jakartasatu.build_query_url("JPO_Bina_Marga"))
        js_nodes = fetch_jakartasatu.arcgis_points_to_nodes(gj, "jpo")
    except Exception as ex:                       # noqa: BLE001 - layer may 404; keep going
        print(f"[warn] Jakarta Satu JPO skipped: {ex}")

    seg_path = os.path.join(DATA, "segments.geojson")
    field_edges, field_nodes = ingest_field.ingest(
        FIELD, seg_path if os.path.exists(seg_path) else None)

    edges = merge.merge_edges(osm_edges, field_edges)
    nodes = merge.merge_nodes(osm_nodes, js_nodes, field_nodes)
    write_geojson(os.path.join(DATA, "pedestrian_network.geojson"),
                  [edge_to_feature(e) for e in edges] + [node_to_feature(n) for n in nodes])

    rows = analyze_gradient.gradient_by_street(edges)
    analyze_gradient.write_gradient_csv(rows, os.path.join(DATA, "gradient.csv"))
    print(f"[ok] {len(edges)} edges, {len(nodes)} nodes, {len(rows)} streets")


if __name__ == "__main__":
    main()
