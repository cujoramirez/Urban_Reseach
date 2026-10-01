#!/usr/bin/env python3
"""
build_prototype.py
Compiles the comprehensive, production-grade Pijak Transit Accessibility Prototype.
Apple Developer Academy @ BINUS research prototype.
"""

import json, csv, math, os
import prototype_data
import prototype_template

base_dir = '/Users/gading/Documents/Urban_Research'
output_path = os.path.join(base_dir, 'transit_accessibility_prototype.html')

print("Loading spatial data files...")

# 1. Dukuh Atas Facilities GeoJSON
with open(os.path.join(base_dir, 'investigate/spatial/data/dukuh_atas_facilities.geojson'), 'r', encoding='utf-8') as f:
    facilities_data = json.load(f)

# 2. Gradient Data CSV
gradient_rows = []
with open(os.path.join(base_dir, 'investigate/spatial/data/gradient.csv'), 'r', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        gradient_rows.append(row)

# 3. Places Data CSV
places_rows = []
with open(os.path.join(base_dir, 'investigate/spatial/data/dukuh_atas_places.csv'), 'r', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        places_rows.append(row)

print(f"Loaded: {len(facilities_data['features'])} facilities, {len(gradient_rows)} gradient rows, {len(places_rows)} places.")
print(f"Loaded presets: {len(prototype_data.PRESETS_DATA)} commute scenarios, {len(prototype_data.STATIONS_DATA)} stations, {len(prototype_data.BUILDINGS_DATA)} buildings.")

# Assemble HTML
html = prototype_template.HTML_TEMPLATE
html = html.replace('__FACILITIES_JSON__', json.dumps(facilities_data, separators=(',', ':')))
html = html.replace('__GRADIENT_JSON__', json.dumps(gradient_rows, separators=(',', ':')))
html = html.replace('__PLACES_JSON__', json.dumps(places_rows, separators=(',', ':')))
html = html.replace('__STATIONS_JSON__', json.dumps(prototype_data.STATIONS_DATA, separators=(',', ':')))
html = html.replace('__BUILDINGS_JSON__', json.dumps(prototype_data.BUILDINGS_DATA, separators=(',', ':')))
html = html.replace('__PRESETS_JSON__', json.dumps(prototype_data.PRESETS_DATA, separators=(',', ':')))

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

file_size_kb = os.path.getsize(output_path) / 1024
print(f"Generated {output_path} successfully ({file_size_kb:.1f} KB)!")
