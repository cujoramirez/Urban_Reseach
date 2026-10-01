import json, csv, math, os

base_dir = '/Users/gading/Documents/Urban_Research'
output_path = os.path.join(base_dir, 'transit_accessibility_prototype.html')

print("Loading data files...")

# 1. Dukuh Atas Facilities
with open(os.path.join(base_dir, 'investigate/spatial/data/dukuh_atas_facilities.geojson'), 'r', encoding='utf-8') as f:
    facilities_data = json.load(f)

# 2. Gradient Data
gradient_rows = []
with open(os.path.join(base_dir, 'investigate/spatial/data/gradient.csv'), 'r', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        gradient_rows.append(row)

# 3. Places Data
places_rows = []
with open(os.path.join(base_dir, 'investigate/spatial/data/dukuh_atas_places.csv'), 'r', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        places_rows.append(row)

# 4. Pedestrian Network
with open(os.path.join(base_dir, 'investigate/spatial/data/pedestrian_network.geojson'), 'r', encoding='utf-8') as f:
    ped_network_data = json.load(f)

print(f"Loaded: {len(facilities_data['features'])} facilities, {len(gradient_rows)} gradient rows, {len(places_rows)} places, {len(ped_network_data['features'])} ped network features.")

# Build HTML template
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>Pijak Transit Accessibility Engine | Multimodal 4-Pillar Router & Spatial Microclimate Prototype</title>
  
  <!-- Leaflet CSS & JS -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
  
  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>
  
  <style>
    :root {
      --apple-bg: #0b0f19;
      --apple-surface: #111827;
      --apple-card: rgba(17, 24, 39, 0.78);
      --apple-card-hover: rgba(30, 41, 59, 0.88);
      --apple-border: rgba(255, 255, 255, 0.09);
      --apple-border-active: rgba(56, 189, 248, 0.45);
      
      --text-primary: #f8fafc;
      --text-secondary: #94a3b8;
      --text-muted: #64748b;
      
      --accent-blue: #0071e3;
      --accent-blue-light: #38bdf8;
      --accent-teal: #0d9488;
      --accent-teal-light: #2dd4bf;
      --accent-green: #34c759;
      --accent-green-light: #10b981;
      --accent-amber: #ff9500;
      --accent-amber-light: #fbbf24;
      --accent-red: #ff3b30;
      --accent-red-light: #f43f5e;
      --accent-purple: #af52de;
      --accent-purple-light: #c084fc;
      
      --font-stack: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Helvetica Neue", Arial, sans-serif;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    body {
      background-color: var(--apple-bg);
      color: var(--text-primary);
      font-family: var(--font-stack);
      height: 100vh;
      width: 100vw;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }

    /* Top Apple Header / Microclimate HUD */
    header.apple-header {
      height: 64px;
      min-height: 64px;
      background: rgba(11, 15, 25, 0.88);
      backdrop-filter: blur(20px) saturate(180%);
      -webkit-backdrop-filter: blur(20px) saturate(180%);
      border-bottom: 1px solid var(--apple-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 20px;
      z-index: 1000;
    }

    .brand-section {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .brand-logo-badge {
      width: 38px;
      height: 38px;
      border-radius: 10px;
      background: linear-gradient(135deg, #0284c7 0%, #0d9488 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 14px rgba(13, 148, 136, 0.35);
      color: #fff;
    }

    .brand-titles {
      display: flex;
      flex-direction: column;
    }

    .brand-title {
      font-size: 15px;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .brand-tag {
      font-size: 10px;
      font-weight: 600;
      padding: 2px 7px;
      border-radius: 999px;
      background: rgba(56, 189, 248, 0.15);
      color: var(--accent-blue-light);
      border: 1px solid rgba(56, 189, 248, 0.3);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .brand-subtitle {
      font-size: 11.5px;
      color: var(--text-secondary);
      font-weight: 400;
    }

    /* Microclimate Scrub HUD */
    .microclimate-hud {
      display: flex;
      align-items: center;
      gap: 16px;
      background: rgba(255, 255, 255, 0.04);
      padding: 6px 14px;
      border-radius: 999px;
      border: 1px solid var(--apple-border);
    }

    .hud-time-controls {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .hud-time-presets {
      display: flex;
      gap: 4px;
    }

    .time-pill {
      background: transparent;
      border: 1px solid transparent;
      color: var(--text-secondary);
      font-size: 11px;
      font-weight: 500;
      padding: 3px 9px;
      border-radius: 999px;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      align-items: center;
      gap: 4px;
    }

    .time-pill:hover {
      color: var(--text-primary);
      background: rgba(255, 255, 255, 0.06);
    }

    .time-pill.active {
      background: rgba(56, 189, 248, 0.18);
      color: #38bdf8;
      border-color: rgba(56, 189, 248, 0.4);
      font-weight: 600;
    }

    .hud-metrics {
      display: flex;
      align-items: center;
      gap: 12px;
      border-left: 1px solid rgba(255, 255, 255, 0.1);
      padding-left: 12px;
    }

    .metric-item {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      line-height: 1.1;
    }

    .metric-label {
      font-size: 9px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--text-muted);
      font-weight: 600;
    }

    .metric-val {
      font-size: 12px;
      font-weight: 700;
      color: var(--text-primary);
      display: flex;
      align-items: center;
      gap: 3px;
    }

    .metric-val.hot {
      color: var(--accent-red-light);
    }

    .metric-val.cool {
      color: var(--accent-blue-light);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .icon-btn {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--apple-border);
      color: var(--text-secondary);
      width: 34px;
      height: 34px;
      border-radius: 9px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s;
    }

    .icon-btn:hover {
      background: rgba(255, 255, 255, 0.1);
      color: #ffffff;
    }

    /* Main Container (Left Sidebar + Right Full Map) */
    .app-main {
      flex: 1;
      display: flex;
      position: relative;
      overflow: hidden;
    }

    /* Sidebar */
    aside.sidebar-panel {
      width: 480px;
      min-width: 480px;
      height: 100%;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(24px) saturate(180%);
      -webkit-backdrop-filter: blur(24px) saturate(180%);
      border-right: 1px solid var(--apple-border);
      display: flex;
      flex-direction: column;
      z-index: 900;
      box-shadow: 10px 0 30px rgba(0, 0, 0, 0.4);
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* Tab Switcher in Sidebar */
    .sidebar-tabs {
      display: flex;
      padding: 10px 14px;
      gap: 6px;
      background: rgba(11, 15, 25, 0.6);
      border-bottom: 1px solid var(--apple-border);
    }

    .tab-btn {
      flex: 1;
      background: transparent;
      border: 1px solid transparent;
      padding: 7px 6px;
      border-radius: 8px;
      font-size: 11.5px;
      font-weight: 500;
      color: var(--text-muted);
      cursor: pointer;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 3px;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .tab-btn:hover {
      color: var(--text-primary);
      background: rgba(255, 255, 255, 0.04);
    }

    .tab-btn.active {
      background: rgba(255, 255, 255, 0.09);
      color: #ffffff;
      border-color: rgba(255, 255, 255, 0.12);
      font-weight: 600;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }

    .tab-btn i {
      width: 16px;
      height: 16px;
    }

    /* Sidebar Content Scrollable Area */
    .sidebar-content {
      flex: 1;
      overflow-y: auto;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .sidebar-content::-webkit-scrollbar {
      width: 6px;
    }
    .sidebar-content::-webkit-scrollbar-thumb {
      background: rgba(255, 255, 255, 0.15);
      border-radius: 3px;
    }

    /* Glass Cards */
    .glass-card {
      background: var(--apple-card);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--apple-border);
      border-radius: 14px;
      padding: 14px;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .glass-card:hover {
      border-color: rgba(255, 255, 255, 0.15);
    }

    .card-header-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
    }

    .card-title {
      font-size: 13px;
      font-weight: 700;
      letter-spacing: -0.01em;
      color: var(--text-primary);
      display: flex;
      align-items: center;
      gap: 7px;
    }

    .card-badge {
      font-size: 10px;
      font-weight: 600;
      padding: 2px 7px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.08);
      color: var(--text-secondary);
    }

    /* Route Presets Selector */
    .preset-selector-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .preset-label {
      font-size: 11px;
      font-weight: 600;
      color: var(--text-secondary);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .preset-dropdown {
      width: 100%;
      background: rgba(11, 15, 25, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.14);
      color: #ffffff;
      padding: 9px 12px;
      border-radius: 10px;
      font-size: 12.5px;
      font-family: var(--font-stack);
      outline: none;
      cursor: pointer;
      transition: border-color 0.2s;
    }

    .preset-dropdown:focus {
      border-color: var(--accent-blue-light);
    }

    /* The 4-Pillar Tactile Segmented Control */
    .pillars-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 8px;
    }

    .pillar-btn {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--apple-border);
      border-radius: 12px;
      padding: 10px;
      text-align: left;
      cursor: pointer;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      overflow: hidden;
    }

    .pillar-btn:hover {
      background: rgba(255, 255, 255, 0.08);
      border-color: rgba(255, 255, 255, 0.18);
    }

    .pillar-btn.active[data-pillar="fastest"] {
      background: rgba(14, 165, 233, 0.14);
      border-color: #38bdf8;
      box-shadow: 0 0 16px rgba(56, 189, 248, 0.2);
    }

    .pillar-btn.active[data-pillar="comfort"] {
      background: rgba(16, 185, 129, 0.14);
      border-color: #10b981;
      box-shadow: 0 0 16px rgba(16, 185, 129, 0.2);
    }

    .pillar-btn.active[data-pillar="cheapest"] {
      background: rgba(245, 158, 11, 0.14);
      border-color: #f59e0b;
      box-shadow: 0 0 16px rgba(245, 158, 11, 0.2);
    }

    .pillar-btn.active[data-pillar="wheelchair"] {
      background: rgba(239, 68, 68, 0.14);
      border-color: #f43f5e;
      box-shadow: 0 0 16px rgba(244, 63, 94, 0.2);
    }

    .pillar-icon-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 6px;
    }

    .pillar-icon {
      font-size: 18px;
    }

    .pillar-status-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.2);
    }

    .pillar-btn.active .pillar-status-dot {
      background: currentColor;
      box-shadow: 0 0 8px currentColor;
    }

    .pillar-name {
      font-size: 13px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 2px;
    }

    .pillar-desc {
      font-size: 10.5px;
      color: var(--text-secondary);
      line-height: 1.25;
    }

    /* Route KPIs Grid */
    .kpis-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      margin-top: 10px;
    }

    .kpi-cell {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 10px;
      padding: 9px;
      display: flex;
      flex-direction: column;
    }

    .kpi-label {
      font-size: 9.5px;
      text-transform: uppercase;
      font-weight: 600;
      letter-spacing: 0.04em;
      color: var(--text-muted);
      margin-bottom: 3px;
    }

    .kpi-val {
      font-size: 16px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: -0.02em;
    }

    .kpi-sub {
      font-size: 9.5px;
      color: var(--text-secondary);
      margin-top: 2px;
    }

    /* Modal Breakdown Timeline Bar */
    .timeline-bar-wrapper {
      margin-top: 12px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .timeline-bar-title {
      font-size: 10.5px;
      font-weight: 600;
      color: var(--text-secondary);
      display: flex;
      justify-content: space-between;
    }

    .modal-timeline-bar {
      height: 10px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.08);
      display: flex;
      overflow: hidden;
      gap: 2px;
    }

    .modal-segment {
      height: 100%;
      transition: width 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }

    .modal-segment.feeder { background: #38bdf8; }
    .modal-segment.rail { background: #6366f1; }
    .modal-segment.walk { background: #10b981; }
    .modal-segment.transfer { background: #a855f7; }

    .modal-legend-row {
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 10px;
      color: var(--text-muted);
      margin-top: 2px;
      flex-wrap: wrap;
    }

    .legend-item {
      display: flex;
      align-items: center;
      gap: 4px;
    }

    .legend-color-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
    }

    /* Hazard & Optimization Alert Callouts */
    .alert-banner {
      border-radius: 10px;
      padding: 10px 12px;
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 11.5px;
      line-height: 1.35;
      margin-top: 8px;
    }

    .alert-banner.thermal {
      background: rgba(245, 158, 11, 0.12);
      border: 1px solid rgba(245, 158, 11, 0.3);
      color: #fde68a;
    }

    .alert-banner.night {
      background: rgba(99, 102, 241, 0.12);
      border: 1px solid rgba(99, 102, 241, 0.3);
      color: #c7d2fe;
    }

    .alert-banner.wheelchair {
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid rgba(16, 185, 129, 0.3);
      color: #a7f3d0;
    }

    .alert-banner.tariff {
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: #bae6fd;
    }

    .alert-icon {
      font-size: 15px;
      flex-shrink: 0;
      margin-top: 1px;
    }

    /* Step-by-Step Directions Itinerary */
    .steps-container {
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-top: 10px;
    }

    .step-card {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 10px;
      padding: 10px 12px;
      display: flex;
      align-items: flex-start;
      gap: 10px;
      transition: all 0.2s;
      cursor: pointer;
    }

    .step-card:hover {
      background: rgba(255, 255, 255, 0.06);
      border-color: rgba(255, 255, 255, 0.15);
    }

    .step-num-badge {
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.1);
      font-size: 11px;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      color: #ffffff;
    }

    .step-info {
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 2px;
    }

    .step-title-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .step-title {
      font-size: 12px;
      font-weight: 600;
      color: #ffffff;
    }

    .step-time-badge {
      font-size: 10px;
      color: var(--accent-blue-light);
      font-weight: 600;
    }

    .step-desc {
      font-size: 11px;
      color: var(--text-secondary);
      line-height: 1.3;
    }

    .step-meta-row {
      display: flex;
      gap: 8px;
      margin-top: 4px;
      font-size: 9.5px;
      color: var(--text-muted);
    }

    .step-meta-pill {
      background: rgba(255, 255, 255, 0.05);
      padding: 1px 6px;
      border-radius: 4px;
      display: flex;
      align-items: center;
      gap: 3px;
    }

    /* Tab 2: Head-to-Head Simulator */
    .h2h-scenario-banner {
      background: linear-gradient(135deg, rgba(239, 68, 68, 0.15) 0%, rgba(16, 185, 129, 0.15) 100%);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .h2h-title {
      font-size: 13.5px;
      font-weight: 700;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .h2h-sub {
      font-size: 11.5px;
      color: var(--text-secondary);
      line-height: 1.35;
    }

    .h2h-cards-grid {
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-top: 8px;
    }

    .h2h-card {
      border-radius: 12px;
      padding: 12px;
      border: 1px solid transparent;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .h2h-card.gmaps-fail {
      background: rgba(239, 68, 68, 0.08);
      border-color: rgba(239, 68, 68, 0.25);
    }

    .h2h-card.pijak-win {
      background: rgba(16, 185, 129, 0.08);
      border-color: rgba(16, 185, 129, 0.25);
    }

    .h2h-card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .h2h-brand-tag {
      font-size: 12px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .h2h-brand-tag.gmaps { color: #f87171; }
    .h2h-brand-tag.pijak { color: #34d399; }

    .h2h-status-badge {
      font-size: 9.5px;
      font-weight: 700;
      text-transform: uppercase;
      padding: 2px 7px;
      border-radius: 999px;
    }

    .h2h-status-badge.fail {
      background: rgba(239, 68, 68, 0.2);
      color: #fca5a5;
    }

    .h2h-status-badge.win {
      background: rgba(16, 185, 129, 0.2);
      color: #6ee7b7;
    }

    .h2h-metric-row {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 6px;
      background: rgba(0, 0, 0, 0.2);
      border-radius: 8px;
      padding: 8px;
    }

    .h2h-metric {
      display: flex;
      flex-direction: column;
    }

    .h2h-metric-label {
      font-size: 9px;
      color: var(--text-muted);
      text-transform: uppercase;
      font-weight: 600;
    }

    .h2h-metric-val {
      font-size: 14px;
      font-weight: 700;
      color: #ffffff;
    }

    .h2h-details-list {
      font-size: 11px;
      color: var(--text-secondary);
      line-height: 1.4;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .h2h-details-item {
      display: flex;
      align-items: flex-start;
      gap: 6px;
    }

    .h2h-details-item i {
      flex-shrink: 0;
      margin-top: 2px;
      width: 14px;
      height: 14px;
    }

    .simulate-btn {
      width: 100%;
      background: linear-gradient(135deg, #0284c7 0%, #0d9488 100%);
      color: #ffffff;
      border: none;
      padding: 10px;
      border-radius: 10px;
      font-size: 12.5px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 4px 14px rgba(13, 148, 136, 0.35);
      transition: all 0.2s;
    }

    .simulate-btn:hover {
      opacity: 0.95;
      transform: translateY(-1px);
    }

    /* Head to Head Matrix Table */
    .matrix-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 10.5px;
      margin-top: 8px;
    }

    .matrix-table th, .matrix-table td {
      padding: 6px 8px;
      text-align: left;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    }

    .matrix-table th {
      color: var(--text-muted);
      font-weight: 600;
      text-transform: uppercase;
      font-size: 9px;
    }

    .matrix-table td.bad {
      color: #fca5a5;
      font-weight: 600;
    }

    .matrix-table td.good {
      color: #6ee7b7;
      font-weight: 600;
    }

    /* Tab 3: Station Catchment & Gradient Table */
    .gradient-filter-row {
      display: flex;
      gap: 6px;
      margin-bottom: 8px;
      overflow-x: auto;
      padding-bottom: 4px;
    }

    .filter-chip {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--apple-border);
      color: var(--text-secondary);
      font-size: 10.5px;
      padding: 3px 8px;
      border-radius: 999px;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s;
    }

    .filter-chip.active {
      background: rgba(56, 189, 248, 0.18);
      color: #38bdf8;
      border-color: rgba(56, 189, 248, 0.4);
    }

    .gradient-table-wrapper {
      max-height: 280px;
      overflow-y: auto;
      border: 1px solid var(--apple-border);
      border-radius: 8px;
      background: rgba(0, 0, 0, 0.2);
    }

    .gradient-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 11px;
    }

    .gradient-table th {
      position: sticky;
      top: 0;
      background: #111827;
      padding: 7px 8px;
      color: var(--text-muted);
      font-weight: 600;
      text-transform: uppercase;
      font-size: 9px;
      border-bottom: 1px solid var(--apple-border);
      text-align: left;
    }

    .gradient-table td {
      padding: 6px 8px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
      color: var(--text-secondary);
      cursor: pointer;
    }

    .gradient-table tr:hover td {
      background: rgba(255, 255, 255, 0.04);
      color: #ffffff;
    }

    .pct-bar-wrapper {
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .pct-bar-bg {
      flex: 1;
      height: 6px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 999px;
      overflow: hidden;
    }

    .pct-bar-fill {
      height: 100%;
      border-radius: 999px;
    }

    .pct-bar-fill.high { background: #10b981; }
    .pct-bar-fill.mid { background: #f59e0b; }
    .pct-bar-fill.zero { background: #ef4444; }

    /* Tab 4: Spatial Pipeline & Wisma Cheshire */
    .pipeline-step-flow {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .pipeline-node {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--apple-border);
      border-radius: 10px;
      padding: 10px;
      display: flex;
      align-items: flex-start;
      gap: 10px;
    }

    .pipeline-node-icon {
      width: 28px;
      height: 28px;
      border-radius: 8px;
      background: rgba(56, 189, 248, 0.15);
      color: #38bdf8;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    .pipeline-node-body {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }

    .pipeline-node-title {
      font-size: 12px;
      font-weight: 700;
      color: #ffffff;
    }

    .pipeline-node-desc {
      font-size: 11px;
      color: var(--text-secondary);
      line-height: 1.3;
    }

    /* Right Map Container */
    .map-canvas-container {
      flex: 1;
      height: 100%;
      position: relative;
      background: #090d16;
    }

    #map {
      width: 100%;
      height: 100%;
      background: #0b0f19;
    }

    /* Floating Apple Map Layer Controls Overlay */
    .map-overlay-panel {
      position: absolute;
      top: 16px;
      right: 16px;
      z-index: 800;
      background: rgba(15, 23, 42, 0.82);
      backdrop-filter: blur(20px) saturate(180%);
      -webkit-backdrop-filter: blur(20px) saturate(180%);
      border: 1px solid var(--apple-border);
      border-radius: 14px;
      padding: 12px;
      width: 250px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
    }

    .overlay-title {
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .layer-toggle-list {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .layer-toggle-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 11.5px;
      color: var(--text-primary);
      cursor: pointer;
      user-select: none;
    }

    .layer-left {
      display: flex;
      align-items: center;
      gap: 7px;
    }

    .layer-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
    }

    /* Custom Checkbox Toggle */
    .apple-switch {
      position: relative;
      display: inline-block;
      width: 32px;
      height: 18px;
    }

    .apple-switch input {
      opacity: 0;
      width: 0;
      height: 0;
    }

    .switch-slider {
      position: absolute;
      cursor: pointer;
      top: 0; left: 0; right: 0; bottom: 0;
      background-color: rgba(255, 255, 255, 0.15);
      transition: .3s;
      border-radius: 34px;
    }

    .switch-slider:before {
      position: absolute;
      content: "";
      height: 14px;
      width: 14px;
      left: 2px;
      bottom: 2px;
      background-color: white;
      transition: .3s;
      border-radius: 50%;
    }

    input:checked + .switch-slider {
      background-color: var(--accent-blue-light);
    }

    input:checked + .switch-slider:before {
      transform: translateX(14px);
    }

    /* Quick Map Bookmarks */
    .bookmark-btn-group {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 5px;
      margin-top: 4px;
    }

    .bookmark-btn {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--apple-border);
      color: var(--text-secondary);
      font-size: 10px;
      font-weight: 500;
      padding: 5px 6px;
      border-radius: 6px;
      cursor: pointer;
      text-align: center;
      transition: all 0.2s;
    }

    .bookmark-btn:hover {
      background: rgba(255, 255, 255, 0.1);
      color: #ffffff;
      border-color: rgba(255, 255, 255, 0.2);
    }

    /* Floating Legend Badge on Map */
    .map-floating-legend {
      position: absolute;
      bottom: 24px;
      left: 16px;
      z-index: 800;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid var(--apple-border);
      border-radius: 10px;
      padding: 8px 12px;
      display: flex;
      align-items: center;
      gap: 14px;
      font-size: 11px;
      color: var(--text-secondary);
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.4);
    }

    .legend-indicator {
      display: flex;
      align-items: center;
      gap: 5px;
    }

    .line-sample {
      width: 16px;
      height: 3px;
      border-radius: 2px;
    }

    /* Responsive Handling */
    @media (max-width: 1024px) {
      aside.sidebar-panel {
        width: 400px;
        min-width: 400px;
      }
    }
    @media (max-width: 768px) {
      .app-main {
        flex-direction: column;
      }
      aside.sidebar-panel {
        width: 100%;
        min-width: 100%;
        height: 50vh;
      }
      .map-canvas-container {
        height: 50vh;
      }
      .microclimate-hud {
        display: none;
      }
    }
  </style>
</head>
<body>

  <!-- Top Apple Header & Microclimate Live HUD -->
  <header class="apple-header">
    <div class="brand-section">
      <div class="brand-logo-badge">
        <i data-lucide="compass" style="width: 22px; height: 22px;"></i>
      </div>
      <div class="brand-titles">
        <div class="brand-title">
          PIJAK TRANSIT ENGINE
          <span class="brand-tag">Research v2.4</span>
        </div>
        <div class="brand-subtitle">
          Multimodal 4-Pillar Router · Microclimate Spatial Prototype · Apple Developer Academy @ BINUS
        </div>
      </div>
    </div>

    <!-- Microclimate Scrub HUD -->
    <div class="microclimate-hud">
      <div class="hud-time-controls">
        <span class="metric-label" style="margin-right: 4px;">Time:</span>
        <div class="hud-time-presets">
          <button class="time-pill" data-time="08:30" onclick="setTimeOfDay('08:30')">
            <i data-lucide="sunrise" style="width: 12px; height: 12px;"></i> 08:30 AM
          </button>
          <button class="time-pill" data-time="12:00" onclick="setTimeOfDay('12:00')">
            <i data-lucide="sun" style="width: 12px; height: 12px;"></i> 12:00 PM
          </button>
          <button class="time-pill" data-time="16:30" onclick="setTimeOfDay('16:30')">
            <i data-lucide="sunset" style="width: 12px; height: 12px;"></i> 16:30 PM
          </button>
          <button class="time-pill active" data-time="22:30" onclick="setTimeOfDay('22:30')">
            <i data-lucide="moon" style="width: 12px; height: 12px;"></i> 22:30 PM (Night)
          </button>
        </div>
      </div>

      <div class="hud-metrics">
        <div class="metric-item">
          <span class="metric-label">Ambient / Feels</span>
          <span class="metric-val" id="hud-temp">26.8°C / 27.5°C</span>
        </div>
        <div class="metric-item">
          <span class="metric-label">UV Index</span>
          <span class="metric-val" id="hud-uv">0.0 (Night)</span>
        </div>
        <div class="metric-item">
          <span class="metric-label">Safe Walk Cap</span>
          <span class="metric-val" id="hud-walkcap">800 m</span>
        </div>
        <div class="metric-item">
          <span class="metric-label">Feeder Status</span>
          <span class="metric-val" id="hud-curfew" style="color: #fbbf24;">Late Curfew</span>
        </div>
      </div>
    </div>

    <div class="header-actions">
      <button class="icon-btn" onclick="toggleMapStyle()" title="Toggle Basemap Style">
        <i data-lucide="map" style="width: 16px; height: 16px;"></i>
      </button>
      <button class="icon-btn" onclick="recenterMap()" title="Fit Route Extent">
        <i data-lucide="crosshair" style="width: 16px; height: 16px;"></i>
      </button>
    </div>
  </header>

  <!-- App Main Content Area -->
  <main class="app-main">

    <!-- Left Sidebar Router Dashboard -->
    <aside class="sidebar-panel">
      
      <!-- Top Navigation Tabs -->
      <nav class="sidebar-tabs">
        <button class="tab-btn active" data-tab="router" onclick="switchTab('router')">
          <i data-lucide="navigation"></i>
          <span>4-Pillar Router</span>
        </button>
        <button class="tab-btn" data-tab="head2head" onclick="switchTab('head2head')">
          <i data-lucide="swords"></i>
          <span>Head-to-Head</span>
        </button>
        <button class="tab-btn" data-tab="catchment" onclick="switchTab('catchment')">
          <i data-lucide="circle-dot"></i>
          <span>Catchment & Gradient</span>
        </button>
        <button class="tab-btn" data-tab="pipeline" onclick="switchTab('pipeline')">
          <i data-lucide="layers"></i>
          <span>Spatial & Wisma</span>
        </button>
      </nav>

      <!-- Tab 1: 4-Pillar Interactive Router -->
      <div class="sidebar-content" id="tab-content-router">
        
        <!-- Preset Dropdown Selector -->
        <div class="glass-card">
          <div class="preset-selector-group">
            <label class="preset-label" for="route-preset-select">Origin & Destination Preset</label>
            <select class="preset-dropdown" id="route-preset-select" onchange="onPresetChange(this.value)">
              <option value="preset_bsd_kebayoran" selected>Apple Dev Academy (BSD) ➔ Jl. Kuburan Lama (Palmerah/Kebayoran)</option>
              <option value="preset_dukuh_senayan">Dukuh Atas Multimodal TOD ➔ Gelora Bung Karno / MRT Senayan</option>
              <option value="preset_wisma_cheshire">Wisma Cheshire (Cilandak) ➔ Dukuh Atas TOD Nexus [Wheelchair Test]</option>
              <option value="preset_rawabuntu_palmerah">Stasiun KRL Rawa Buntu ➔ Palmerah Market / SMAN 3</option>
            </select>
          </div>
        </div>

        <!-- 4-Pillar Tactile Segmented Buttons -->
        <div class="glass-card">
          <div class="card-header-row">
            <span class="card-title">
              <i data-lucide="git-branch" style="width: 15px; height: 15px; color: var(--accent-blue-light);"></i>
              Routing Optimization Pillar
            </span>
            <span class="card-badge" id="active-pillar-badge">Fastest Mode</span>
          </div>

          <div class="pillars-grid">
            <button class="pillar-btn active" data-pillar="fastest" onclick="selectPillar('fastest')">
              <div class="pillar-icon-row">
                <span class="pillar-icon">⚡</span>
                <span class="pillar-status-dot"></span>
              </div>
              <div class="pillar-name">Fastest</div>
              <div class="pillar-desc">Chained multimodal A* · Min trip time</div>
            </button>

            <button class="pillar-btn" data-pillar="comfort" onclick="selectPillar('comfort')">
              <div class="pillar-icon-row">
                <span class="pillar-icon">🛋️</span>
                <span class="pillar-status-dot"></span>
              </div>
              <div class="pillar-name">Comfort</div>
              <div class="pillar-desc">Solar shade · Night safety · 500m walk cap</div>
            </button>

            <button class="pillar-btn" data-pillar="cheapest" onclick="selectPillar('cheapest')">
              <div class="pillar-icon-row">
                <span class="pillar-icon">💰</span>
                <span class="pillar-status-dot"></span>
              </div>
              <div class="pillar-name">Cheapest</div>
              <div class="pillar-desc">Rp 0 JakLingko · Rp 3k KRL · Rp 3.5k TJ</div>
            </button>

            <button class="pillar-btn" data-pillar="wheelchair" onclick="selectPillar('wheelchair')">
              <div class="pillar-icon-row">
                <span class="pillar-icon">♿</span>
                <span class="pillar-status-dot"></span>
              </div>
              <div class="pillar-name">Wheelchair</div>
              <div class="pillar-desc">Slope ≤ 8.33% · 0 steps · Lifts verified</div>
            </button>
          </div>
        </div>

        <!-- Dynamic Route Overview KPI Card -->
        <div class="glass-card">
          <div class="card-header-row">
            <span class="card-title" id="route-title-header">
              Trip Overview
            </span>
            <span class="card-badge" id="route-arrival-clock" style="color: #38bdf8;">Arrival ~23:18 WIB</span>
          </div>

          <div class="kpis-grid">
            <div class="kpi-cell">
              <span class="kpi-label">Total Time</span>
              <span class="kpi-val" id="kpi-total-time">40 min</span>
              <span class="kpi-sub" id="kpi-time-sub">vs 1h 48m transit</span>
            </div>
            <div class="kpi-cell">
              <span class="kpi-label">Transit Fare</span>
              <span class="kpi-val" id="kpi-fare" style="color: #34d399;">Rp 3.000</span>
              <span class="kpi-sub" id="kpi-fare-sub">Saves Rp 79.000</span>
            </div>
            <div class="kpi-cell">
              <span class="kpi-label">Walk Exposure</span>
              <span class="kpi-val" id="kpi-walk-dist">550 m</span>
              <span class="kpi-sub" id="kpi-walk-time">8 min walk</span>
            </div>
            <div class="kpi-cell">
              <span class="kpi-label">In-Vehicle</span>
              <span class="kpi-val" id="kpi-transit-time">32 min</span>
              <span class="kpi-sub" id="kpi-transit-sub">KRL + Feeder</span>
            </div>
            <div class="kpi-cell">
              <span class="kpi-label">Comfort Score</span>
              <span class="kpi-val" id="kpi-comfort-score" style="color: #60a5fa;">88%</span>
              <span class="kpi-sub" id="kpi-comfort-sub">Lit & Sheltered</span>
            </div>
            <div class="kpi-cell">
              <span class="kpi-label">Step-Free</span>
              <span class="kpi-val" id="kpi-accessible-score" style="color: #a7f3d0;">100%</span>
              <span class="kpi-sub" id="kpi-accessible-sub">0 Steps</span>
            </div>
          </div>

          <!-- Modal Breakdown Timeline Bar -->
          <div class="timeline-bar-wrapper">
            <div class="timeline-bar-title">
              <span>Modal Time Breakdown</span>
              <span id="timeline-breakdown-text">Feeder (6m) · Rail (26m) · Walk (8m)</span>
            </div>
            <div class="modal-timeline-bar" id="modal-timeline-bar">
              <div class="modal-segment feeder" id="bar-feeder" style="width: 15%;"></div>
              <div class="modal-segment rail" id="bar-rail" style="width: 65%;"></div>
              <div class="modal-segment walk" id="bar-walk" style="width: 20%;"></div>
            </div>
            <div class="modal-legend-row">
              <div class="legend-item"><span class="legend-color-dot" style="background: #38bdf8;"></span> Feeder/Ojol</div>
              <div class="legend-item"><span class="legend-color-dot" style="background: #6366f1;"></span> KRL / Rail Trunk</div>
              <div class="legend-item"><span class="legend-color-dot" style="background: #10b981;"></span> Pedestrian Walk</div>
              <div class="legend-item"><span class="legend-color-dot" style="background: #a855f7;"></span> Transfer Sync</div>
            </div>
          </div>

          <!-- Dynamic Alerts & Hazard Shields -->
          <div id="dynamic-alerts-container">
            <!-- Alert injected via JS -->
          </div>
        </div>

        <!-- Step-by-Step Directions Itinerary -->
        <div class="glass-card">
          <div class="card-header-row">
            <span class="card-title">
              <i data-lucide="milestone" style="width: 15px; height: 15px; color: var(--accent-teal-light);"></i>
              Turn-by-Turn Navigation Steps
            </span>
            <span class="card-badge" id="step-count-badge">5 Steps</span>
          </div>

          <div class="steps-container" id="steps-list-container">
            <!-- Injected via JS -->
          </div>
        </div>

      </div>

      <!-- Tab 2: Google Maps vs. Pijak Head-to-Head Simulator -->
      <div class="sidebar-content" id="tab-content-head2head" style="display: none;">
        
        <div class="h2h-scenario-banner">
          <div class="h2h-title">
            <i data-lucide="flame" style="width: 18px; height: 18px; color: #ef4444;"></i>
            The 10:30 PM BSD Nocturnal Commute Challenge
          </div>
          <div class="h2h-sub">
            Origin: <strong>Apple Developer Academy @ BINUS (BSD GOP 9)</strong><br />
            Destination: <strong>Jl. Kuburan Lama (Palmerah / Kebayoran)</strong><br />
            Time of Departure: <strong>22:30 WIB (Night Curfew)</strong>
          </div>
        </div>

        <button class="simulate-btn" onclick="animateHeadToHeadCommute()">
          <i data-lucide="play" style="width: 16px; height: 16px;"></i>
          Run Live Route Simulation on Map
        </button>

        <div class="h2h-cards-grid">
          
          <!-- Google Maps Failure Card -->
          <div class="h2h-card gmaps-fail">
            <div class="h2h-card-header">
              <span class="h2h-brand-tag gmaps">
                <i data-lucide="x-circle" style="width: 16px; height: 16px;"></i>
                Google Maps Navigation
              </span>
              <span class="h2h-status-badge fail">Failure Modes</span>
            </div>

            <div class="h2h-metric-row">
              <div class="h2h-metric">
                <span class="h2h-metric-label">Travel Time</span>
                <span class="h2h-metric-val" style="color: #f87171;">3h 32m – 7h 50m</span>
              </div>
              <div class="h2h-metric">
                <span class="h2h-metric-label">Walk Exposure</span>
                <span class="h2h-metric-val" style="color: #f87171;">47 min (Dark)</span>
              </div>
              <div class="h2h-metric">
                <span class="h2h-metric-label">Trip Fare</span>
                <span class="h2h-metric-val">Rp 92.000+</span>
              </div>
            </div>

            <div class="h2h-details-list">
              <div class="h2h-details-item">
                <i data-lucide="alert-triangle" style="color: #f87171;"></i>
                <span><strong>The Kalideres/Airport Detour:</strong> Fails to chain first-mile feeder; routes commuter 38 km north via expressway shoulders.</span>
              </div>
              <div class="h2h-details-item">
                <i data-lucide="eye-off" style="color: #f87171;"></i>
                <span><strong>The 47-Minute Dark Walk:</strong> Directs commuter through pitch-black suburban alleys (<em>gang tikus</em>) with open gutters (<em>got</em>).</span>
              </div>
              <div class="h2h-details-item">
                <i data-lucide="clock" style="color: #f87171;"></i>
                <span><strong>Stranded Signal:</strong> Often flags transit as "Unavailable until 03:35 AM tomorrow" or forces a surge taxi.</span>
              </div>
            </div>
          </div>

          <!-- Pijak Multimodal Solution Card -->
          <div class="h2h-card pijak-win">
            <div class="h2h-card-header">
              <span class="h2h-brand-tag pijak">
                <i data-lucide="check-circle" style="width: 16px; height: 16px;"></i>
                Pijak Multimodal Solution
              </span>
              <span class="h2h-status-badge win">Proven Solution</span>
            </div>

            <div class="h2h-metric-row">
              <div class="h2h-metric">
                <span class="h2h-metric-label">Travel Time</span>
                <span class="h2h-metric-val" style="color: #34d399;">40 min Total</span>
              </div>
              <div class="h2h-metric">
                <span class="h2h-metric-label">Walk Exposure</span>
                <span class="h2h-metric-val" style="color: #34d399;">8 min (Lit)</span>
              </div>
              <div class="h2h-metric">
                <span class="h2h-metric-label">Trip Fare</span>
                <span class="h2h-metric-val" style="color: #34d399;">Rp 3.000</span>
              </div>
            </div>

            <div class="h2h-details-list">
              <div class="h2h-details-item">
                <i data-lucide="bike" style="color: #34d399;"></i>
                <span><strong>Feeder Integration:</strong> 6-min shuttle/ojol drop-off at Stasiun Rawa Buntu.</span>
              </div>
              <div class="h2h-details-item">
                <i data-lucide="train" style="color: #34d399;"></i>
                <span><strong>KRL Express Trunk:</strong> 26-min high-speed Commuter Line directly to Kebayoran (Rp 3.000).</span>
              </div>
              <div class="h2h-details-item">
                <i data-lucide="shield-check" style="color: #34d399;"></i>
                <span><strong>Passive Surveillance:</strong> 8-min walk strictly routed along Jl. Kebayoran Lama with active 24h stores.</span>
              </div>
            </div>
          </div>

        </div>

        <!-- Comparative Matrix Table -->
        <div class="glass-card">
          <div class="card-header-row">
            <span class="card-title">Performance Benchmark Matrix</span>
          </div>

          <table class="matrix-table">
            <thead>
              <tr>
                <th>Evaluation Metric</th>
                <th>Google Maps</th>
                <th>Pijak 4-Pillar</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Total Travel Duration</td>
                <td class="bad">3h 32m – 7h 50m</td>
                <td class="good">40 min (Arrival 23:18)</td>
              </tr>
              <tr>
                <td>Out-of-Pocket Cost</td>
                <td class="bad">Rp 92.000+ (Taxi)</td>
                <td class="good">Rp 3.000 (KRL)</td>
              </tr>
              <tr>
                <td>Pedestrian Dark Exposure</td>
                <td class="bad">47 min unlit got</td>
                <td class="good">8 min continuous light</td>
              </tr>
              <tr>
                <td>Crime / Begal Vulnerability</td>
                <td class="bad">Severe (Gang Tikus)</td>
                <td class="good">Protected (Commercial Spine)</td>
              </tr>
              <tr>
                <td>Wheelchair Feasibility</td>
                <td class="bad">0% (Stairs on Overpass)</td>
                <td class="good">100% Step-Free Ramps & Lifts</td>
              </tr>
            </tbody>
          </table>
        </div>

      </div>

      <!-- Tab 3: Station Catchment Explorer & Walkability Gradient -->
      <div class="sidebar-content" id="tab-content-catchment" style="display: none;">
        
        <div class="glass-card">
          <div class="card-header-row">
            <span class="card-title">
              <i data-lucide="radar" style="width: 15px; height: 15px; color: var(--accent-blue-light);"></i>
              500m Station Walkable Catchments
            </span>
          </div>
          <p style="font-size: 11.5px; color: var(--text-secondary); line-height: 1.4;">
            Circular and network-bounded 500m walksheds (6–7 minutes walking threshold) surrounding Greater Jakarta transit nodes.
          </p>
          <div class="bookmark-btn-group" style="margin-top: 10px;">
            <button class="bookmark-btn" onclick="focusStation('dukuh_atas_mrt')">Dukuh Atas TOD</button>
            <button class="bookmark-btn" onclick="focusStation('kebayoran')">Stn. Kebayoran</button>
            <button class="bookmark-btn" onclick="focusStation('rawa_buntu')">Stn. Rawa Buntu</button>
            <button class="bookmark-btn" onclick="focusStation('fatmawati')">MRT Fatmawati</button>
          </div>
        </div>

        <!-- The Walkability Gradient Table (from gradient.csv) -->
        <div class="glass-card">
          <div class="card-header-row">
            <span class="card-title">
              <i data-lucide="trending-down" style="width: 15px; height: 15px; color: var(--accent-red-light);"></i>
              The Walkability Gradient (69 Streets)
            </span>
            <span class="card-badge" style="color: #f87171;">65.2% Have 0% Sidewalk</span>
          </div>

          <div class="gradient-filter-row">
            <button class="filter-chip active" onclick="filterGradientTable('all', this)">All (68)</button>
            <button class="filter-chip" onclick="filterGradientTable('high', this)">100% Arterial (21)</button>
            <button class="filter-chip" onclick="filterGradientTable('mid', this)">60–75% Transition (3)</button>
            <button class="filter-chip" onclick="filterGradientTable('zero', this)">0% Back-Streets (44)</button>
          </div>

          <div class="gradient-table-wrapper">
            <table class="gradient-table" id="gradient-table-elem">
              <thead>
                <tr>
                  <th>Street Name</th>
                  <th>Length</th>
                  <th>Sidewalk %</th>
                </tr>
              </thead>
              <tbody id="gradient-table-body">
                <!-- Injected via JS -->
              </tbody>
            </table>
          </div>
        </div>

      </div>

      <!-- Tab 4: Spatial Pipeline & Wisma Cheshire Co-Testing -->
      <div class="sidebar-content" id="tab-content-pipeline" style="display: none;">
        
        <div class="glass-card">
          <div class="card-header-row">
            <span class="card-title">
              <i data-lucide="cpu" style="width: 15px; height: 15px; color: var(--accent-blue-light);"></i>
              Spatial Computing Architecture
            </span>
          </div>

          <div class="pipeline-step-flow">
            <div class="pipeline-node">
              <div class="pipeline-node-icon"><i data-lucide="satellite"></i></div>
              <div class="pipeline-node-body">
                <div class="pipeline-node-title">Tier 1: Tile2Net Aerial Segmentation</div>
                <div class="pipeline-node-desc">0.3m orthophoto analysis (HRNet/SegFormer) classifying roadways, sidewalks, and crosswalks.</div>
              </div>
            </div>

            <div class="pipeline-node">
              <div class="pipeline-node-icon"><i data-lucide="sun"></i></div>
              <div class="pipeline-node-body">
                <div class="pipeline-node-title">Tier 2: CoolWalks Solar Ray-Casting</div>
                <div class="pipeline-node-desc">2.5D building extrusion and hourly solar azimuth/zenith projection computing shade fraction $S_e(t)$.</div>
              </div>
            </div>

            <div class="pipeline-node">
              <div class="pipeline-node-icon"><i data-lucide="git-merge"></i></div>
              <div class="pipeline-node-body">
                <div class="pipeline-node-title">Tier 3: 4-Pillar Algorithmic Router</div>
                <div class="pipeline-node-desc">A* graph engine combining GTFS timetables, Rupiah tariff formulas, and strict step-free topological pruning.</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Wisma Cheshire Partnership Card -->
        <div class="glass-card">
          <div class="card-header-row">
            <span class="card-title">
              <i data-lucide="heart-handshake" style="width: 15px; height: 15px; color: #f43f5e;"></i>
              Wisma Cheshire Co-Testing Protocol
            </span>
            <span class="card-badge" style="color: #6ee7b7;">Ground-Truth</span>
          </div>
          <p style="font-size: 11.5px; color: var(--text-secondary); line-height: 1.4;">
            In-situ participatory research with permanent manual wheelchair residents at <strong>Wisma Cheshire Indonesia</strong> (Jl. Wijaya Kusuma No. 15A, Cilandak Barat, South Jakarta).
          </p>
          <div style="margin-top: 8px; font-size: 11px; color: var(--text-secondary); display: flex; flex-direction: column; gap: 5px;">
            <div>• <strong>Agency & Dignity:</strong> Eliminates unexpected 20-cm drop-offs that force wheelchair users into helpless dependence on strangers.</div>
            <div>• <strong>Biomechanical Strain:</strong> Calibrates upper-body energy expenditure on slopes exceeding 8.33% (Permen PUPR 14/2017).</div>
            <div>• <strong>Fatmawati Corridor:</strong> Verified continuous ramp path linking Wisma Cheshire directly to MRT Fatmawati Station Elevators.</div>
          </div>
          <button class="bookmark-btn" style="width: 100%; margin-top: 10px; padding: 7px;" onclick="focusStation('wisma_cheshire')">
            <i data-lucide="map-pin" style="width: 12px; height: 12px; display: inline; vertical-align: middle;"></i> Fly to Wisma Cheshire & MRT Fatmawati
          </button>
        </div>

      </div>

    </aside>

    <!-- Right Map Canvas Container -->
    <div class="map-canvas-container">
      <div id="map"></div>

      <!-- Floating Map Layer Controls Overlay (Apple Glass) -->
      <div class="map-overlay-panel">
        <div class="overlay-title">
          <span>Map Visual Layers</span>
          <i data-lucide="sliders-horizontal" style="width: 14px; height: 14px;"></i>
        </div>

        <div class="layer-toggle-list">
          
          <label class="layer-toggle-item">
            <div class="layer-left">
              <span class="layer-dot" style="background: #38bdf8;"></span>
              <span>Transit Rail & Feeder</span>
            </div>
            <label class="apple-switch">
              <input type="checkbox" id="layer-transit" checked onchange="toggleLayer('transit', this.checked)">
              <span class="switch-slider"></span>
            </label>
          </label>

          <label class="layer-toggle-item">
            <div class="layer-left">
              <span class="layer-dot" style="background: #a855f7;"></span>
              <span>500m Catchment Buffers</span>
            </div>
            <label class="apple-switch">
              <input type="checkbox" id="layer-catchment" checked onchange="toggleLayer('catchment', this.checked)">
              <span class="switch-slider"></span>
            </label>
          </label>

          <label class="layer-toggle-item">
            <div class="layer-left">
              <span class="layer-dot" style="background: #10b981;"></span>
              <span>Dukuh Atas Facilities</span>
            </div>
            <label class="apple-switch">
              <input type="checkbox" id="layer-facilities" checked onchange="toggleLayer('facilities', this.checked)">
              <span class="switch-slider"></span>
            </label>
          </label>

          <label class="layer-toggle-item">
            <div class="layer-left">
              <span class="layer-dot" style="background: #fbbf24;"></span>
              <span>CoolWalks Solar Shade</span>
            </div>
            <label class="apple-switch">
              <input type="checkbox" id="layer-shade" checked onchange="toggleLayer('shade', this.checked)">
              <span class="switch-slider"></span>
            </label>
          </label>

          <label class="layer-toggle-item">
            <div class="layer-left">
              <span class="layer-dot" style="background: #6366f1;"></span>
              <span>Night Streetlights</span>
            </div>
            <label class="apple-switch">
              <input type="checkbox" id="layer-lighting" checked onchange="toggleLayer('lighting', this.checked)">
              <span class="switch-slider"></span>
            </label>
          </label>

          <label class="layer-toggle-item">
            <div class="layer-left">
              <span class="layer-dot" style="background: #f43f5e;"></span>
              <span>Wheelchair Lifts / Ramps</span>
            </div>
            <label class="apple-switch">
              <input type="checkbox" id="layer-wheelchair" checked onchange="toggleLayer('wheelchair', this.checked)">
              <span class="switch-slider"></span>
            </label>
          </label>

        </div>

        <div class="overlay-title" style="margin-top: 4px;">
          <span>Quick Bookmarks</span>
        </div>

        <div class="bookmark-btn-group">
          <button class="bookmark-btn" onclick="focusStation('dukuh_atas_mrt')">Dukuh Atas TOD</button>
          <button class="bookmark-btn" onclick="focusStation('binus_bsd')">BSD ➔ Palmerah</button>
          <button class="bookmark-btn" onclick="focusStation('wisma_cheshire')">Wisma Cheshire</button>
          <button class="bookmark-btn" onclick="focusStation('csw_asean')">CSW / ASEAN</button>
        </div>
      </div>

      <!-- Floating Map Legend Badge -->
      <div class="map-floating-legend">
        <div class="legend-indicator">
          <span class="line-sample" style="background: #38bdf8;"></span>
          <span>Feeder / Ojol</span>
        </div>
        <div class="legend-indicator">
          <span class="line-sample" style="background: #6366f1;"></span>
          <span>KRL / MRT</span>
        </div>
        <div class="legend-indicator">
          <span class="line-sample" style="background: #10b981;"></span>
          <span>Pedestrian</span>
        </div>
        <div class="legend-indicator">
          <span class="line-sample" style="background: #ef4444; border-top: 2px dashed #ef4444;"></span>
          <span>G-Maps Detour</span>
        </div>
      </div>

    </div>

  </main>

  <!-- Embedded Datasets & Script Engine -->
  <script>
    // Embedded Spatial Data from Python
    const FACILITIES_DATA = __FACILITIES_JSON__;
    const GRADIENT_DATA = __GRADIENT_JSON__;
    const PLACES_DATA = __PLACES_JSON__;
    
    // Stations Catalog
    const STATIONS = __STATIONS_JSON__;
    
    // Head to head and preset route polylines & steps definition
    const ROUTE_PRESETS = __PRESETS_JSON__;
    
    // High-rise building massing footprints around Dukuh Atas for solar shadow modeling
    const DUKUH_BUILDINGS = [
      { name: "Wisma 46 (BNI)", height: 262, lat: -6.2030, lon: 106.8215, radius: 25 },
      { name: "Menara Astra", height: 261, lat: -6.2065, lon: 106.8220, radius: 28 },
      { name: "Chase Plaza", height: 110, lat: -6.2085, lon: 106.8210, radius: 22 },
      { name: "Indofood Tower", height: 192, lat: -6.2078, lon: 106.8228, radius: 26 },
      { name: "UOB Plaza / Thamrin Nine", height: 383, lat: -6.1995, lon: 106.8225, radius: 30 },
      { name: "Shangri-La Jakarta", height: 140, lat: -6.2038, lon: 106.8190, radius: 35 },
      { name: "Dukuh Atas TOD Hub", height: 35, lat: -6.2020, lon: 106.8235, radius: 20 }
    ];

    // Global App State
    let currentTab = 'router';
    let currentPreset = 'preset_bsd_kebayoran';
    let currentPillar = 'fastest';
    let currentTimeOfDay = '22:30';
    let currentBasemap = 'dark';
    
    let map;
    let baseTileLayer;
    let referenceTileLayer = null;
    
    // Layer Groups
    let transitLayerGroup;
    let catchmentLayerGroup;
    let facilitiesLayerGroup;
    let shadeLayerGroup;
    let lightingLayerGroup;
    let wheelchairLayerGroup;
    let activeRouteLayerGroup;
    let simulationLayerGroup;

    // Simulation animation state
    let simInterval = null;
    let simCommuterMarker = null;

    // Initialize Map and UI
    window.addEventListener('DOMContentLoaded', () => {
      lucide.createIcons();
      initMap();
      loadGradientTable(GRADIENT_DATA);
      updateMicroclimateState('22:30');
      renderRouteSolution();
    });

    function initMap() {
      // Create Leaflet Map centered on South Jakarta / Dukuh Atas corridor
      map = L.map('map', {
        center: [-6.2300, 106.7800],
        zoom: 12,
        zoomControl: false
      });

      // Position Zoom Control top-left
      L.control.zoom({ position: 'topleft' }).addTo(map);

      // Basemap Tiles: CartoDB Dark Matter by default
      setBasemap('dark');

      // Create Layer Groups
      transitLayerGroup = L.layerGroup(); transitLayerGroup.addTo(map);
      catchmentLayerGroup = L.layerGroup(); catchmentLayerGroup.addTo(map);
      facilitiesLayerGroup = L.layerGroup(); facilitiesLayerGroup.addTo(map);
      shadeLayerGroup = L.layerGroup(); shadeLayerGroup.addTo(map);
      lightingLayerGroup = L.layerGroup(); lightingLayerGroup.addTo(map);
      wheelchairLayerGroup = L.layerGroup(); wheelchairLayerGroup.addTo(map);
      activeRouteLayerGroup = L.layerGroup(); activeRouteLayerGroup.addTo(map);
      simulationLayerGroup = L.layerGroup(); simulationLayerGroup.addTo(map);

      // Populate Layers
      renderTransitNetwork();
      renderCatchmentBuffers();
      renderFacilities();
      renderSolarShades('22:30');
      renderNightLighting();
      renderWheelchairNodes();
    }

    function setBasemap(style) {
      if (baseTileLayer) {
        map.removeLayer(baseTileLayer);
        baseTileLayer = null;
      }
      if (referenceTileLayer) {
        map.removeLayer(referenceTileLayer);
        referenceTileLayer = null;
      }
      currentBasemap = style;
      if (style === 'dark') {
        baseTileLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}', {
          maxNativeZoom: 16,
          maxZoom: 19,
          attribution: 'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ'
        }).addTo(map);
        referenceTileLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Reference/MapServer/tile/{z}/{y}/{x}', {
          maxNativeZoom: 16,
          maxZoom: 19,
          attribution: ''
        }).addTo(map);
      } else if (style === 'satellite') {
        baseTileLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
          maxZoom: 19,
          attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS'
        }).addTo(map);
      } else {
        baseTileLayer = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
          maxZoom: 19,
          attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);
      }
    }

    function toggleMapStyle() {
      if (currentBasemap === 'dark') {
        setBasemap('light');
      } else if (currentBasemap === 'light') {
        setBasemap('satellite');
      } else {
        setBasemap('dark');
      }
    }

    // Render Transit Network (KRL Green Line, Loop Line, MRT North-South, LRT, JakLingko)
    function renderTransitNetwork() {
      transitLayerGroup.clearLayers();

      // KRL Green Line (Rangkasbitung Line: Rawa Buntu -> Palmerah -> Tanah Abang)
      const krlGreenCoords = [
        [-6.3204, 106.6718], // Rawa Buntu
        [-6.2952, 106.7115], // Sudimara
        [-6.2844, 106.7303], // Jurang Mangu
        [-6.2750, 106.7454], // Pondok Ranji
        [-6.2374, 106.7836], // Kebayoran
        [-6.2081, 106.7972], // Palmerah
        [-6.1856, 106.8110]  // Tanah Abang
      ];
      L.polyline(krlGreenCoords, {
        color: '#10b981',
        weight: 4,
        opacity: 0.85,
        dashArray: '8, 4'
      }).bindPopup('<b>KRL Commuter Line</b><br>Rangkasbitung Line (Green Line)').addTo(transitLayerGroup);

      // KRL Loop Line (Tanah Abang -> Karet -> BNI City -> Sudirman -> Manggarai)
      const krlLoopCoords = [
        [-6.1856, 106.8110], // Tanah Abang
        [-6.2003, 106.8166], // Karet
        [-6.2018, 106.8214], // BNI City
        [-6.2024, 106.8233], // Sudirman
        [-6.2099, 106.8498]  // Manggarai
      ];
      L.polyline(krlLoopCoords, {
        color: '#3b82f6',
        weight: 4,
        opacity: 0.85
      }).bindPopup('<b>KRL Commuter Line</b><br>Cikarang / Loop Line').addTo(transitLayerGroup);

      // MRT Jakarta North-South Line (Lebak Bulus -> Fatmawati -> Blok M -> Dukuh Atas -> Bundaran HI)
      const mrtCoords = [
        [-6.2891, 106.7745], // Lebak Bulus
        [-6.2928, 106.7937], // Fatmawati
        [-6.2787, 106.7972], // Cipete
        [-6.2665, 106.7974], // Haji Nawi
        [-6.2555, 106.7975], // Blok A
        [-6.2445, 106.7981], // Blok M
        [-6.2386, 106.7988], // ASEAN / CSW
        [-6.2253, 106.8027], // Senayan
        [-6.2195, 106.8080], // Istora
        [-6.2145, 106.8184], // Benhil
        [-6.2088, 106.8219], // Setiabudi
        [-6.2014, 106.8227], // Dukuh Atas BNI
        [-6.1925, 106.8231]  // Bundaran HI
      ];
      L.polyline(mrtCoords, {
        color: '#0284c7',
        weight: 5,
        opacity: 0.95
      }).bindPopup('<b>MRT Jakarta</b><br>North-South Line (M1)').addTo(transitLayerGroup);

      // LRT Jabodebek (Dukuh Atas -> Kuningan -> Cawang)
      const lrtCoords = [
        [-6.2028, 106.8248],
        [-6.2090, 106.8296],
        [-6.2185, 106.8318],
        [-6.2307, 106.8329],
        [-6.2435, 106.8398],
        [-6.2468, 106.8643]
      ];
      L.polyline(lrtCoords, {
        color: '#f43f5e',
        weight: 4,
        opacity: 0.8
      }).bindPopup('<b>LRT Jabodebek</b><br>Dukuh Atas - Harjamukti / Jatimulya').addTo(transitLayerGroup);

      // JakLingko Mikrotrans Feeder Lines (JAK-11 Kebayoran - Tanah Abang)
      const jak11Coords = [
        [-6.2374, 106.7836], // Kebayoran
        [-6.2240, 106.7890],
        [-6.2081, 106.7972], // Palmerah
        [-6.1950, 106.8030],
        [-6.1856, 106.8110]  // Tanah Abang
      ];
      L.polyline(jak11Coords, {
        color: '#f59e0b',
        weight: 3,
        opacity: 0.75,
        dashArray: '6, 6'
      }).bindPopup('<b>JakLingko Mikrotrans JAK-11</b><br>Kebayoran Lama - Tanah Abang (Tariff: Rp 0)').addTo(transitLayerGroup);

      // Render Station Point Markers
      STATIONS.forEach(st => {
        let markerColor = '#3b82f6';
        let radius = 6;
        if (st.type === 'origin') { markerColor = '#38bdf8'; radius = 8; }
        else if (st.type === 'dest') { markerColor = '#f43f5e'; radius = 8; }
        else if (st.type === 'mrt') { markerColor = '#0284c7'; radius = 6; }
        else if (st.type === 'accessibility') { markerColor = '#ec4899'; radius = 8; }

        L.circleMarker([st.lat, st.lon], {
          radius: radius,
          fillColor: markerColor,
          color: '#ffffff',
          weight: 2,
          opacity: 1,
          fillOpacity: 0.9
        }).bindPopup(`<b>${st.name}</b><br>${st.desc}`).addTo(transitLayerGroup);
      });
    }

    // Render 500m Walkable Station Catchment Buffers
    function renderCatchmentBuffers() {
      catchmentLayerGroup.clearLayers();

      const keyStations = [
        { name: "Dukuh Atas TOD Nexus", lat: -6.2014, lon: 106.8227 },
        { name: "Stasiun KRL Kebayoran", lat: -6.2374, lon: 106.7836 },
        { name: "Stasiun KRL Rawa Buntu", lat: -6.3204, lon: 106.6718 },
        { name: "Stasiun MRT Fatmawati", lat: -6.2928, lon: 106.7937 },
        { name: "CSW / ASEAN Transit Hub", lat: -6.2386, lon: 106.7988 }
      ];

      keyStations.forEach(st => {
        // 500m Buffer Circle (approx 6-7 min walkshed)
        L.circle([st.lat, st.lon], {
          radius: 500,
          color: '#a855f7',
          weight: 1.5,
          opacity: 0.7,
          fillColor: '#a855f7',
          fillOpacity: 0.12,
          dashArray: '4, 4'
        }).bindPopup(`<b>${st.name}</b><br>500-Meter Walkable Catchment Area (6-8 mins walk)`).addTo(catchmentLayerGroup);

        // 800m Outer Catchment (10-12 mins)
        L.circle([st.lat, st.lon], {
          radius: 800,
          color: '#c084fc',
          weight: 1,
          opacity: 0.4,
          fillColor: 'transparent',
          dashArray: '3, 6'
        }).addTo(catchmentLayerGroup);
      });
    }

    // Render 235 Facilities in Dukuh Atas from GeoJSON
    function renderFacilities() {
      facilitiesLayerGroup.clearLayers();

      if (!FACILITIES_DATA || !FACILITIES_DATA.features) return;

      FACILITIES_DATA.features.forEach(f => {
        const geom = f.geometry;
        const props = f.properties || {};

        if (geom.type === 'Point') {
          const lat = geom.coordinates[1];
          const lon = geom.coordinates[0];
          const facility = props.facility || 'facility';
          let color = '#38bdf8';
          let label = props.label || props.name || 'Facility';

          if (facility === 'elevator' || label.toLowerCase().includes('lift') || label.toLowerCase().includes('elevator')) {
            color = '#10b981';
          } else if (facility === 'crossing') {
            color = '#fbbf24';
          } else if (facility === 'toilet') {
            color = '#a855f7';
          }

          L.circleMarker([lat, lon], {
            radius: 4,
            fillColor: color,
            color: '#ffffff',
            weight: 1,
            fillOpacity: 0.8
          }).bindPopup(`<b>${label}</b><br>Type: ${facility}<br>Accessible: ${props.accessible || 'Verified'}`).addTo(facilitiesLayerGroup);
        } else if (geom.type === 'LineString') {
          const latlngs = geom.coordinates.map(c => [c[1], c[0]]);
          const stroke = props.stroke || '#38bdf8';
          L.polyline(latlngs, {
            color: stroke,
            weight: props['stroke-width'] || 2,
            opacity: 0.7
          }).bindPopup(`<b>${props.name || 'Sidewalk / Path'}</b><br>Layer: ${props.layer || 'sidewalk'}`).addTo(facilitiesLayerGroup);
        }
      });
    }

    // Render CoolWalks Solar Shadows around Dukuh Atas High-Rises
    function renderSolarShades(timeStr) {
      shadeLayerGroup.clearLayers();

      let azimuth, zenith, factor;
      if (timeStr === '08:30') {
        azimuth = 75; // East-North-East
        zenith = 48;
        factor = 1.1; // Long western shadow
      } else if (timeStr === '12:00') {
        azimuth = 350;
        zenith = 82; // Almost directly overhead
        factor = 0.14; // Tiny shadow, maximum sun exposure
      } else if (timeStr === '16:30') {
        azimuth = 285; // West-North-West
        zenith = 42;
        factor = 1.25; // Long eastern shadow
      } else {
        // Night (22:30) - No solar shadows
        return;
      }

      // Convert azimuth to radians (shadow casts opposite to sun: azimuth + 180)
      const shadowAngleRad = ((azimuth + 180) % 360) * Math.PI / 180;

      DUKUH_BUILDINGS.forEach(b => {
        const shadowLenMeters = b.height * factor;
        // Convert meters to approx lat/lon offset in Jakarta (~111,000m per degree lat, ~110,500m per degree lon)
        const dLat = (shadowLenMeters * Math.cos(shadowAngleRad)) / 111000;
        const dLon = (shadowLenMeters * Math.sin(shadowAngleRad)) / 110500;

        const bLat = b.lat;
        const bLon = b.lon;
        const rLat = (b.radius / 111000);
        const rLon = (b.radius / 110500);

        // Approximate 2.5D extruded shadow polygon
        const shadowPoly = [
          [bLat - rLat, bLon - rLon],
          [bLat + rLat, bLon - rLon],
          [bLat + rLat + dLat, bLon + rLon + dLon],
          [bLat - rLat + dLat, bLon - rLon + dLon]
        ];

        L.polygon(shadowPoly, {
          color: '#1e293b',
          weight: 1,
          fillColor: '#0f172a',
          fillOpacity: 0.45
        }).bindPopup(`<b>${b.name} (${b.height}m)</b><br>CoolWalks Shadow Projection at ${timeStr}<br>Shadow Length: ${Math.round(shadowLenMeters)}m`).addTo(shadeLayerGroup);
      });
    }

    // Render Night Streetlights & Crime Hazard Zones (for 22:30 curfew)
    function renderNightLighting() {
      lightingLayerGroup.clearLayers();

      // Arterial streetlamps along Sudirman & Kebayoran
      const litSpines = [
        [[-6.2014, 106.8227], [-6.2088, 106.8219], [-6.2145, 106.8184], [-6.2253, 106.8027]],
        [[-6.2374, 106.7836], [-6.2345, 106.7820]] // Kebayoran station to Jl. Kuburan Lama
      ];

      litSpines.forEach(spine => {
        L.polyline(spine, {
          color: '#fbbf24',
          weight: 4,
          opacity: 0.6,
          dashArray: '3, 6'
        }).bindPopup('<b>Continuous Luminaire Corridor</b><br>Lighting Index: 2/2 · Active 24h Commercial Frontage').addTo(lightingLayerGroup);
      });

      // Dark Back-Alleys (Gang Tikus Hazard Zones: e.g. Gang Kebon Sayur, got without lights)
      const darkAlleys = [
        [[-6.2355, 106.7845], [-6.2335, 106.7830]],
        [[-6.2025, 106.8247], [-6.2045, 106.8270]]
      ];

      darkAlleys.forEach(alley => {
        L.polyline(alley, {
          color: '#ef4444',
          weight: 3,
          opacity: 0.8,
          dashArray: '4, 4'
        }).bindPopup('<b>⚠️ Nocturnal Hazard: Unlit Alley (Gang Tikus)</b><br>Lighting: 0/2 · Open roadside ditch (got) · High begal/mugging vulnerability').addTo(lightingLayerGroup);
      });
    }

    // Render Wheelchair Accessible Nodes & Elevators
    function renderWheelchairNodes() {
      wheelchairLayerGroup.clearLayers();

      const wheelchairNodes = [
        { name: "MRT Fatmawati Elevator A1", lat: -6.2926, lon: 106.7935, slope: "3.8%", note: "Verified step-free access from Wisma Cheshire" },
        { name: "MRT Dukuh Atas Elevator D1", lat: -6.2015, lon: 106.8226, slope: "4.2%", note: "Underground lift directly connecting concourse" },
        { name: "KRL Kebayoran Accessible Ramp", lat: -6.2372, lon: 106.7835, slope: "4.8%", note: "Skybridge to Transjakarta Corridor 13 with lift" },
        { name: "Wisma Cheshire Indonesia Ramp", lat: -6.2917, lon: 106.7952, slope: "3.5%", note: "Permanent wheelchair residential center ground-truth anchor" }
      ];

      wheelchairNodes.forEach(node => {
        L.circleMarker([node.lat, node.lon], {
          radius: 7,
          fillColor: '#10b981',
          color: '#ffffff',
          weight: 2,
          opacity: 1,
          fillOpacity: 0.95
        }).bindPopup(`<b>♿ ${node.name}</b><br>Max Ramp Slope: ${node.slope}<br>${node.note}`).addTo(wheelchairLayerGroup);
      });
    }

    // Tab Switching
    function switchTab(tabId) {
      currentTab = tabId;
      document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-tab') === tabId);
      });

      document.getElementById('tab-content-router').style.display = (tabId === 'router') ? 'flex' : 'none';
      document.getElementById('tab-content-head2head').style.display = (tabId === 'head2head') ? 'flex' : 'none';
      document.getElementById('tab-content-catchment').style.display = (tabId === 'catchment') ? 'flex' : 'none';
      document.getElementById('tab-content-pipeline').style.display = (tabId === 'pipeline') ? 'flex' : 'none';

      if (tabId === 'head2head') {
        renderHeadToHeadRoute();
      } else if (tabId === 'router') {
        renderRouteSolution();
      } else if (tabId === 'catchment') {
        map.flyTo([-6.2200, 106.8100], 13);
      } else if (tabId === 'pipeline') {
        focusStation('wisma_cheshire');
      }
    }

    // Preset Selection
    function onPresetChange(presetKey) {
      currentPreset = presetKey;
      renderRouteSolution();
    }

    // Pillar Selection
    function selectPillar(pillarKey) {
      currentPillar = pillarKey;
      document.querySelectorAll('.pillar-btn').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-pillar') === pillarKey);
      });
      document.getElementById('active-pillar-badge').innerText = pillarKey.charAt(0).toUpperCase() + pillarKey.slice(1) + ' Mode';
      renderRouteSolution();
    }

    // Time of Day Control
    function setTimeOfDay(timeStr) {
      currentTimeOfDay = timeStr;
      document.querySelectorAll('.time-pill').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-time') === timeStr);
      });
      updateMicroclimateState(timeStr);
      renderSolarShades(timeStr);
      renderRouteSolution();
    }

    function updateMicroclimateState(timeStr) {
      const hudTemp = document.getElementById('hud-temp');
      const hudUv = document.getElementById('hud-uv');
      const hudWalkCap = document.getElementById('hud-walkcap');
      const hudCurfew = document.getElementById('hud-curfew');

      if (timeStr === '08:30') {
        hudTemp.innerText = '29.2°C / 31.0°C';
        hudTemp.className = 'metric-val';
        hudUv.innerText = '4.2 (Moderate)';
        hudWalkCap.innerText = '700 m';
        hudCurfew.innerText = 'Morning Peak';
        hudCurfew.style.color = '#38bdf8';
        setBasemap('light');
      } else if (timeStr === '12:00') {
        hudTemp.innerText = '33.8°C / 35.2°C';
        hudTemp.className = 'metric-val hot';
        hudUv.innerText = '8.4 (Very High)';
        hudWalkCap.innerText = '400 m (Cap)';
        hudCurfew.innerText = 'Midday Peak';
        hudCurfew.style.color = '#f59e0b';
        setBasemap('light');
      } else if (timeStr === '16:30') {
        hudTemp.innerText = '31.5°C / 33.0°C';
        hudTemp.className = 'metric-val';
        hudUv.innerText = '2.1 (Low)';
        hudWalkCap.innerText = '650 m';
        hudCurfew.innerText = 'Evening Peak';
        hudCurfew.style.color = '#10b981';
        setBasemap('light');
      } else {
        // 22:30 Night
        hudTemp.innerText = '26.8°C / 27.5°C';
        hudTemp.className = 'metric-val cool';
        hudUv.innerText = '0.0 (Night)';
        hudWalkCap.innerText = '800 m';
        hudCurfew.innerText = 'Late Curfew';
        hudCurfew.style.color = '#fbbf24';
        setBasemap('dark');
      }
    }

    // Render Route Solution for 4-Pillar Router
    function renderRouteSolution() {
      activeRouteLayerGroup.clearLayers();
      if (simInterval) { clearInterval(simInterval); simInterval = null; }

      const presetData = ROUTE_PRESETS[currentPreset];
      if (!presetData) return;

      const solution = presetData.pillars[currentPillar] || presetData.pillars['fastest'];

      // Update KPI Cards
      document.getElementById('route-title-header').innerText = presetData.name;
      document.getElementById('route-arrival-clock').innerText = `Arrival ~${solution.arrivalTime}`;
      document.getElementById('kpi-total-time').innerText = solution.totalTime;
      document.getElementById('kpi-time-sub').innerText = solution.timeSub;
      document.getElementById('kpi-fare').innerText = solution.fare;
      document.getElementById('kpi-fare-sub').innerText = solution.fareSub;
      document.getElementById('kpi-walk-dist').innerText = solution.walkDist;
      document.getElementById('kpi-walk-time').innerText = solution.walkTime;
      document.getElementById('kpi-transit-time').innerText = solution.transitTime;
      document.getElementById('kpi-transit-sub').innerText = solution.transitSub;
      document.getElementById('kpi-comfort-score').innerText = solution.comfortScore;
      document.getElementById('kpi-comfort-sub').innerText = solution.comfortSub;
      document.getElementById('kpi-accessible-score').innerText = solution.accessibleScore;
      document.getElementById('kpi-accessible-sub').innerText = solution.accessibleSub;

      // Update Breakdown Timeline Bar
      document.getElementById('timeline-breakdown-text').innerText = solution.breakdownText;
      document.getElementById('bar-feeder').style.width = solution.barFeederPct + '%';
      document.getElementById('bar-rail').style.width = solution.barRailPct + '%';
      document.getElementById('bar-walk').style.width = solution.barWalkPct + '%';

      // Update Alert Banner
      const alertsContainer = document.getElementById('dynamic-alerts-container');
      let alertHtml = '';
      if (currentTimeOfDay === '12:00' && currentPillar !== 'cheapest') {
        alertHtml = `
          <div class="alert-banner thermal">
            <span class="alert-icon">☀️</span>
            <div><strong>Midday Solar Heat Alert (35.2°C Feels-like):</strong> Pedestrian walking segment strictly constrained to ≤ 400m; routed through shaded tree buffer and station canopies.</div>
          </div>
        `;
      } else if (currentTimeOfDay === '22:30') {
        alertHtml = `
          <div class="alert-banner night">
            <span class="alert-icon">🌙</span>
            <div><strong>Night Safety Active (22:30 WIB):</strong> Bypassed unlit alleyways; routed along illuminated commercial corridor with 24h storefronts and CCTV.</div>
          </div>
        `;
      } else if (currentPillar === 'wheelchair') {
        alertHtml = `
          <div class="alert-banner wheelchair">
            <span class="alert-icon">♿</span>
            <div><strong>Strict Step-Free Verification:</strong> 0 steps encountered. Elevators at origin & transit hubs verified online. Max cross-slope 4.8% (Permen PUPR 14/2017 compliant).</div>
          </div>
        `;
      } else {
        alertHtml = `
          <div class="alert-banner tariff">
            <span class="alert-icon">💰</span>
            <div><strong>Rupiah Tariff Optimization:</strong> Statutory integration rules applied: Rp 0 JakLingko feeder + Rp 3.000 KRL commuter fare.</div>
          </div>
        `;
      }
      alertsContainer.innerHTML = alertHtml;

      // Update Step-by-Step Directions
      const stepsContainer = document.getElementById('steps-list-container');
      document.getElementById('step-count-badge').innerText = solution.steps.length + ' Steps';
      let stepsHtml = '';
      solution.steps.forEach((st, idx) => {
        stepsHtml += `
          <div class="step-card" onclick="flyToCoord([${st.coord[0]}, ${st.coord[1]}])">
            <div class="step-num-badge">${idx + 1}</div>
            <div class="step-info">
              <div class="step-title-row">
                <span class="step-title">${st.title}</span>
                <span class="step-time-badge">${st.time}</span>
              </div>
              <div class="step-desc">${st.desc}</div>
              <div class="step-meta-row">
                <span class="step-meta-pill"><i data-lucide="footprints" style="width: 10px; height: 10px;"></i> ${st.dist}</span>
                <span class="step-meta-pill"><i data-lucide="shield" style="width: 10px; height: 10px;"></i> ${st.meta}</span>
              </div>
            </div>
          </div>
        `;
      });
      stepsContainer.innerHTML = stepsHtml;
      lucide.createIcons();

      // Render Polylines on Map
      if (solution.segments) {
        solution.segments.forEach(seg => {
          let color = '#38bdf8';
          let dash = null;
          if (seg.mode === 'rail') { color = '#6366f1'; }
          else if (seg.mode === 'walk') { color = '#10b981'; }
          else if (seg.mode === 'feeder') { color = '#38bdf8'; }

          L.polyline(seg.coords, {
            color: color,
            weight: 5,
            opacity: 0.95,
            dashArray: dash
          }).bindPopup(`<b>${seg.name}</b><br>Mode: ${seg.mode.toUpperCase()}<br>Duration: ${seg.time}`).addTo(activeRouteLayerGroup);
        });

        // Fit map bounds to route
        const allPoints = solution.segments.flatMap(s => s.coords);
        if (allPoints.length > 0) {
          map.fitBounds(allPoints, { padding: [40, 40] });
        }
      }
    }

    // Render Google Maps vs Pijak Head-to-Head on Map
    function renderHeadToHeadRoute() {
      activeRouteLayerGroup.clearLayers();
      if (simInterval) { clearInterval(simInterval); simInterval = null; }

      const h2h = ROUTE_PRESETS['preset_bsd_kebayoran'];
      const pijak = h2h.pillars['fastest'];
      const gmaps = h2h.gmaps;

      // 1. Render Google Maps Detour (Red Dashed Line)
      L.polyline(gmaps.coords, {
        color: '#ef4444',
        weight: 4,
        opacity: 0.85,
        dashArray: '8, 6'
      }).bindPopup('<b>Google Maps Navigation Failure</b><br>3h 32m to 7h 50m Detour via Kalideres / Airport Perimeter<br>47-min pitch-black alley walk').addTo(activeRouteLayerGroup);

      // 2. Render Pijak Multimodal Route (Cyan/Blue/Green Solid Lines)
      pijak.segments.forEach(seg => {
        let color = '#38bdf8';
        if (seg.mode === 'rail') color = '#6366f1';
        if (seg.mode === 'walk') color = '#10b981';

        L.polyline(seg.coords, {
          color: color,
          weight: 6,
          opacity: 0.95
        }).bindPopup(`<b>Pijak Solution: ${seg.name}</b><br>${seg.time} · ${seg.mode.toUpperCase()}`).addTo(activeRouteLayerGroup);
      });

      // Fit bounds to encompass both paths
      const allPoints = [...gmaps.coords, ...pijak.segments.flatMap(s => s.coords)];
      map.fitBounds(allPoints, { padding: [50, 50] });
    }

    // Animate Commuter Movement in Head-to-Head Simulator
    function animateHeadToHeadCommute() {
      if (simInterval) { clearInterval(simInterval); }
      simulationLayerGroup.clearLayers();

      const h2h = ROUTE_PRESETS['preset_bsd_kebayoran'];
      const pijakCoords = h2h.pillars['fastest'].segments.flatMap(s => s.coords);

      if (pijakCoords.length < 2) return;

      // Animated Marker
      simCommuterMarker = L.circleMarker(pijakCoords[0], {
        radius: 9,
        fillColor: '#38bdf8',
        color: '#ffffff',
        weight: 3,
        opacity: 1,
        fillOpacity: 1
      }).bindPopup('<b>Commuter (Pijak Multimodal)</b><br>Moving: GOP 9 BSD ➔ Stasiun Rawa Buntu ➔ KRL ➔ Kebayoran').addTo(simulationLayerGroup);

      let stepIdx = 0;
      simInterval = setInterval(() => {
        stepIdx++;
        if (stepIdx >= pijakCoords.length) {
          clearInterval(simInterval);
          simInterval = null;
          simCommuterMarker.bindPopup('<b>Arrived at Jl. Kuburan Lama!</b><br>Time elapsed: 40 mins · Fare: Rp 3.000<br>Status: Safe, lit, on-time (23:18 WIB)').openPopup();
          return;
        }
        simCommuterMarker.setLatLng(pijakCoords[stepIdx]);
      }, 250);
    }

    // Populate Walkability Gradient Table
    function loadGradientTable(data) {
      const tbody = document.getElementById('gradient-table-body');
      tbody.innerHTML = '';

      data.forEach(row => {
        const pct = parseFloat(row.sidewalk_pct) || 0;
        let fillClass = 'high';
        if (pct === 0) fillClass = 'zero';
        else if (pct < 80) fillClass = 'mid';

        const tr = document.createElement('tr');
        tr.setAttribute('data-pct', pct);
        tr.onclick = () => {
          // Fly to Sudirman area
          map.flyTo([-6.2050, 106.8220], 16);
        };

        tr.innerHTML = `
          <td><strong>${row.street_name}</strong></td>
          <td>${parseFloat(row.total_len_m).toFixed(0)}m</td>
          <td>
            <div class="pct-bar-wrapper">
              <div class="pct-bar-bg">
                <div class="pct-bar-fill ${fillClass}" style="width: ${pct}%;"></div>
              </div>
              <span style="font-size: 10px; font-weight: 600; min-width: 32px;">${pct.toFixed(0)}%</span>
            </div>
          </td>
        `;
        tbody.appendChild(tr);
      });
    }

    // Filter Gradient Table
    function filterGradientTable(filterType, elem) {
      document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
      elem.classList.add('active');

      const rows = document.querySelectorAll('#gradient-table-body tr');
      rows.forEach(r => {
        const pct = parseFloat(r.getAttribute('data-pct'));
        if (filterType === 'all') {
          r.style.display = '';
        } else if (filterType === 'high') {
          r.style.display = (pct >= 90) ? '' : 'none';
        } else if (filterType === 'mid') {
          r.style.display = (pct > 0 && pct < 90) ? '' : 'none';
        } else if (filterType === 'zero') {
          r.style.display = (pct === 0) ? '' : 'none';
        }
      });
    }

    // Quick Station Focus
    function focusStation(stationId) {
      const st = STATIONS.find(s => s.id === stationId);
      if (st) {
        map.flyTo([st.lat, st.lon], 16, { duration: 1.2 });
      }
    }

    function flyToCoord(latlng) {
      map.flyTo(latlng, 17, { duration: 0.8 });
    }

    function recenterMap() {
      if (currentTab === 'head2head') {
        renderHeadToHeadRoute();
      } else {
        renderRouteSolution();
      }
    }

    // Layer Visibility Toggles
    function toggleLayer(layerName, isVisible) {
      const mapRef = {
        'transit': transitLayerGroup,
        'catchment': catchmentLayerGroup,
        'facilities': facilitiesLayerGroup,
        'shade': shadeLayerGroup,
        'lighting': lightingLayerGroup,
        'wheelchair': wheelchairLayerGroup
      };

      const grp = mapRef[layerName];
      if (grp) {
        if (isVisible) {
          map.addLayer(grp);
        } else {
          map.removeLayer(grp);
        }
      }
    }
  </script>
