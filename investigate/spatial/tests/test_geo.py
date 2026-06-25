from investigate.spatial.geo import in_bbox, line_in_bbox, normalize_street, NAMED_STREETS, BBOX


def test_in_bbox_true_for_corridor_point():
    assert in_bbox([106.820, -6.205]) is True


def test_in_bbox_false_outside():
    assert in_bbox([106.700, -6.300]) is False


def test_line_in_bbox_true_if_any_vertex_inside():
    assert line_in_bbox([[106.700, -6.300], [106.820, -6.205]]) is True


def test_normalize_street_lowercases_and_strips():
    assert normalize_street("  Jl. Jenderal SUDIRMAN ") == "jl. jenderal sudirman"


def test_named_streets_includes_sudirman_and_a_backstreet():
    assert "jl. jenderal sudirman" in NAMED_STREETS
    assert any("benhil" in s or "bendungan hilir" in s for s in NAMED_STREETS)
