import os, json, re
import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
DASHBOARD_PATH = os.path.join(ROOT, "empirical_field_data_dashboard.html")
FIELD_DASHBOARD_PATH = os.path.join(ROOT, "investigate", "field", "empirical_field_data_dashboard.html")


def test_dashboard_files_exist():
    assert os.path.exists(DASHBOARD_PATH), f"Missing {DASHBOARD_PATH}"
    assert os.path.exists(FIELD_DASHBOARD_PATH), f"Missing {FIELD_DASHBOARD_PATH}"
    assert os.path.getsize(DASHBOARD_PATH) > 100_000, "Dashboard file is unexpectedly small"
    assert os.path.getsize(FIELD_DASHBOARD_PATH) > 100_000, "Field dashboard file is unexpectedly small"


def test_dashboard_embedded_data_integrity():
    with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    # Verify all payload markers exist
    for var, min_len in [
        ("RESPONDENTS", 24),
        ("MEDIA_POINTS", 105),
        ("WEATHER", 6),
        ("GRADIENT", 60),
        ("PLACES", 100),
    ]:
        match = re.search(r"const " + var + r" = (.*?);\n", html, re.DOTALL)
        assert match is not None, f"Variable {var} not found in HTML"
        data = json.loads(match.group(1))
        assert len(data) >= min_len, f"Expected at least {min_len} items for {var}, found {len(data)}"

    # Check network GeoJSON
    match = re.search(r"const PEDESTRIAN_NET = (.*?);\n", html, re.DOTALL)
    assert match is not None
    pnet = json.loads(match.group(1))
    assert pnet.get("type") == "FeatureCollection"
    assert len(pnet.get("features", [])) == 680


def test_respondents_demographic_profiles_completeness():
    with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
        html = f.read()
    match = re.search(r"const RESPONDENTS = (.*?);\n", html, re.DOTALL)
    assert match is not None
    respondents = json.loads(match.group(1))
    assert len(respondents) == 24

    for r in respondents:
        assert "gender" in r and r["gender"] in ["Male", "Female"], f"Missing or invalid gender in {r['id']}"
        assert "age_bracket" in r and len(r["age_bracket"]) > 0, f"Missing age_bracket in {r['id']}"
        assert "age_group" in r and len(r["age_group"]) > 0, f"Missing age_group in {r['id']}"
        assert "mobility_mode" in r, f"Missing mobility_mode in {r['id']}"


def test_basemap_clean_and_unwatermarked():
    with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    # Carto voyager requires API keys and renders watermarks; verify clean OSM / Esri tiles are used
    assert "rastertiles/voyager" not in html, "Found deprecated watermarked Carto voyager tile endpoint"
    assert "tile.openstreetmap.org" in html, "Missing clean OpenStreetMap tile layer"


def test_media_thumbnails_exist_for_documented_assets():
    with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
        html = f.read()
    match = re.search(r"const MEDIA_POINTS = (.*?);\n", html, re.DOTALL)
    media = json.loads(match.group(1))
    
    thumb_count = sum(1 for m in media if m.get("has_thumb"))
    assert thumb_count == 84, f"Expected 84 thumbnails from Documentations/, found {thumb_count}"

    for m in media:
        if m.get("has_thumb"):
            local_rel = m["thumb_url"].lstrip("./")
            abs_path = os.path.join(ROOT, local_rel)
            assert os.path.exists(abs_path), f"Thumbnail does not exist: {abs_path}"

            # Verify subfolder resolution: in investigate/field/, Documentations/thumbnails exists
            field_dir = os.path.join(ROOT, "investigate", "field")
            field_thumb_path = os.path.join(field_dir, local_rel)
            assert os.path.exists(field_thumb_path), f"Thumbnail unresolved in investigate/field: {field_thumb_path}"


def test_gallery_filter_function_defined():
    with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    assert "function filterGallery" in html, "filterGallery function not defined"
    assert "filterGallery('all', this)" in html, "Missing filterGallery onclick handler"
