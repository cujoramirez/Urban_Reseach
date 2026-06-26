from investigate.spatial.schema import Edge
from investigate.spatial.analyze_gradient import gradient_by_street


def test_gradient_computes_pct_and_means_per_street():
    edges = [
        Edge(id="1", geometry=[[0, 0], [0, 1]], street_name="Jl. Jenderal Sudirman",
             has_sidewalk="yes", width_m=2.4, shade=2, length_m=100.0),
        Edge(id="2", geometry=[[0, 0], [0, 1]], street_name="Jl. Jenderal Sudirman",
             has_sidewalk="yes", width_m=2.0, shade=1, length_m=100.0),
        Edge(id="3", geometry=[[0, 0], [0, 1]], street_name="Jl. Kendal",
             has_sidewalk="no", width_m=None, shade=0, length_m=100.0),
    ]
    rows = gradient_by_street(edges)
    sud = next(r for r in rows if r["street_name"] == "Jl. Jenderal Sudirman")
    ken = next(r for r in rows if r["street_name"] == "Jl. Kendal")
    assert sud["sidewalk_pct"] == 100.0 and sud["mean_width_m"] == 2.2 and sud["mean_shade"] == 1.5
    assert ken["sidewalk_pct"] == 0.0 and ken["mean_width_m"] is None
    assert rows[0]["sidewalk_pct"] >= rows[-1]["sidewalk_pct"]  # sorted desc