</body>
</html>
"""

# Let's define the comprehensive stations catalog
stations_data = [
    {"id": "binus_bsd", "name": "Apple Developer Academy @ BINUS (BSD)", "type": "origin", "lat": -6.3023, "lon": 106.6522, "desc": "Campus pick-up bay at Green Office Park 9 (GOP 9)"},
    {"id": "rawa_buntu", "name": "Stasiun KRL Rawa Buntu", "type": "rail", "lat": -6.3204, "lon": 106.6718, "desc": "KRL Commuter Line Green Line (Rangkasbitung Line)"},
    {"id": "sudimara", "name": "Stasiun KRL Sudimara", "type": "rail", "lat": -6.2952, "lon": 106.7115, "desc": "KRL Commuter Line Green Line"},
    {"id": "jurang_mangu", "name": "Stasiun KRL Jurang Mangu", "type": "rail", "lat": -6.2844, "lon": 106.7303, "desc": "Bintaro Xchange Transit Hub"},
    {"id": "pondok_ranji", "name": "Stasiun KRL Pondok Ranji", "type": "rail", "lat": -6.2750, "lon": 106.7454, "desc": "KRL Commuter Line Green Line"},
    {"id": "kebayoran", "name": "Stasiun KRL Kebayoran", "type": "rail", "lat": -6.2374, "lon": 106.7836, "desc": "Skybridge connection to Transjakarta Corridor 13 (Velbak / CSW)"},
    {"id": "palmerah", "name": "Stasiun KRL Palmerah", "type": "rail", "lat": -6.2081, "lon": 106.7972, "desc": "KRL Green Line station near DPR/MPR & Gelora"},
    {"id": "tanah_abang", "name": "Stasiun KRL Tanah Abang", "type": "rail", "lat": -6.1856, "lon": 106.8110, "desc": "Major Commuter Line Interchange (Green & Loop Line)"},
    {"id": "kuburan_lama", "name": "Jl. Kuburan Lama (Palmerah / Kebayoran)", "type": "dest", "lat": -6.2345, "lon": 106.7820, "desc": "Destination residential zone off Jl. Kebayoran Lama corridor"},
    {"id": "dukuh_atas_mrt", "name": "Stasiun MRT Dukuh Atas BNI", "type": "mrt", "lat": -6.2014, "lon": 106.8227, "desc": "Multimodal TOD Spine, North-South Line"},
    {"id": "sudirman_krl", "name": "Stasiun KRL Sudirman", "type": "rail", "lat": -6.2024, "lon": 106.8233, "desc": "KRL Loop & Cikarang Line trunk"},
    {"id": "bni_city", "name": "Stasiun BNI City", "type": "rail", "lat": -6.2018, "lon": 106.8214, "desc": "Soekarno-Hatta Airport Rail Link (Basoetta)"},
    {"id": "dukuh_atas_lrt", "name": "Stasiun LRT Dukuh Atas", "type": "lrt", "lat": -6.2028, "lon": 106.8248, "desc": "LRT Jabodebek Cibubur & Bekasi Lines terminus"},
    {"id": "bundaran_hi", "name": "Stasiun MRT Bundaran HI", "type": "mrt", "lat": -6.1925, "lon": 106.8231, "desc": "North terminus of MRT Line 1"},
    {"id": "setiabudi_astra", "name": "Stasiun MRT Setiabudi Astra", "type": "mrt", "lat": -6.2088, "lon": 106.8219, "desc": "MRT North-South Line"},
    {"id": "bendungan_hilir", "name": "Stasiun MRT Bendungan Hilir", "type": "mrt", "lat": -6.2145, "lon": 106.8184, "desc": "MRT North-South Line"},
    {"id": "istora_mandiri", "name": "Stasiun MRT Istora Mandiri", "type": "mrt", "lat": -6.2195, "lon": 106.8080, "desc": "Gelora Bung Karno East Gate"},
    {"id": "senayan_mrt", "name": "Stasiun MRT Senayan", "type": "mrt", "lat": -6.2253, "lon": 106.8027, "desc": "Senayan commercial and sports center"},
    {"id": "csw_asean", "name": "CSW / ASEAN Multimodal Interchange", "type": "mrt", "lat": -6.2386, "lon": 106.7988, "desc": "Iconic 5-level interchange: MRT ASEAN + TJ Corridor 1 & 13"},
    {"id": "blok_m", "name": "Stasiun MRT Blok M BCA", "type": "mrt", "lat": -6.2445, "lon": 106.7981, "desc": "Major transit hub with integrated bus terminal"},
    {"id": "fatmawati", "name": "Stasiun MRT Fatmawati Indomaret", "type": "mrt", "lat": -6.2928, "lon": 106.7937, "desc": "Elevated MRT station with accessible lifts and tactile paths"},
    {"id": "lebak_bulus", "name": "Stasiun MRT Lebak Bulus Grab", "type": "mrt", "lat": -6.2891, "lon": 106.7745, "desc": "South terminal & depot of MRT North-South Line"},
    {"id": "wisma_cheshire", "name": "Wisma Cheshire Indonesia", "type": "accessibility", "lat": -6.2917, "lon": 106.7952, "desc": "Residential home for persons with severe physical disabilities (320m from MRT Fatmawati)"}
]

# Presets and 4 Pillars Definition
presets_data = {
    "preset_bsd_kebayoran": {
        "name": "Apple Dev Academy (BSD) ➔ Jl. Kuburan Lama (Kebayoran)",
        "gmaps": {
            "coords": [
                [-6.3023, 106.6522], # BSD GOP 9
                [-6.2800, 106.6600], # Tol Serpong
                [-6.2400, 106.6700], # Tol Kunciran
                [-6.1900, 106.6800], # Towards Kalideres
                [-6.1550, 106.7050], # Kalideres Detour
                [-6.1580, 106.7400], # Daan Mogot
                [-6.1650, 106.7700], # Grogol
                [-6.1900, 106.7900], # Tomang
                [-6.2081, 106.7972], # Palmerah
                [-6.2200, 106.7900], # Dark alleyways
                [-6.2345, 106.7820]  # Jl. Kuburan Lama
            ]
        },
        "pillars": {
            "fastest": {
                "arrivalTime": "23:18 WIB",
                "totalTime": "40 min",
                "timeSub": "vs 1h 48m transit",
                "fare": "Rp 3.000",
                "fareSub": "Saves Rp 79.000",
                "walkDist": "550 m",
                "walkTime": "8 min walk",
                "transitTime": "32 min",
                "transitSub": "KRL + Feeder",
                "comfortScore": "88%",
                "comfortSub": "Lit & Sheltered",
                "accessibleScore": "100%",
                "accessibleSub": "0 Steps",
                "breakdownText": "Feeder (6m) · Rail (26m) · Walk (8m)",
                "barFeederPct": 15,
                "barRailPct": 65,
                "barWalkPct": 20,
                "steps": [
                    {"title": "Depart Apple Developer Academy @ BINUS", "time": "22:30 WIB", "desc": "Walk 50m to Green Office Park 9 (GOP 9) multimodal pickup bay.", "dist": "50m", "meta": "Lit Campus Bay", "coord": [-6.3023, 106.6522]},
                    {"title": "Board Micro-Feeder / Ojol to Stn. Rawa Buntu", "time": "22:32 WIB", "desc": "Transit connector via Jl. BSD Grand Boulevard directly to Stasiun Rawa Buntu North Gate.", "dist": "3.2 km", "meta": "In-vehicle (6 min)", "coord": [-6.3120, 106.6620]},
                    {"title": "Tap In at Stasiun KRL Rawa Buntu", "time": "22:39 WIB", "desc": "Tap in at fare gates (Platform 1, Direction Tanah Abang). Synchronized transfer.", "dist": "30m", "meta": "Fare: Rp 3.000", "coord": [-6.3204, 106.6718]},
                    {"title": "Board KRL Commuter Line (Green Line)", "time": "22:42 WIB", "desc": "Ride 4 intermediate stops: Sudimara, Jurang Mangu, Pondok Ranji to Stasiun Kebayoran.", "dist": "16.5 km", "meta": "Air-conditioned (26 min)", "coord": [-6.2750, 106.7454]},
                    {"title": "Alight at Stasiun Kebayoran & Walk to Destination", "time": "23:10 WIB", "desc": "Exit North concourse; walk 550m along illuminated sidewalk on Jl. Kebayoran Lama to Jl. Kuburan Lama.", "dist": "550m", "meta": "Lighting 2/2 · 0 steps", "coord": [-6.2345, 106.7820]}
                ],
                "segments": [
                    {"name": "Campus Feeder / Ojol", "mode": "feeder", "time": "6 min", "coords": [[-6.3023, 106.6522], [-6.3080, 106.6580], [-6.3150, 106.6650], [-6.3204, 106.6718]]},
                    {"name": "KRL Commuter Line", "mode": "rail", "time": "26 min", "coords": [[-6.3204, 106.6718], [-6.2952, 106.7115], [-6.2844, 106.7303], [-6.2750, 106.7454], [-6.2374, 106.7836]]},
                    {"name": "Illuminated Last-Mile Walk", "mode": "walk", "time": "8 min", "coords": [[-6.2374, 106.7836], [-6.2360, 106.7830], [-6.2345, 106.7820]]}
                ]
            },
            "comfort": {
                "arrivalTime": "23:22 WIB",
                "totalTime": "44 min",
                "timeSub": "Prioritizes Safety",
                "fare": "Rp 3.000",
                "fareSub": "Statutory Tariff",
                "walkDist": "580 m",
                "walkTime": "9 min walk",
                "transitTime": "35 min",
                "transitSub": "Feeder + AC Rail",
                "comfortScore": "96%",
                "comfortSub": "100% Streetlamps",
                "accessibleScore": "100%",
                "accessibleSub": "0 Steps",
                "breakdownText": "Shuttle (8m) · Rail (27m) · Protected Walk (9m)",
                "barFeederPct": 18,
                "barRailPct": 62,
                "barWalkPct": 20,
                "steps": [
                    {"title": "GOP 9 Air-Conditioned Shuttle Pick-up", "time": "22:30 WIB", "desc": "Board protected shuttle at GOP 9 lobby directly to Rawa Buntu.", "dist": "3.2 km", "meta": "Comfortable AC", "coord": [-6.3023, 106.6522]},
                    {"title": "Platform Boarding at Stasiun Rawa Buntu", "time": "22:40 WIB", "desc": "Enter via accessible ramp; board quiet carriage.", "dist": "40m", "meta": "Protected Waiting Area", "coord": [-6.3204, 106.6718]},
                    {"title": "KRL Commuter Line to Kebayoran", "time": "22:44 WIB", "desc": "Smooth rail journey with CCTV surveillance throughout.", "dist": "16.5 km", "meta": "26 min", "coord": [-6.2750, 106.7454]},
                    {"title": "Protected Night Walk via Main Arterial", "time": "23:13 WIB", "desc": "Bypasses dark Gang Kebon Sayur. Uses 100% lit commercial frontage with active warung Makan.", "dist": "580m", "meta": "Eyes on the Street", "coord": [-6.2345, 106.7820]}
                ],
                "segments": [
                    {"name": "BSD Shuttle", "mode": "feeder", "time": "8 min", "coords": [[-6.3023, 106.6522], [-6.3080, 106.6580], [-6.3150, 106.6650], [-6.3204, 106.6718]]},
                    {"name": "KRL Rail Trunk", "mode": "rail", "time": "26 min", "coords": [[-6.3204, 106.6718], [-6.2952, 106.7115], [-6.2844, 106.7303], [-6.2750, 106.7454], [-6.2374, 106.7836]]},
                    {"name": "Lit Commercial Corridor Walk", "mode": "walk", "time": "9 min", "coords": [[-6.2374, 106.7836], [-6.2365, 106.7832], [-6.2355, 106.7828], [-6.2345, 106.7820]]}
                ]
            },
            "cheapest": {
                "arrivalTime": "23:26 WIB",
                "totalTime": "46 min",
                "timeSub": "Maximum Savings",
                "fare": "Rp 3.000",
                "fareSub": "96% vs Taxi (Rp 92k)",
                "walkDist": "600 m",
                "walkTime": "9 min walk",
                "transitTime": "37 min",
                "transitSub": "JakLingko + KRL",
                "comfortScore": "84%",
                "comfortSub": "Integrated Fare",
                "accessibleScore": "95%",
                "accessibleSub": "Low Floor Feeder",
                "breakdownText": "Free Shuttle (10m) · KRL Rail (27m) · Walk (9m)",
                "barFeederPct": 22,
                "barRailPct": 58,
                "barWalkPct": 20,
                "steps": [
                    {"title": "Board Free Campus Shuttle to Rawa Buntu", "time": "22:30 WIB", "desc": "Zero-fare student connector to Stasiun Rawa Buntu.", "dist": "3.2 km", "meta": "Fare: Rp 0", "coord": [-6.3023, 106.6522]},
                    {"title": "KRL Commuter Line Trunk", "time": "22:42 WIB", "desc": "Standard statutory distance fare (first 25 km is flat Rp 3.000).", "dist": "16.5 km", "meta": "Fare: Rp 3.000", "coord": [-6.2750, 106.7454]},
                    {"title": "Walk or JakLingko JAK-11 to Destination", "time": "23:12 WIB", "desc": "Direct walk along sidewalk (Rp 0).", "dist": "600m", "meta": "Fare: Rp 0", "coord": [-6.2345, 106.7820]}
                ],
                "segments": [
                    {"name": "Campus Shuttle", "mode": "feeder", "time": "10 min", "coords": [[-6.3023, 106.6522], [-6.3080, 106.6580], [-6.3150, 106.6650], [-6.3204, 106.6718]]},
                    {"name": "KRL Commuter Line", "mode": "rail", "time": "26 min", "coords": [[-6.3204, 106.6718], [-6.2952, 106.7115], [-6.2844, 106.7303], [-6.2750, 106.7454], [-6.2374, 106.7836]]},
                    {"name": "Pedestrian Walk", "mode": "walk", "time": "9 min", "coords": [[-6.2374, 106.7836], [-6.2360, 106.7830], [-6.2345, 106.7820]]}
                ]
            },
            "wheelchair": {
                "arrivalTime": "23:28 WIB",
                "totalTime": "48 min",
                "timeSub": "100% Step-Free",
                "fare": "Rp 3.000",
                "fareSub": "Statutory Fare",
                "walkDist": "580 m",
                "walkTime": "12 min roll",
                "transitTime": "36 min",
                "transitSub": "Accessible WAV + Rail",
                "comfortScore": "92%",
                "comfortSub": "Tactile & Ramps",
                "accessibleScore": "100%",
                "accessibleSub": "0 Steps · Elevators OK",
                "breakdownText": "Accessible WAV (8m) · Accessible KRL (28m) · Ramp Roll (12m)",
                "barFeederPct": 17,
                "barRailPct": 58,
                "barWalkPct": 25,
                "steps": [
                    {"title": "GOP 9 Accessible Pick-up Bay", "time": "22:30 WIB", "desc": "Flush curb-cut roll onto accessible WAV feeder.", "dist": "30m", "meta": "Slope 3.5%", "coord": [-6.3023, 106.6522]},
                    {"title": "Rawa Buntu Station Elevator", "time": "22:40 WIB", "desc": "Street-to-concourse lift to Platform 1. Platform gap < 3cm.", "dist": "50m", "meta": "Operational Lift", "coord": [-6.3204, 106.6718]},
                    {"title": "Accessible Carriage KRL", "time": "22:45 WIB", "desc": "Carriage 4 with designated wheelchair securement bays.", "dist": "16.5 km", "meta": "Dedicated Bay", "coord": [-6.2750, 106.7454]},
                    {"title": "Stasiun Kebayoran North Lift & Ramp Concourse", "time": "23:14 WIB", "desc": "Platform lift to street level. Continuous 1.8m wide sidewalk with drop-curbs to Jl. Kuburan Lama.", "dist": "580m", "meta": "0 Steps · Slope 4.5%", "coord": [-6.2345, 106.7820]}
                ],
                "segments": [
                    {"name": "WAV Feeder", "mode": "feeder", "time": "8 min", "coords": [[-6.3023, 106.6522], [-6.3080, 106.6580], [-6.3150, 106.6650], [-6.3204, 106.6718]]},
                    {"name": "Accessible KRL Line", "mode": "rail", "time": "26 min", "coords": [[-6.3204, 106.6718], [-6.2952, 106.7115], [-6.2844, 106.7303], [-6.2750, 106.7454], [-6.2374, 106.7836]]},
                    {"name": "Step-Free Ramp Roll", "mode": "walk", "time": "12 min", "coords": [[-6.2374, 106.7836], [-6.2360, 106.7830], [-6.2345, 106.7820]]}
                ]
            }
        }
    },

    "preset_dukuh_senayan": {
        "name": "Dukuh Atas Multimodal TOD ➔ Gelora Bung Karno / MRT Senayan",
        "pillars": {
            "fastest": {
                "arrivalTime": "12:12 PM",
                "totalTime": "12 min",
                "timeSub": "Direct MRT Trunk",
                "fare": "Rp 6.000",
                "fareSub": "MRT Fare",
                "walkDist": "380 m",
                "walkTime": "5 min walk",
                "transitTime": "7 min",
                "transitSub": "MRT Line 1",
                "comfortScore": "89%",
                "comfortSub": "Canopy Shaded",
                "accessibleScore": "100%",
                "accessibleSub": "0 Steps",
                "breakdownText": "MRT (7m) · Canopy Walk (5m)",
                "barFeederPct": 0,
                "barRailPct": 60,
                "barWalkPct": 40,
                "steps": [
                    {"title": "Enter MRT Dukuh Atas BNI Station", "time": "12:00 PM", "desc": "Descend via Terowongan Kendal covered canopy entrance to underground concourse.", "dist": "80m", "meta": "Shaded Canopy", "coord": [-6.2014, 106.8227]},
                    {"title": "Board MRT Jakarta North-South Line", "time": "12:03 PM", "desc": "Travel 3 stops: Setiabudi Astra, Bendungan Hilir, Istora Mandiri to Senayan.", "dist": "3.8 km", "meta": "7 min underground", "coord": [-6.2145, 106.8184]},
                    {"title": "Alight at MRT Senayan & Walk to GBK", "time": "12:10 PM", "desc": "Exit Gate B; walk along landscaped tree buffer on Jl. Jend. Sudirman to GBK North Gate.", "dist": "300m", "meta": "Tree Shaded", "coord": [-6.2253, 106.8027]}
                ],
                "segments": [
                    {"name": "MRT Jakarta", "mode": "rail", "time": "7 min", "coords": [[-6.2014, 106.8227], [-6.2088, 106.8219], [-6.2145, 106.8184], [-6.2195, 106.8080], [-6.2253, 106.8027]]},
                    {"name": "GBK Tree-Buffered Walk", "mode": "walk", "time": "5 min", "coords": [[-6.2253, 106.8027], [-6.2230, 106.8035], [-6.2210, 106.8040]]}
                ]
            },
            "comfort": {
                "arrivalTime": "12:15 PM",
                "totalTime": "15 min",
                "timeSub": "Max Thermal Shade",
                "fare": "Rp 6.000",
                "fareSub": "MRT Fare",
                "walkDist": "320 m",
                "walkTime": "5 min walk",
                "transitTime": "10 min",
                "transitSub": "Air-Conditioned",
                "comfortScore": "95%",
                "comfortSub": "88% Shade Ratio",
                "accessibleScore": "100%",
                "accessibleSub": "0 Steps",
                "breakdownText": "MRT (7m) · Covered Walk (5m)",
                "barFeederPct": 0,
                "barRailPct": 60,
                "barWalkPct": 40,
                "steps": [
                    {"title": "Terowongan Kendal Shaded Walkway", "time": "12:00 PM", "desc": "100% solar shade through pedestrianized tunnel directly into MRT station.", "dist": "120m", "meta": "0% Sun Exposure", "coord": [-6.2014, 106.8227]},
                    {"title": "MRT Jakarta Air-Conditioned Carriage", "time": "12:04 PM", "desc": "Fast air-conditioned rail to MRT Senayan.", "dist": "3.8 km", "meta": "Temp 22°C", "coord": [-6.2145, 106.8184]},
                    {"title": "Covered Walk to Gelora Bung Karno", "time": "12:11 PM", "desc": "Walk strictly beneath mature mahogany tree canopies. Ambient feels-like reduced from 35.2°C to 29.5°C.", "dist": "200m", "meta": "Thermal Cap Respected", "coord": [-6.2253, 106.8027]}
                ],
                "segments": [
                    {"name": "MRT Jakarta Line", "mode": "rail", "time": "7 min", "coords": [[-6.2014, 106.8227], [-6.2088, 106.8219], [-6.2145, 106.8184], [-6.2195, 106.8080], [-6.2253, 106.8027]]},
                    {"name": "Shaded Forest Walkway", "mode": "walk", "time": "5 min", "coords": [[-6.2253, 106.8027], [-6.2230, 106.8035], [-6.2210, 106.8040]]}
                ]
            },
            "cheapest": {
                "arrivalTime": "12:18 PM",
                "totalTime": "18 min",
                "timeSub": "BRT Integration",
                "fare": "Rp 3.500",
                "fareSub": "42% vs MRT (Rp 6k)",
                "walkDist": "390 m",
                "walkTime": "6 min walk",
                "transitTime": "12 min",
                "transitSub": "Transjakarta BRT",
                "comfortScore": "82%",
                "comfortSub": "Dedicated Busway",
                "accessibleScore": "90%",
                "accessibleSub": "Station Ramps",
                "breakdownText": "Transjakarta (12m) · Walk (6m)",
                "barFeederPct": 0,
                "barRailPct": 70,
                "barWalkPct": 30,
                "steps": [
                    {"title": "Board Transjakarta Corridor 1 (Blok M - Kota)", "time": "12:00 PM", "desc": "Halte Dukuh Atas 1 directly onto dedicated BRT lane.", "dist": "50m", "meta": "Fare: Rp 3.500", "coord": [-6.2018, 106.8228]},
                    {"title": "Transjakarta BRT to Halte GBK", "time": "12:05 PM", "desc": "4 stops along Sudirman busway corridor.", "dist": "3.5 km", "meta": "12 min", "coord": [-6.2145, 106.8184]},
                    {"title": "Alight at Halte GBK & Cross via JPO Ramp", "time": "12:15 PM", "desc": "Gentle ramped pedestrian overpass to GBK gates.", "dist": "340m", "meta": "Ramp Slope 6.2%", "coord": [-6.2210, 106.8040]}
                ],
                "segments": [
                    {"name": "Transjakarta Corridor 1", "mode": "rail", "time": "12 min", "coords": [[-6.2018, 106.8228], [-6.2088, 106.8219], [-6.2145, 106.8184], [-6.2195, 106.8080], [-6.2210, 106.8040]]},
                    {"name": "GBK Concourse Walk", "mode": "walk", "time": "6 min", "coords": [[-6.2210, 106.8040], [-6.2200, 106.8050]]}
                ]
            },
            "wheelchair": {
                "arrivalTime": "12:14 PM",
                "totalTime": "14 min",
                "timeSub": "100% Step-Free",
                "fare": "Rp 6.000",
                "fareSub": "MRT Fare",
                "walkDist": "350 m",
                "walkTime": "6 min roll",
                "transitTime": "8 min",
                "transitSub": "Dual Elevators",
                "comfortScore": "94%",
                "comfortSub": "Permen PUPR 14/2017",
                "accessibleScore": "100%",
                "accessibleSub": "0 Steps",
                "breakdownText": "MRT Lift (2m) · Train (6m) · Concourse Ramp (6m)",
                "barFeederPct": 0,
                "barRailPct": 55,
                "barWalkPct": 45,
                "steps": [
                    {"title": "Dukuh Atas Street Lift Entrance D1", "time": "12:00 PM", "desc": "Direct elevator to ticket hall and platform. Level boarding.", "dist": "40m", "meta": "Elevator D1 Verified", "coord": [-6.2014, 106.8227]},
                    {"title": "MRT North-South Train", "time": "12:03 PM", "desc": "Board designated wheelchair carriage with platform gap < 3cm.", "dist": "3.8 km", "meta": "6 min", "coord": [-6.2145, 106.8184]},
                    {"title": "MRT Senayan Lift to GBK Surface", "time": "12:09 PM", "desc": "Take Lift B to surface level. Roll along 2.4m wide tactile-paved walkway with flush curb-cuts to GBK gate.", "dist": "310m", "meta": "Slope 3.8% · 0 Steps", "coord": [-6.2253, 106.8027]}
                ],
                "segments": [
                    {"name": "MRT Jakarta", "mode": "rail", "time": "6 min", "coords": [[-6.2014, 106.8227], [-6.2088, 106.8219], [-6.2145, 106.8184], [-6.2195, 106.8080], [-6.2253, 106.8027]]},
                    {"name": "Flush Sidewalk Roll", "mode": "walk", "time": "6 min", "coords": [[-6.2253, 106.8027], [-6.2230, 106.8035], [-6.2210, 106.8040]]}
                ]
            }
        }
    },

    "preset_wisma_cheshire": {
        "name": "Wisma Cheshire (Cilandak) ➔ Dukuh Atas TOD Nexus [Wheelchair]",
        "pillars": {
            "fastest": {
                "arrivalTime": "10:32 AM",
                "totalTime": "32 min",
                "timeSub": "Direct MRT Trunk",
                "fare": "Rp 11.000",
                "fareSub": "MRT Standard",
                "walkDist": "450 m",
                "walkTime": "9 min roll",
                "transitTime": "23 min",
                "transitSub": "MRT Line 1",
                "comfortScore": "94%",
                "comfortSub": "Step-Free Verified",
                "accessibleScore": "100%",
                "accessibleSub": "0 Steps",
                "breakdownText": "Sidewalk Roll (6m) · MRT Trunk (23m) · TOD Ramp (3m)",
                "barFeederPct": 0,
                "barRailPct": 75,
                "barWalkPct": 25,
                "steps": [
                    {"title": "Roll from Wisma Cheshire Indonesia", "time": "10:00 AM", "desc": "Exit residential gate on Jl. Wijaya Kusuma; continuous paved sidewalk with 1.6m clearance.", "dist": "320m", "meta": "Slope 3.5%", "coord": [-6.2917, 106.7952]},
                    {"title": "Enter MRT Fatmawati Station Entrance A", "time": "10:06 AM", "desc": "Street-to-concourse Lift A1, followed by Concourse-to-platform Lift A2.", "dist": "50m", "meta": "Lifts Verified Online", "coord": [-6.2928, 106.7937]},
                    {"title": "Board MRT Jakarta North-South Line", "time": "10:09 AM", "desc": "Ride 8 stations: Cipete, Haji Nawi, Blok A, Blok M, ASEAN, Senayan, Istora, Benhil to Dukuh Atas.", "dist": "11.2 km", "meta": "21 min transit", "coord": [-6.2445, 106.7981]},
                    {"title": "Alight at MRT Dukuh Atas BNI", "time": "10:30 AM", "desc": "Take Elevator D1 to underground concourse; roll up ramp to JPM Dukuh Atas multi-transit hub.", "dist": "80m", "meta": "Slope 4.8% · 0 Steps", "coord": [-6.2014, 106.8227]}
                ],
                "segments": [
                    {"name": "Jl. Wijaya Kusuma Sidewalk", "mode": "walk", "time": "6 min", "coords": [[-6.2917, 106.7952], [-6.2922, 106.7942], [-6.2928, 106.7937]]},
                    {"name": "MRT Jakarta Trunk", "mode": "rail", "time": "21 min", "coords": [[-6.2928, 106.7937], [-6.2787, 106.7972], [-6.2555, 106.7975], [-6.2445, 106.7981], [-6.2386, 106.7988], [-6.2253, 106.8027], [-6.2145, 106.8184], [-6.2014, 106.8227]]},
                    {"name": "JPM Transit Ramp", "mode": "walk", "time": "3 min", "coords": [[-6.2014, 106.8227], [-6.2020, 106.8235]]}
                ]
            },
            "comfort": {
                "arrivalTime": "10:35 AM",
                "totalTime": "35 min",
                "timeSub": "Max Comfort",
                "fare": "Rp 11.000",
                "fareSub": "MRT Standard",
                "walkDist": "450 m",
                "walkTime": "9 min roll",
                "transitTime": "26 min",
                "transitSub": "Air-Conditioned",
                "comfortScore": "97%",
                "comfortSub": "Continuous Canopy",
                "accessibleScore": "100%",
                "accessibleSub": "0 Steps",
                "breakdownText": "Sidewalk (6m) · MRT Trunk (23m) · Canopy (6m)",
                "barFeederPct": 0,
                "barRailPct": 70,
                "barWalkPct": 30,
                "steps": [
                    {"title": "Paved Roll from Wisma Cheshire", "time": "10:00 AM", "desc": "Tree-shaded route along residential corridor to MRT Fatmawati.", "dist": "320m", "meta": "Shaded 82%", "coord": [-6.2917, 106.7952]},
                    {"title": "MRT Fatmawati Dual Elevators", "time": "10:06 AM", "desc": "Protected lift lobby into air-conditioned concourse.", "dist": "50m", "meta": "Lifts OK", "coord": [-6.2928, 106.7937]},
                    {"title": "MRT Jakarta Transit", "time": "10:09 AM", "desc": "Smooth carriage ride with wheelchair docking points.", "dist": "11.2 km", "meta": "21 min", "coord": [-6.2445, 106.7981]},
                    {"title": "Arrive Dukuh Atas TOD Interchange", "time": "10:32 AM", "desc": "Step-free connection through Terowongan Kendal to Sudirman KRL and LRT.", "dist": "80m", "meta": "100% Covered", "coord": [-6.2014, 106.8227]}
                ],
                "segments": [
                    {"name": "Tree Shaded Roll", "mode": "walk", "time": "6 min", "coords": [[-6.2917, 106.7952], [-6.2922, 106.7942], [-6.2928, 106.7937]]},
                    {"name": "MRT Rail Line", "mode": "rail", "time": "21 min", "coords": [[-6.2928, 106.7937], [-6.2787, 106.7972], [-6.2555, 106.7975], [-6.2445, 106.7981], [-6.2386, 106.7988], [-6.2253, 106.8027], [-6.2145, 106.8184], [-6.2014, 106.8227]]},
                    {"name": "Covered Interchange", "mode": "walk", "time": "6 min", "coords": [[-6.2014, 106.8227], [-6.2020, 106.8235]]}
                ]
            },
            "cheapest": {
                "arrivalTime": "10:48 AM",
                "totalTime": "48 min",
                "timeSub": "Transjakarta Bus",
                "fare": "Rp 3.500",
                "fareSub": "68% vs MRT (Rp 11k)",
                "walkDist": "520 m",
                "walkTime": "11 min roll",
                "transitTime": "37 min",
                "transitSub": "Low-Floor BRT",
                "comfortScore": "80%",
                "comfortSub": "Ramped Busway",
                "accessibleScore": "92%",
                "accessibleSub": "Low Floor Bus",
                "breakdownText": "Roll to Halte (7m) · Low Floor Bus (37m) · TOD Roll (4m)",
                "barFeederPct": 0,
                "barRailPct": 75,
                "barWalkPct": 25,
                "steps": [
                    {"title": "Roll from Wisma Cheshire to Halte RS Fatmawati", "time": "10:00 AM", "desc": "Roll to Transjakarta low-floor bus stop on Jl. RS Fatmawati.", "dist": "380m", "meta": "Sidewalk Paved", "coord": [-6.2917, 106.7952]},
                    {"title": "Board Transjakarta 1E (Pondok Labu - Blok M)", "time": "10:08 AM", "desc": "Low-floor bus with fold-out wheelchair boarding ramp. Flat fare.", "dist": "6.8 km", "meta": "Fare: Rp 3.500", "coord": [-6.2787, 106.7972]},
                    {"title": "Transfer to Corridor 1 at Blok M Hub to Dukuh Atas", "time": "10:28 AM", "desc": "Free within-station transfer to Corridor 1 directly to Halte Dukuh Atas 1.", "dist": "5.2 km", "meta": "Free Transfer (Rp 0)", "coord": [-6.2253, 106.8027]},
                    {"title": "Exit Halte Dukuh Atas via Ramp", "time": "10:45 AM", "desc": "Gentle ramped skybridge to Dukuh Atas pedestrian concourse.", "dist": "140m", "meta": "Slope 5.8%", "coord": [-6.2014, 106.8227]}
                ],
                "segments": [
                    {"name": "Sidewalk Roll", "mode": "walk", "time": "7 min", "coords": [[-6.2917, 106.7952], [-6.2922, 106.7942], [-6.2928, 106.7937]]},
                    {"name": "Transjakarta Busway", "mode": "rail", "time": "37 min", "coords": [[-6.2928, 106.7937], [-6.2445, 106.7981], [-6.2014, 106.8227]]},
                    {"name": "TOD Skybridge Roll", "mode": "walk", "time": "4 min", "coords": [[-6.2014, 106.8227], [-6.2020, 106.8235]]}
                ]
            },
            "wheelchair": {
                "arrivalTime": "10:32 AM",
                "totalTime": "32 min",
                "timeSub": "100% Step-Free Verified",
                "fare": "Rp 11.000",
                "fareSub": "MRT Standard",
                "walkDist": "450 m",
                "walkTime": "9 min roll",
                "transitTime": "23 min",
                "transitSub": "Dual Elevators OK",
                "comfortScore": "98%",
                "comfortSub": "Permen PUPR 14/2017",
                "accessibleScore": "100%",
                "accessibleSub": "0 Steps Encountered",
                "breakdownText": "Sidewalk Roll (6m) · MRT Trunk (23m) · TOD Ramp (3m)",
                "barFeederPct": 0,
                "barRailPct": 75,
                "barWalkPct": 25,
                "steps": [
                    {"title": "Wisma Cheshire Ramp Departure", "time": "10:00 AM", "desc": "Step-free ramp descent (slope 3.5%) onto Jl. Wijaya Kusuma. No open gutters.", "dist": "320m", "meta": "Permen PUPR Compliant", "coord": [-6.2917, 106.7952]},
                    {"title": "MRT Fatmawati Station Lift A1 & A2", "time": "10:06 AM", "desc": "Elevator door width 1.1m (exceeds 0.9m standard). Audible and braille floor buttons.", "dist": "50m", "meta": "100% Functional", "coord": [-6.2928, 106.7937]},
                    {"title": "Dedicated Accessible MRT Train Car", "time": "10:09 AM", "desc": "Automatic level platform boarding; platform horizontal gap < 3cm, vertical gap < 1.5cm.", "dist": "11.2 km", "meta": "Wheelchair Anchor Bay", "coord": [-6.2445, 106.7981]},
                    {"title": "Dukuh Atas BNI Lift D1 to JPM Concourse", "time": "10:30 AM", "desc": "Direct underground lift into JPM Dukuh Atas multimodal hub. 0 steps encountered throughout journey.", "dist": "80m", "meta": "0 Steps Total", "coord": [-6.2014, 106.8227]}
                ],
                "segments": [
                    {"name": "Accessible Sidewalk", "mode": "walk", "time": "6 min", "coords": [[-6.2917, 106.7952], [-6.2922, 106.7942], [-6.2928, 106.7937]]},
                    {"name": "Level-Boarding MRT", "mode": "rail", "time": "21 min", "coords": [[-6.2928, 106.7937], [-6.2787, 106.7972], [-6.2555, 106.7975], [-6.2445, 106.7981], [-6.2386, 106.7988], [-6.2253, 106.8027], [-6.2145, 106.8184], [-6.2014, 106.8227]]},
                    {"name": "TOD Multi-Level Ramp", "mode": "walk", "time": "3 min", "coords": [[-6.2014, 106.8227], [-6.2020, 106.8235]]}
                ]
            }
        }
    },

    "preset_rawabuntu_palmerah": {
        "name": "Stasiun KRL Rawa Buntu ➔ Palmerah Market / SMAN 3",
        "pillars": {
            "fastest": {
                "arrivalTime": "07:38 AM",
                "totalTime": "28 min",
                "timeSub": "Direct KRL Trunk",
                "fare": "Rp 3.000",
                "fareSub": "Statutory Tariff",
                "walkDist": "420 m",
                "walkTime": "6 min walk",
                "transitTime": "22 min",
                "transitSub": "KRL Green Line",
                "comfortScore": "86%",
                "comfortSub": "Peak Frequency",
                "accessibleScore": "95%",
                "accessibleSub": "Station Lifts",
                "breakdownText": "KRL Rail (22m) · Palmerah Walk (6m)",
                "barFeederPct": 0,
                "barRailPct": 78,
                "barWalkPct": 22,
                "steps": [
                    {"title": "Tap In at Stasiun Rawa Buntu", "time": "07:10 AM", "desc": "Enter Platform 1; high-frequency morning rush service (every 8 mins).", "dist": "30m", "meta": "Fare: Rp 3.000", "coord": [-6.3204, 106.6718]},
                    {"title": "KRL Green Line to Stasiun Palmerah", "time": "07:14 AM", "desc": "Express commuter line traversing Sudimara, Jurang Mangu, Pondok Ranji, Kebayoran to Palmerah.", "dist": "19.2 km", "meta": "22 min transit", "coord": [-6.2750, 106.7454]},
                    {"title": "Alight Stasiun Palmerah & Walk to SMAN 3", "time": "07:36 AM", "desc": "Exit East Concourse; walk 400m along broad arterial footway on Jl. Palmerah Barat.", "dist": "400m", "meta": "Lit & Guarded", "coord": [-6.2081, 106.7972]}
                ],
                "segments": [
                    {"name": "KRL Commuter Line", "mode": "rail", "time": "22 min", "coords": [[-6.3204, 106.6718], [-6.2952, 106.7115], [-6.2844, 106.7303], [-6.2750, 106.7454], [-6.2374, 106.7836], [-6.2081, 106.7972]]},
                    {"name": "Palmerah Arterial Walk", "mode": "walk", "time": "6 min", "coords": [[-6.2081, 106.7972], [-6.2090, 106.7990], [-6.2095, 106.8010]]}
                ]
            },
            "comfort": {
                "arrivalTime": "07:42 AM",
                "totalTime": "32 min",
                "timeSub": "Tree Shaded",
                "fare": "Rp 3.000",
                "fareSub": "Statutory Tariff",
                "walkDist": "400 m",
                "walkTime": "6 min walk",
                "transitTime": "26 min",
                "transitSub": "Air-Conditioned",
                "comfortScore": "94%",
                "comfortSub": "Morning Sun 29°C",
                "accessibleScore": "95%",
                "accessibleSub": "Station Lifts",
                "breakdownText": "KRL Rail (24m) · Shaded Walk (6m)",
                "barFeederPct": 0,
                "barRailPct": 75,
                "barWalkPct": 25,
                "steps": [
                    {"title": "Board KRL Commuter Line", "time": "07:10 AM", "desc": "Board air-conditioned carriage at Rawa Buntu.", "dist": "30m", "meta": "AC Carriage", "coord": [-6.3204, 106.6718]},
                    {"title": "KRL Transit to Palmerah", "time": "07:14 AM", "desc": "Smooth rail transit.", "dist": "19.2 km", "meta": "22 min", "coord": [-6.2750, 106.7454]},
                    {"title": "Tree Shaded Walk to SMAN 3", "time": "07:36 AM", "desc": "Walk along western sidewalk with continuous morning tree shadows.", "dist": "400m", "meta": "78% Shaded", "coord": [-6.2081, 106.7972]}
                ],
                "segments": [
                    {"name": "KRL Rail Trunk", "mode": "rail", "time": "22 min", "coords": [[-6.3204, 106.6718], [-6.2952, 106.7115], [-6.2844, 106.7303], [-6.2750, 106.7454], [-6.2374, 106.7836], [-6.2081, 106.7972]]},
                    {"name": "Shaded Sidewalk Walk", "mode": "walk", "time": "6 min", "coords": [[-6.2081, 106.7972], [-6.2090, 106.7990], [-6.2095, 106.8010]]}
                ]
            },
            "cheapest": {
                "arrivalTime": "07:38 AM",
                "totalTime": "28 min",
                "timeSub": "Statutory KRL",
                "fare": "Rp 3.000",
                "fareSub": "92% Savings vs Ride",
                "walkDist": "420 m",
                "walkTime": "6 min walk",
                "transitTime": "22 min",
                "transitSub": "KRL Commuter",
                "comfortScore": "86%",
                "comfortSub": "Integrated Tariff",
                "accessibleScore": "95%",
                "accessibleSub": "Station Ramps",
                "breakdownText": "KRL Rail (22m) · Walk (6m)",
                "barFeederPct": 0,
                "barRailPct": 78,
                "barWalkPct": 22,
                "steps": [
                    {"title": "Stasiun Rawa Buntu Fare Gate", "time": "07:10 AM", "desc": "Tap in with multi-trip card (KMT) or JakLingko.", "dist": "30m", "meta": "Rp 3.000", "coord": [-6.3204, 106.6718]},
                    {"title": "KRL Green Line", "time": "07:14 AM", "desc": "Direct transit to Stasiun Palmerah.", "dist": "19.2 km", "meta": "22 min", "coord": [-6.2750, 106.7454]},
                    {"title": "Walk to Palmerah Market / School", "time": "07:36 AM", "desc": "Direct sidewalk walk.", "dist": "400m", "meta": "Rp 0", "coord": [-6.2081, 106.7972]}
                ],
                "segments": [
                    {"name": "KRL Commuter Line", "mode": "rail", "time": "22 min", "coords": [[-6.3204, 106.6718], [-6.2952, 106.7115], [-6.2844, 106.7303], [-6.2750, 106.7454], [-6.2374, 106.7836], [-6.2081, 106.7972]]},
                    {"name": "Sidewalk Walk", "mode": "walk", "time": "6 min", "coords": [[-6.2081, 106.7972], [-6.2090, 106.7990], [-6.2095, 106.8010]]}
                ]
            },
            "wheelchair": {
                "arrivalTime": "07:44 AM",
                "totalTime": "34 min",
                "timeSub": "100% Step-Free",
                "fare": "Rp 3.000",
                "fareSub": "Statutory Tariff",
                "walkDist": "450 m",
                "walkTime": "8 min roll",
                "transitTime": "26 min",
                "transitSub": "Station Lifts",
                "comfortScore": "93%",
                "comfortSub": "Permen PUPR 14/2017",
                "accessibleScore": "100%",
                "accessibleSub": "0 Steps",
                "breakdownText": "Lift Access (2m) · KRL Trunk (24m) · Ramp Roll (8m)",
                "barFeederPct": 0,
                "barRailPct": 72,
                "barWalkPct": 28,
                "steps": [
                    {"title": "Stasiun Rawa Buntu Lift to Platform 1", "time": "07:10 AM", "desc": "Elevator access to train platform.", "dist": "40m", "meta": "Lift Operational", "coord": [-6.3204, 106.6718]},
                    {"title": "KRL Accessible Carriage to Palmerah", "time": "07:14 AM", "desc": "Dedicated accessible area.", "dist": "19.2 km", "meta": "22 min", "coord": [-6.2750, 106.7454]},
                    {"title": "Stasiun Palmerah Lift & Paved Ramp", "time": "07:36 AM", "desc": "Take concourse elevator to street level. Paved curb-cut ramp to Jl. Palmerah Barat.", "dist": "410m", "meta": "Slope 4.2% · 0 Steps", "coord": [-6.2081, 106.7972]}
                ],
                "segments": [
                    {"name": "KRL Rail Trunk", "mode": "rail", "time": "22 min", "coords": [[-6.3204, 106.6718], [-6.2952, 106.7115], [-6.2844, 106.7303], [-6.2750, 106.7454], [-6.2374, 106.7836], [-6.2081, 106.7972]]},
                    {"name": "Step-Free Ramp Roll", "mode": "walk", "time": "8 min", "coords": [[-6.2081, 106.7972], [-6.2090, 106.7990], [-6.2095, 106.8010]]}
                ]
            }
        }
    }
}

# Replace placeholders
final_html = html_content.replace('__FACILITIES_JSON__', json.dumps(facilities_data, separators=(',', ':')))
final_html = final_html.replace('__GRADIENT_JSON__', json.dumps(gradient_rows, separators=(',', ':')))
final_html = final_html.replace('__PLACES_JSON__', json.dumps(places_rows, separators=(',', ':')))
final_html = final_html.replace('__STATIONS_JSON__', json.dumps(stations_data, separators=(',', ':')))
final_html = final_html.replace('__PRESETS_JSON__', json.dumps(presets_data, separators=(',', ':')))

# Write out file
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

file_size_kb = os.path.getsize(output_path) / 1024
print(f"Generated {output_path} successfully ({file_size_kb:.1f} KB)!")

