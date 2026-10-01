# prototype_template.py
# Holds the complete HTML, CSS, and JS template for transit_accessibility_prototype.html

HTML_TEMPLATE = """<!DOCTYPE html>
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
      --apple-bg: #070a13;
      --apple-surface: #0e1524;
      --apple-card: rgba(16, 24, 40, 0.72);
      --apple-card-hover: rgba(26, 37, 60, 0.85);
      --apple-card-active: rgba(30, 48, 77, 0.92);
      --apple-border: rgba(255, 255, 255, 0.08);
      --apple-border-hover: rgba(255, 255, 255, 0.18);
      --apple-border-active: rgba(56, 189, 248, 0.55);
      
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
      height: 66px;
      min-height: 66px;
      background: rgba(10, 14, 24, 0.88);
      backdrop-filter: blur(28px) saturate(190%);
      -webkit-backdrop-filter: blur(28px) saturate(190%);
      border-bottom: 1px solid var(--apple-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 20px;
      z-index: 1000;
      box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }

    .brand-section {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .brand-logo-badge {
      width: 40px;
      height: 40px;
      border-radius: 11px;
      background: linear-gradient(135deg, #0284c7 0%, #0d9488 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 16px rgba(13, 148, 136, 0.4), inset 0 1px 1px rgba(255,255,255,0.4);
      color: #fff;
      flex-shrink: 0;
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
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 999px;
      background: rgba(56, 189, 248, 0.16);
      color: var(--accent-blue-light);
      border: 1px solid rgba(56, 189, 248, 0.35);
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
      padding: 6px 16px;
      border-radius: 999px;
      border: 1px solid var(--apple-border);
      backdrop-filter: blur(12px);
    }

    .hud-time-controls {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .time-slider-wrapper {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .time-scrubber {
      -webkit-appearance: none;
      width: 110px;
      height: 4px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.2);
      outline: none;
      cursor: pointer;
      transition: background 0.2s;
    }

    .time-scrubber::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: #38bdf8;
      box-shadow: 0 0 8px rgba(56, 189, 248, 0.6);
      cursor: pointer;
      transition: transform 0.1s;
    }

    .time-scrubber::-webkit-slider-thumb:hover {
      transform: scale(1.2);
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
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.2);
    }

    .hud-metrics {
      display: flex;
      align-items: center;
      gap: 14px;
      border-left: 1px solid rgba(255, 255, 255, 0.1);
      padding-left: 14px;
    }

    .metric-item {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      line-height: 1.15;
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
      font-feature-settings: "tnum";
    }

    .metric-val.hot { color: var(--accent-red-light); }
    .metric-val.cool { color: var(--accent-blue-light); }
    .metric-val.warn { color: var(--accent-amber-light); }
    .metric-val.good { color: var(--accent-green-light); }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .icon-btn {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--apple-border);
      color: var(--text-secondary);
      width: 36px;
      height: 36px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s;
    }

    .icon-btn:hover {
      background: rgba(255, 255, 255, 0.12);
      color: #ffffff;
      border-color: rgba(255, 255, 255, 0.2);
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
      width: 490px;
      min-width: 490px;
      height: 100%;
      background: rgba(13, 19, 33, 0.88);
      backdrop-filter: blur(28px) saturate(190%);
      -webkit-backdrop-filter: blur(28px) saturate(190%);
      border-right: 1px solid var(--apple-border);
      display: flex;
      flex-direction: column;
      z-index: 900;
      box-shadow: 12px 0 35px rgba(0, 0, 0, 0.45);
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* Tab Switcher in Sidebar */
    .sidebar-tabs {
      display: flex;
      padding: 10px 14px;
      gap: 6px;
      background: rgba(9, 13, 23, 0.7);
      border-bottom: 1px solid var(--apple-border);
    }

    .tab-btn {
      flex: 1;
      background: transparent;
      border: 1px solid transparent;
      padding: 8px 6px;
      border-radius: 9px;
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
      background: rgba(255, 255, 255, 0.05);
    }

    .tab-btn.active {
      background: rgba(255, 255, 255, 0.09);
      color: #ffffff;
      border-color: rgba(255, 255, 255, 0.14);
      font-weight: 600;
      box-shadow: 0 3px 10px rgba(0, 0, 0, 0.25);
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
      gap: 14px;
    }

    .sidebar-content::-webkit-scrollbar {
      width: 5px;
    }
    .sidebar-content::-webkit-scrollbar-thumb {
      background: rgba(255, 255, 255, 0.16);
      border-radius: 3px;
    }
    .sidebar-content::-webkit-scrollbar-thumb:hover {
      background: rgba(56, 189, 248, 0.5);
    }

    /* Glass Cards */
    .glass-card {
      background: var(--apple-card);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid var(--apple-border);
      border-radius: 14px;
      padding: 14px;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.08), 0 6px 20px rgba(0,0,0,0.25);
    }

    .glass-card:hover {
      border-color: var(--apple-border-hover);
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
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.08);
      color: var(--text-secondary);
      border: 1px solid rgba(255, 255, 255, 0.06);
    }

    /* Route Presets Selector */
    .preset-selector-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .preset-label-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .preset-label {
      font-size: 11px;
      font-weight: 700;
      color: var(--text-secondary);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .preset-case-badge {
      font-size: 10px;
      font-weight: 600;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.12);
      padding: 2px 7px;
      border-radius: 999px;
      border: 1px solid rgba(56, 189, 248, 0.25);
    }

    .preset-dropdown {
      width: 100%;
      background: rgba(9, 13, 23, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.14);
      color: #ffffff;
      padding: 9px 12px;
      border-radius: 10px;
      font-size: 12px;
      font-family: var(--font-stack);
      outline: none;
      cursor: pointer;
      transition: all 0.2s;
    }

    .preset-dropdown:focus {
      border-color: var(--accent-blue-light);
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.25);
    }

    /* The 4-Pillar Tactile Segmented Control */
    .pillars-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 8px;
    }

    .pillar-btn {
      background: rgba(255, 255, 255, 0.03);
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
      background: rgba(255, 255, 255, 0.07);
      border-color: rgba(255, 255, 255, 0.18);
    }

    .pillar-btn:active {
      transform: scale(0.98);
    }

    .pillar-btn.active[data-pillar="fastest"] {
      background: rgba(14, 165, 233, 0.15);
      border-color: #38bdf8;
      box-shadow: 0 0 18px rgba(56, 189, 248, 0.25);
    }

    .pillar-btn.active[data-pillar="comfort"] {
      background: rgba(16, 185, 129, 0.15);
      border-color: #10b981;
      box-shadow: 0 0 18px rgba(16, 185, 129, 0.25);
    }

    .pillar-btn.active[data-pillar="cheapest"] {
      background: rgba(245, 158, 11, 0.15);
      border-color: #f59e0b;
      box-shadow: 0 0 18px rgba(245, 158, 11, 0.25);
    }

    .pillar-btn.active[data-pillar="wheelchair"] {
      background: rgba(244, 63, 94, 0.15);
      border-color: #f43f5e;
      box-shadow: 0 0 18px rgba(244, 63, 94, 0.25);
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
      font-size: 10px;
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
      font-weight: 700;
      letter-spacing: 0.04em;
      color: var(--text-muted);
      margin-bottom: 3px;
    }

    .kpi-val {
      font-size: 16px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: -0.02em;
      font-feature-settings: "tnum";
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
      border-radius: 11px;
      padding: 10px 12px;
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 11.5px;
      line-height: 1.35;
      margin-top: 8px;
    }

    .alert-banner.thermal {
      background: rgba(245, 158, 11, 0.14);
      border: 1px solid rgba(245, 158, 11, 0.35);
      color: #fde68a;
    }

    .alert-banner.night {
      background: rgba(99, 102, 241, 0.14);
      border: 1px solid rgba(99, 102, 241, 0.35);
      color: #c7d2fe;
    }

    .alert-banner.wheelchair {
      background: rgba(16, 185, 129, 0.14);
      border: 1px solid rgba(16, 185, 129, 0.35);
      color: #a7f3d0;
    }

    .alert-banner.tariff {
      background: rgba(56, 189, 248, 0.14);
      border: 1px solid rgba(56, 189, 248, 0.35);
      color: #bae6fd;
    }

    .alert-icon {
      font-size: 16px;
      flex-shrink: 0;
      margin-top: 1px;
    }

    /* Journey Simulator Control Box */
    .simulator-control-box {
      margin-top: 10px;
      background: rgba(0, 0, 0, 0.25);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      padding: 10px 12px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .sim-header-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .sim-title {
      font-size: 11.5px;
      font-weight: 700;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .sim-buttons-row {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .sim-primary-btn {
      flex: 1;
      background: linear-gradient(135deg, #0284c7 0%, #0d9488 100%);
      color: #ffffff;
      border: none;
      padding: 8px 12px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.2s;
      box-shadow: 0 4px 12px rgba(13, 148, 136, 0.35);
    }

    .sim-primary-btn:hover {
      opacity: 0.95;
      transform: translateY(-1px);
    }

    .sim-speed-btn {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--apple-border);
      color: var(--text-secondary);
      font-size: 10px;
      font-weight: 700;
      padding: 6px 8px;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.2s;
    }

    .sim-speed-btn.active {
      background: rgba(56, 189, 248, 0.2);
      color: #38bdf8;
      border-color: rgba(56, 189, 248, 0.4);
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
      border-radius: 11px;
      padding: 10px 12px;
      display: flex;
      align-items: flex-start;
      gap: 10px;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
    }

    .step-card:hover {
      background: rgba(255, 255, 255, 0.07);
      border-color: rgba(255, 255, 255, 0.16);
      transform: translateX(2px);
    }

    .step-card.active-step {
      background: rgba(56, 189, 248, 0.12);
      border-color: #38bdf8;
      box-shadow: 0 0 16px rgba(56, 189, 248, 0.25);
    }

    .step-num-badge {
      width: 24px;
      height: 24px;
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

    .step-card.active-step .step-num-badge {
      background: #38bdf8;
      color: #0b0f19;
      box-shadow: 0 0 8px #38bdf8;
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
      font-weight: 700;
      color: #ffffff;
    }

    .step-time-badge {
      font-size: 10px;
      color: var(--accent-blue-light);
      font-weight: 600;
      font-feature-settings: "tnum";
    }

    .step-desc {
      font-size: 11px;
      color: var(--text-secondary);
      line-height: 1.35;
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
      font-feature-settings: "tnum";
    }

    .h2h-details-list {
      font-size: 11px;
      color: var(--text-secondary);
      line-height: 1.4;
      display: flex;
      flex-direction: column;
      gap: 5px;
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
      font-weight: 700;
      text-transform: uppercase;
      font-size: 9px;
    }

    .matrix-table td.bad {
      color: #fca5a5;
      font-weight: 600;
    }

    .matrix-table td.good {
      color: #6ee7b7;
      font-weight: 700;
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
      background: #070a13;
    }

    #map {
      width: 100%;
      height: 100%;
      background: #070a13;
    }

    /* Glowing polyline filter */
    .leaflet-interactive.route-glow {
      filter: drop-shadow(0 0 8px rgba(56, 189, 248, 0.7));
    }

    /* Floating Apple Map Layer Controls Overlay */
    .map-overlay-panel {
      position: absolute;
      top: 16px;
      right: 16px;
      z-index: 800;
      background: rgba(13, 19, 33, 0.85);
      backdrop-filter: blur(24px) saturate(180%);
      -webkit-backdrop-filter: blur(24px) saturate(180%);
      border: 1px solid var(--apple-border);
      border-radius: 14px;
      padding: 12px;
      width: 250px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.5);
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
      background: rgba(13, 19, 33, 0.88);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid var(--apple-border);
      border-radius: 10px;
      padding: 8px 14px;
      display: flex;
      align-items: center;
      gap: 14px;
      font-size: 11px;
      color: var(--text-secondary);
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
    }

    .legend-indicator {
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .line-sample {
      width: 16px;
      height: 3px;
      border-radius: 2px;
    }

    /* Floating Commuter HUD Banner (During Simulation) */
    .sim-floating-hud {
      position: absolute;
      top: 16px;
      left: 60px;
      z-index: 850;
      background: rgba(13, 19, 33, 0.92);
      backdrop-filter: blur(24px) saturate(180%);
      -webkit-backdrop-filter: blur(24px) saturate(180%);
      border: 1px solid var(--apple-border-active);
      border-radius: 14px;
      padding: 10px 16px;
      display: flex;
      align-items: center;
      gap: 16px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.55);
      animation: fadeInDown 0.3s ease-out;
    }

    @keyframes fadeInDown {
      from { opacity: 0; transform: translateY(-10px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .sim-hud-mode-badge {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border-radius: 999px;
      font-size: 11.5px;
      font-weight: 700;
      background: rgba(56, 189, 248, 0.2);
      color: #38bdf8;
      border: 1px solid rgba(56, 189, 248, 0.4);
    }

    .sim-hud-details {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }

    .sim-hud-leg-title {
      font-size: 12px;
      font-weight: 700;
      color: #ffffff;
    }

    .sim-hud-sub {
      font-size: 10.5px;
      color: var(--text-secondary);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .sim-hud-alert-chip {
      font-size: 10px;
      font-weight: 600;
      color: #fde68a;
      background: rgba(245, 158, 11, 0.2);
      padding: 1px 6px;
      border-radius: 4px;
      border: 1px solid rgba(245, 158, 11, 0.3);
    }

    /* Radar Pulse Marker Animation */
    @keyframes radar-pulse {
      0% { transform: scale(0.6); opacity: 0.9; }
      50% { opacity: 0.4; }
      100% { transform: scale(2.4); opacity: 0; }
    }

    .pulse-ring-element {
      position: absolute;
      top: -10px;
      left: -10px;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      border: 2px solid #38bdf8;
      animation: radar-pulse 2s infinite ease-out;
      pointer-events: none;
    }

    .pulse-ring-dest {
      border-color: #f43f5e;
    }

    /* Responsive Handling */
    @media (max-width: 1024px) {
      aside.sidebar-panel {
        width: 420px;
        min-width: 420px;
      }
    }
    @media (max-width: 768px) {
      .app-main {
        flex-direction: column;
      }
      aside.sidebar-panel {
        width: 100%;
        min-width: 100%;
        height: 52vh;
      }
      .map-canvas-container {
        height: 48vh;
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
          PIJAK TRANSIT ACCESSIBILITY ENGINE
          <span class="brand-tag">Research v3.0</span>
        </div>
        <div class="brand-subtitle">
          Multimodal 4-Pillar Router · Microclimate Solar ray-tracer · Apple Developer Academy @ BINUS
        </div>
      </div>
    </div>

    <!-- Microclimate Scrub HUD -->
    <div class="microclimate-hud">
      <div class="hud-time-controls">
        <div class="time-slider-wrapper">
          <span class="metric-label">Time:</span>
          <input type="range" class="time-scrubber" id="time-scrubber-input" min="360" max="1410" step="15" value="1350" oninput="onTimeSliderChange(this.value)" />
        </div>
        <div class="hud-time-presets">
          <button class="time-pill" data-time="08:30" onclick="setTimeOfDay('08:30')">
            <i data-lucide="sunrise" style="width: 12px; height: 12px;"></i> 08:30
          </button>
          <button class="time-pill" data-time="12:00" onclick="setTimeOfDay('12:00')">
            <i data-lucide="sun" style="width: 12px; height: 12px;"></i> 12:00
          </button>
          <button class="time-pill" data-time="17:30" onclick="setTimeOfDay('17:30')">
            <i data-lucide="sunset" style="width: 12px; height: 12px;"></i> 17:30
          </button>
          <button class="time-pill active" data-time="22:30" onclick="setTimeOfDay('22:30')">
            <i data-lucide="moon" style="width: 12px; height: 12px;"></i> 22:30
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
      <button class="icon-btn" onclick="toggleMapStyle()" title="Toggle Basemap Style (Dark / Light / Satellite)">
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
            <div class="preset-label-row">
              <label class="preset-label" for="route-preset-select">Origin & Destination Scenario</label>
              <span class="preset-case-badge" id="preset-active-case-tag">Case 1 · Late Curfew</span>
            </div>
            <select class="preset-dropdown" id="route-preset-select" onchange="onPresetChange(this.value)">
              <option value="preset_bsd_kebayoran" selected>Case 1: Apple Dev Academy (BSD) ➔ Jl. Kuburan Lama (22:30 WIB Curfew)</option>
              <option value="preset_dukuh_menara_bca">Case 2: MRT Dukuh Atas ➔ Menara BCA / Grand Indonesia (12:00 Midday Heat)</option>
              <option value="preset_sudirman_dukuh_setiabudi">Case 3: KRL Sudirman ➔ MRT Dukuh Atas ➔ LRT Setiabudi (Wheelchair Transfer)</option>
              <option value="preset_tebet_megakuningan">Case 4: Stasiun KRL Tebet ➔ Mega Kuningan (08:30 Peak Feeder Shortcut)</option>
              <option value="preset_bni_bundaranhi">Case 5: Stasiun BNI City (KA Bandara) ➔ MRT Bundaran HI (Heavy Luggage)</option>
              <option value="preset_wisma_cheshire">Case 6: Wisma Cheshire (Cilandak) ➔ Dukuh Atas TOD [Wheelchair Co-Test]</option>
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
              <div class="pillar-desc">Chained multimodal A* · Min travel time</div>
            </button>

            <button class="pillar-btn" data-pillar="comfort" onclick="selectPillar('comfort')">
              <div class="pillar-icon-row">
                <span class="pillar-icon">🛋️</span>
                <span class="pillar-status-dot"></span>
              </div>
              <div class="pillar-name">Comfort</div>
              <div class="pillar-desc">Solar shade · Continuous lighting · Max shelter</div>
            </button>

            <button class="pillar-btn" data-pillar="cheapest" onclick="selectPillar('cheapest')">
              <div class="pillar-icon-row">
                <span class="pillar-icon">💰</span>
                <span class="pillar-status-dot"></span>
              </div>
              <div class="pillar-name">Cheapest</div>
              <div class="pillar-desc">Rp 0 JakLingko · Rp 3k KRL · Flat TJ</div>
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
              <div class="legend-item"><span class="legend-color-dot" style="background: #38bdf8;"></span> Feeder / Bus</div>
              <div class="legend-item"><span class="legend-color-dot" style="background: #6366f1;"></span> KRL / MRT / Rail</div>
              <div class="legend-item"><span class="legend-color-dot" style="background: #10b981;"></span> Pedestrian Walk</div>
              <div class="legend-item"><span class="legend-color-dot" style="background: #a855f7;"></span> Transfer Sync</div>
            </div>
          </div>

          <!-- Journey Simulator Box -->
          <div class="simulator-control-box">
            <div class="sim-header-row">
              <span class="sim-title">
                <i data-lucide="play-circle" style="width: 15px; height: 15px; color: #38bdf8;"></i>
                Animated Journey Playback
              </span>
              <div style="display: flex; gap: 4px;">
                <button class="sim-speed-btn active" id="sim-spd-1" onclick="setSimSpeed(1)">1x</button>
                <button class="sim-speed-btn" id="sim-spd-2" onclick="setSimSpeed(2)">2x</button>
                <button class="sim-speed-btn" id="sim-spd-4" onclick="setSimSpeed(4)">4x</button>
              </div>
            </div>
            <div class="sim-buttons-row">
              <button class="sim-primary-btn" id="sim-run-btn" onclick="toggleJourneySimulation()">
                <i data-lucide="play" id="sim-run-icon" style="width: 14px; height: 14px;"></i>
                <span id="sim-run-text">Simulate Journey</span>
              </button>
              <button class="icon-btn" onclick="resetJourneySimulation()" title="Reset Simulation">
                <i data-lucide="rotate-ccw" style="width: 14px; height: 14px;"></i>
              </button>
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
        
        <!-- Scenario Switcher for Tab 2 -->
        <div class="glass-card" style="padding: 10px 14px;">
          <div class="preset-selector-group">
            <label class="preset-label" for="h2h-scenario-select">Compare Scenario Benchmark</label>
            <select class="preset-dropdown" id="h2h-scenario-select" onchange="onH2HScenarioChange(this.value)">
              <option value="preset_bsd_kebayoran" selected>Case 1: Late-Night BSD ➔ Palmerah (Curfew Cutoff)</option>
              <option value="preset_dukuh_menara_bca">Case 2: Midday MRT Dukuh Atas ➔ Menara BCA (Tropical Heat)</option>
              <option value="preset_sudirman_dukuh_setiabudi">Case 3: Wheelchair Sudirman ➔ Dukuh Atas ➔ LRT (Step-Free)</option>
              <option value="preset_tebet_megakuningan">Case 4: Stasiun Tebet ➔ Mega Kuningan (Peak Hour Shortcut)</option>
              <option value="preset_bni_bundaranhi">Case 5: Airport BNI City ➔ Bundaran HI (Heavy Luggage)</option>
              <option value="preset_wisma_cheshire">Case 6: Wisma Cheshire ➔ Dukuh Atas TOD (Wheelchair Benchmark)</option>
            </select>
          </div>
        </div>

        <div class="h2h-scenario-banner" id="h2h-banner-elem">
          <div class="h2h-title" id="h2h-banner-title">
            <i data-lucide="flame" style="width: 18px; height: 18px; color: #ef4444;"></i>
            The 10:30 PM BSD Nocturnal Commute Challenge
          </div>
          <div class="h2h-sub" id="h2h-banner-sub">
            Origin: <strong>Apple Developer Academy @ BINUS (BSD GOP 9)</strong><br />
            Destination: <strong>Jl. Kuburan Lama (Palmerah / Kebayoran)</strong><br />
            Time of Departure: <strong>22:30 WIB (Night Curfew)</strong>
          </div>
        </div>

        <button class="sim-primary-btn" style="padding: 10px;" onclick="renderHeadToHeadRoute(true)">
          <i data-lucide="play" style="width: 16px; height: 16px;"></i>
          Animate Head-to-Head Comparison on Map
        </button>

        <div class="h2h-cards-grid">
          
          <!-- Google Maps Failure Card -->
          <div class="h2h-card gmaps-fail">
            <div class="h2h-card-header">
              <span class="h2h-brand-tag gmaps">
                <i data-lucide="x-circle" style="width: 16px; height: 16px;"></i>
                Google Maps Navigation
              </span>
              <span class="h2h-status-badge fail" id="h2h-gmaps-badge">Failure Mode</span>
            </div>

            <div class="h2h-metric-row">
              <div class="h2h-metric">
                <span class="h2h-metric-label">Travel Time</span>
                <span class="h2h-metric-val" id="h2h-gmaps-time" style="color: #f87171;">3h 32m – 7h 50m</span>
              </div>
              <div class="h2h-metric">
                <span class="h2h-metric-label">Exposure</span>
                <span class="h2h-metric-val" id="h2h-gmaps-walk" style="color: #f87171;">47 min (Dark)</span>
              </div>
              <div class="h2h-metric">
                <span class="h2h-metric-label">Trip Fare</span>
                <span class="h2h-metric-val" id="h2h-gmaps-fare">Rp 92.000+</span>
              </div>
            </div>

            <div class="h2h-details-list" id="h2h-gmaps-list">
              <!-- Injected via JS -->
            </div>
          </div>

          <!-- Pijak Multimodal Solution Card -->
          <div class="h2h-card pijak-win">
            <div class="h2h-card-header">
              <span class="h2h-brand-tag pijak">
                <i data-lucide="check-circle" style="width: 16px; height: 16px;"></i>
                Pijak Multimodal Solution
              </span>
              <span class="h2h-status-badge win" id="h2h-pijak-badge">Proven Solution</span>
            </div>

            <div class="h2h-metric-row">
              <div class="h2h-metric">
                <span class="h2h-metric-label">Travel Time</span>
                <span class="h2h-metric-val" id="h2h-pijak-time" style="color: #34d399;">40 min Total</span>
              </div>
              <div class="h2h-metric">
                <span class="h2h-metric-label">Exposure</span>
                <span class="h2h-metric-val" id="h2h-pijak-walk" style="color: #34d399;">8 min (Lit)</span>
              </div>
              <div class="h2h-metric">
                <span class="h2h-metric-label">Trip Fare</span>
                <span class="h2h-metric-val" id="h2h-pijak-fare" style="color: #34d399;">Rp 3.000</span>
              </div>
            </div>

            <div class="h2h-details-list" id="h2h-pijak-list">
              <!-- Injected via JS -->
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
            <tbody id="h2h-matrix-body">
              <!-- Injected via JS -->
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
            <button class="bookmark-btn" onclick="focusStation('tebet_krl')">Stn. Tebet</button>
            <button class="bookmark-btn" onclick="focusStation('bundaran_hi')">MRT Bundaran HI</button>
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
            <span class="card-badge" style="color: #6ee7b7;">Ground-Truth Validated</span>
          </div>
          <p style="font-size: 11.5px; color: var(--text-secondary); line-height: 1.4;">
            In-situ participatory research with permanent manual wheelchair residents at <strong>Wisma Cheshire Indonesia</strong> (Jl. Wijaya Kusuma No. 15A, Cilandak Barat, South Jakarta).
          </p>
          <div style="margin-top: 8px; font-size: 11px; color: var(--text-secondary); display: flex; flex-direction: column; gap: 5px;">
            <div>• <strong>Agency & Dignity:</strong> Eliminates unexpected 20-cm drop-offs that force wheelchair users into helpless dependence on strangers.</div>
            <div>• <strong>Biomechanical Strain:</strong> Calibrates upper-body energy expenditure on slopes exceeding 8.33% (Permen PUPR 14/2017).</div>
            <div>• <strong>Fatmawati Corridor:</strong> Verified continuous ramp path linking Wisma Cheshire directly to MRT Fatmawati Station Elevators.</div>
          </div>
          <button class="sim-primary-btn" style="width: 100%; margin-top: 10px; padding: 8px;" onclick="focusStation('wisma_cheshire')">
            <i data-lucide="map-pin" style="width: 13px; height: 13px;"></i> Fly to Wisma Cheshire & MRT Fatmawati
          </button>
        </div>

      </div>

    </aside>

    <!-- Right Map Canvas Container -->
    <div class="map-canvas-container">
      <div id="map"></div>

      <!-- Floating Live Commuter HUD during Simulation -->
      <div class="sim-floating-hud" id="sim-floating-hud" style="display: none;">
        <div class="sim-hud-mode-badge" id="sim-hud-mode">
          <span>🚶‍♂️</span> <span>Walking</span>
        </div>
        <div class="sim-hud-details">
          <div class="sim-hud-leg-title" id="sim-hud-title">Moving: GOP 9 Campus ➔ Rawa Buntu</div>
          <div class="sim-hud-sub">
            <span id="sim-hud-speed">4.8 km/h</span> · 
            <span id="sim-hud-progress">Leg 1 of 5</span> · 
            <span id="sim-hud-transfer">0 Transfers</span>
            <span class="sim-hud-alert-chip" id="sim-hud-alert" style="display: none;">☀️ Shaded</span>
          </div>
        </div>
      </div>

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
          <button class="bookmark-btn" onclick="focusStation('binus_bsd')">BSD GOP 9</button>
          <button class="bookmark-btn" onclick="focusStation('tebet_krl')">Stn. Tebet</button>
          <button class="bookmark-btn" onclick="focusStation('wisma_cheshire')">Wisma Cheshire</button>
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
    const STATIONS = __STATIONS_JSON__;
    const BUILDINGS = __BUILDINGS_JSON__;
    const ROUTE_PRESETS = __PRESETS_JSON__;

    // App State
    let currentTab = 'router';
    let currentPreset = 'preset_bsd_kebayoran';
    let currentPillar = 'fastest';
    let currentTimeOfDay = '22:30';
    let currentBasemap = 'dark';
    
    let map;
    let baseTileLayer = null;
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
    let pulseLayerGroup;

    // Simulation animation state
    let simInterval = null;
    let simCommuterMarker = null;
    let isSimulating = false;
    let simSpeedMultiplier = 1;

    // Custom SVG Pin Generator for Leaflet
    function createCustomPin(type, color, text) {
      let iconSvg = '';
      if (type === 'krl') {
        iconSvg = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="3" width="16" height="16" rx="2"/><path d="M4 11h16"/><path d="M12 3v8"/><path d="m8 19-2 3"/><path d="m18 22-2-3"/><circle cx="8" cy="15" r="1"/><circle cx="16" cy="15" r="1"/></svg>';
      } else if (type === 'mrt') {
        iconSvg = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v10a3 3 0 0 1-3 3H7a3 3 0 0 1-3-3V6Z"/><path d="m9 17-2 3"/><path d="m17 20-2-3"/><circle cx="9" cy="12" r="1"/><circle cx="15" cy="12" r="1"/></svg>';
      } else if (type === 'lrt') {
        iconSvg = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="16" x="4" y="3" rx="2"/><path d="M12 3v8"/><path d="M4 11h16"/><path d="m8 19-2 3"/><path d="m18 22-2-3"/></svg>';
      } else if (type === 'airport') {
        iconSvg = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"/></svg>';
      } else if (type === 'accessibility') {
        iconSvg = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="4" r="2"/><path d="m18 19 1-7-6 1"/><path d="m5 8 3-3 5.5 3-2.36 3.5"/><path d="M4.24 14.5a5 5 0 0 0 6.88 6"/><path d="M13.76 17.5a5 5 0 0 0-4-7.5"/></svg>';
      } else {
        iconSvg = '<div style="width:7px; height:7px; border-radius:50%; background:#fff;"></div>';
      }

      const html = `
        <div style="position:relative; display:flex; align-items:center; justify-content:center; width:26px; height:26px;">
          <div style="position:absolute; width:26px; height:26px; border-radius:50%; background:${color}; box-shadow:0 0 10px ${color}, inset 0 1px 1px rgba(255,255,255,0.4); display:flex; align-items:center; justify-content:center; border:2px solid #ffffff;">
            ${iconSvg}
          </div>
        </div>
      `;
      return L.divIcon({ html: html, className: 'custom-station-pin', iconSize: [26, 26], iconAnchor: [13, 13] });
    }

    // Init Map and UI
    window.addEventListener('DOMContentLoaded', () => {
      lucide.createIcons();
      initMap();
      loadGradientTable(GRADIENT_DATA);
      updateMicroclimateState('22:30');
      renderRouteSolution();
    });

    function initMap() {
      map = L.map('map', {
        center: [-6.2300, 106.7800],
        zoom: 12,
        zoomControl: false
      });

      L.control.zoom({ position: 'topleft' }).addTo(map);

      setBasemap('dark');

      transitLayerGroup = L.layerGroup().addTo(map);
      catchmentLayerGroup = L.layerGroup().addTo(map);
      facilitiesLayerGroup = L.layerGroup().addTo(map);
      shadeLayerGroup = L.layerGroup().addTo(map);
      lightingLayerGroup = L.layerGroup().addTo(map);
      wheelchairLayerGroup = L.layerGroup().addTo(map);
      activeRouteLayerGroup = L.layerGroup().addTo(map);
      simulationLayerGroup = L.layerGroup().addTo(map);
      pulseLayerGroup = L.layerGroup().addTo(map);

      renderTransitNetwork();
      renderCatchmentBuffers();
      renderFacilities();
      renderSolarShades('22:30');
      renderNightLighting();
      renderWheelchairNodes();
    }

    function setBasemap(style) {
      if (baseTileLayer) { map.removeLayer(baseTileLayer); baseTileLayer = null; }
      if (referenceTileLayer) { map.removeLayer(referenceTileLayer); referenceTileLayer = null; }

      currentBasemap = style;
      if (style === 'dark') {
        baseTileLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}', {
          maxNativeZoom: 16, maxZoom: 19, attribution: 'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ'
        }).addTo(map);
        referenceTileLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Reference/MapServer/tile/{z}/{y}/{x}', {
          maxNativeZoom: 16, maxZoom: 19, attribution: ''
        }).addTo(map);
      } else if (style === 'satellite') {
        baseTileLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
          maxZoom: 19, attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS'
        }).addTo(map);
      } else {
        baseTileLayer = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
          maxZoom: 19, attribution: '&copy; OpenStreetMap contributors'
        }).addTo(map);
      }
    }

    function toggleMapStyle() {
      if (currentBasemap === 'dark') setBasemap('light');
      else if (currentBasemap === 'light') setBasemap('satellite');
      else setBasemap('dark');
    }

    // Render Transit Network with custom pins and glowing lines
    function renderTransitNetwork() {
      transitLayerGroup.clearLayers();

      // KRL Green Line
      const krlGreenCoords = [
        [-6.3204, 106.6718], [-6.2952, 106.7115], [-6.2844, 106.7303],
        [-6.2750, 106.7454], [-6.2374, 106.7836], [-6.2081, 106.7972], [-6.1856, 106.8110]
      ];
      L.polyline(krlGreenCoords, { color: '#10b981', weight: 4.5, opacity: 0.85, dashArray: '8, 4' })
        .bindPopup('<b>KRL Commuter Line</b><br>Rangkasbitung Line (Green Line)').addTo(transitLayerGroup);

      // KRL Loop Line
      const krlLoopCoords = [
        [-6.1856, 106.8110], [-6.2003, 106.8166], [-6.2018, 106.8214],
        [-6.2024, 106.8233], [-6.2099, 106.8498]
      ];
      L.polyline(krlLoopCoords, { color: '#3b82f6', weight: 4.5, opacity: 0.85 })
        .bindPopup('<b>KRL Commuter Line</b><br>Cikarang / Loop Line').addTo(transitLayerGroup);

      // KRL Bogor Line (Manggarai -> Tebet -> Cawang)
      const krlBogorCoords = [
        [-6.2099, 106.8498], [-6.2265, 106.8582], [-6.2427, 106.8585]
      ];
      L.polyline(krlBogorCoords, { color: '#e11d48', weight: 4.5, opacity: 0.85 })
        .bindPopup('<b>KRL Commuter Line</b><br>Bogor Line (Red Line)').addTo(transitLayerGroup);

      // MRT Jakarta North-South Line
      const mrtCoords = [
        [-6.2891, 106.7745], [-6.2928, 106.7937], [-6.2787, 106.7972],
        [-6.2665, 106.7974], [-6.2555, 106.7975], [-6.2445, 106.7981],
        [-6.2386, 106.7988], [-6.2253, 106.8027], [-6.2195, 106.8080],
        [-6.2145, 106.8184], [-6.2088, 106.8219], [-6.2014, 106.8227], [-6.1925, 106.8231]
      ];
      L.polyline(mrtCoords, { color: '#0284c7', weight: 5, opacity: 0.95 })
        .bindPopup('<b>MRT Jakarta</b><br>North-South Line (M1)').addTo(transitLayerGroup);

      // LRT Jabodebek
      const lrtCoords = [
        [-6.2028, 106.8248], [-6.2088, 106.8290], [-6.2185, 106.8318],
        [-6.2307, 106.8329], [-6.2435, 106.8398], [-6.2468, 106.8643]
      ];
      L.polyline(lrtCoords, { color: '#f43f5e', weight: 4.5, opacity: 0.85 })
        .bindPopup('<b>LRT Jabodebek</b><br>Dukuh Atas - Harjamukti / Jatimulya').addTo(transitLayerGroup);

      // JakLingko Mikrotrans (JAK-11 Kebayoran - Tanah Abang)
      const jak11Coords = [
        [-6.2374, 106.7836], [-6.2240, 106.7890], [-6.2081, 106.7972],
        [-6.1950, 106.8030], [-6.1856, 106.8110]
      ];
      L.polyline(jak11Coords, { color: '#f59e0b', weight: 3.5, opacity: 0.75, dashArray: '6, 6' })
        .bindPopup('<b>JakLingko Mikrotrans JAK-11</b><br>Kebayoran - Tanah Abang (Tariff: Rp 0)').addTo(transitLayerGroup);

      // JakLingko Mikrotrans (JAK.43 Tebet - Mega Kuningan)
      const jak43Coords = [
        [-6.2265, 106.8582], [-6.2250, 106.8510], [-6.2238, 106.8420],
        [-6.2245, 106.8340], [-6.2275, 106.8290], [-6.2285, 106.8275]
      ];
      L.polyline(jak43Coords, { color: '#f59e0b', weight: 3.5, opacity: 0.85, dashArray: '6, 6' })
        .bindPopup('<b>JakLingko Mikrotrans JAK.43</b><br>Tebet - Kuningan (Tariff: Rp 0 Shortcut)').addTo(transitLayerGroup);

      // Render Station Custom Pins
      STATIONS.forEach(st => {
        let pinColor = '#3b82f6';
        if (st.type === 'krl') pinColor = '#10b981';
        else if (st.type === 'mrt') pinColor = '#0284c7';
        else if (st.type === 'lrt') pinColor = '#f43f5e';
        else if (st.type === 'airport') pinColor = '#06b6d4';
        else if (st.type === 'origin') pinColor = '#38bdf8';
        else if (st.type === 'dest') pinColor = '#f43f5e';
        else if (st.type === 'accessibility') pinColor = '#ec4899';

        const customPin = createCustomPin(st.type, pinColor);
        const marker = L.marker([st.lat, st.lon], { icon: customPin }).addTo(transitLayerGroup);
        marker.bindPopup(`<b>${st.name}</b><br>${st.desc}`);

        // Interactive sync: clicking station centers map & flashes relevant step card
        marker.on('click', () => {
          syncMapClickToSidebar(st.name);
        });
      });
    }

    // Render 500m Station Catchment Buffers
    function renderCatchmentBuffers() {
      catchmentLayerGroup.clearLayers();

      const keyStations = [
        { name: "Dukuh Atas TOD Nexus", lat: -6.2014, lon: 106.8227 },
        { name: "Stasiun KRL Kebayoran", lat: -6.2374, lon: 106.7836 },
        { name: "Stasiun KRL Rawa Buntu", lat: -6.3204, lon: 106.6718 },
        { name: "Stasiun MRT Fatmawati", lat: -6.2928, lon: 106.7937 },
        { name: "Stasiun KRL Tebet", lat: -6.2265, lon: 106.8582 },
        { name: "Stasiun MRT Bundaran HI", lat: -6.1925, lon: 106.8231 }
      ];

      keyStations.forEach(st => {
        L.circle([st.lat, st.lon], {
          radius: 500, color: '#a855f7', weight: 1.5, opacity: 0.7,
          fillColor: '#a855f7', fillOpacity: 0.12, dashArray: '4, 4'
        }).bindPopup(`<b>${st.name}</b><br>500-Meter Walkable Catchment Area (6-8 mins walk)`).addTo(catchmentLayerGroup);

        L.circle([st.lat, st.lon], {
          radius: 800, color: '#c084fc', weight: 1, opacity: 0.35,
          fillColor: 'transparent', dashArray: '3, 6'
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
            radius: 4.5, fillColor: color, color: '#ffffff', weight: 1, fillOpacity: 0.85
          }).bindPopup(`<b>${label}</b><br>Type: ${facility}<br>Accessible: ${props.accessible || 'Verified'}`).addTo(facilitiesLayerGroup);
        } else if (geom.type === 'LineString') {
          const latlngs = geom.coordinates.map(c => [c[1], c[0]]);
          const stroke = props.stroke || '#38bdf8';
          L.polyline(latlngs, {
            color: stroke, weight: props['stroke-width'] || 2, opacity: 0.7
          }).bindPopup(`<b>${props.name || 'Sidewalk / Path'}</b><br>Layer: ${props.layer || 'sidewalk'}`).addTo(facilitiesLayerGroup);
        }
      });
    }

    // Dynamic 2.5D Solar Shadows around High-Rises
    function renderSolarShades(timeStr) {
      shadeLayerGroup.clearLayers();

      const [hours, minutes] = timeStr.split(':').map(Number);
      const totalMinutes = hours * 60 + minutes;

      // Night time (after 18:30 or before 05:45) -> zero solar shadows
      if (totalMinutes >= 1110 || totalMinutes < 345) return;

      // Approximate solar astronomical calculation for Jakarta (Lat: -6.2° S)
      // Sunrise ~05:45 (345 min), Solar Noon ~12:00 (720 min), Sunset ~18:15 (1095 min)
      const solarProg = (totalMinutes - 345) / (1095 - 345); // 0 to 1
      const solarAltitude = Math.sin(solarProg * Math.PI) * 82; // Max elevation ~82 deg at noon
      const elevationRad = Math.max(solarAltitude, 8) * Math.PI / 180;
      
      // Azimuth: Morning East (75 deg) -> Noon North (355 deg) -> Evening West (285 deg)
      const azimuthDeg = 75 + solarProg * (285 - 75);
      const shadowAngleRad = ((azimuthDeg + 180) % 360) * Math.PI / 180;
      const factor = 1 / Math.tan(elevationRad); // Shadow length factor

      BUILDINGS.forEach(b => {
        const shadowLenMeters = Math.min(b.height * factor, 350); // Cap at 350m
        const dLat = (shadowLenMeters * Math.cos(shadowAngleRad)) / 111000;
        const dLon = (shadowLenMeters * Math.sin(shadowAngleRad)) / 110500;

        const bLat = b.lat;
        const bLon = b.lon;
        const rLat = (b.radius / 111000);
        const rLon = (b.radius / 110500);

        const shadowPoly = [
          [bLat - rLat, bLon - rLon],
          [bLat + rLat, bLon - rLon],
          [bLat + rLat + dLat, bLon + rLon + dLon],
          [bLat - rLat + dLat, bLon - rLon + dLon]
        ];

        L.polygon(shadowPoly, {
          color: '#1e293b',
          weight: 1,
          fillColor: '#0a0f1d',
          fillOpacity: 0.55
        }).bindPopup(`<b>${b.name} (${b.height}m)</b><br>CoolWalks Ray-Cast Shadow at ${timeStr}<br>Shadow Length: ${Math.round(shadowLenMeters)}m<br>Azimuth: ${Math.round(azimuthDeg)}° · Elevation: ${Math.round(solarAltitude)}°`).addTo(shadeLayerGroup);
      });
    }

    // Render Night Streetlights & Crime Hazard Corridors
    function renderNightLighting() {
      lightingLayerGroup.clearLayers();

      const litSpines = [
        [[-6.2014, 106.8227], [-6.2088, 106.8219], [-6.2145, 106.8184], [-6.2253, 106.8027]],
        [[-6.2374, 106.7836], [-6.2360, 106.7830], [-6.2345, 106.7820]],
        [[-6.2265, 106.8582], [-6.2245, 106.8340], [-6.2275, 106.8290]]
      ];

      litSpines.forEach(spine => {
        L.polyline(spine, { color: '#fbbf24', weight: 4.5, opacity: 0.65, dashArray: '4, 6' })
          .bindPopup('<b>Continuous Luminaire Corridor</b><br>Lighting Index: 2/2 · Active 24h Commercial Frontage').addTo(lightingLayerGroup);
      });

      const darkAlleys = [
        [[-6.2355, 106.7845], [-6.2335, 106.7830]],
        [[-6.2025, 106.8247], [-6.2045, 106.8270]],
        [[-6.2220, 106.8380], [-6.2240, 106.8370]]
      ];

      darkAlleys.forEach(alley => {
        L.polyline(alley, { color: '#ef4444', weight: 3.5, opacity: 0.85, dashArray: '4, 4' })
          .bindPopup('<b>⚠️ Nocturnal Hazard: Unlit Alley (Gang Tikus)</b><br>Lighting: 0/2 · Open roadside ditch (got) · High mugging risk').addTo(lightingLayerGroup);
      });
    }

    // Render Wheelchair Accessible Nodes
    function renderWheelchairNodes() {
      wheelchairLayerGroup.clearLayers();

      const wheelchairNodes = [
        { name: "MRT Fatmawati Dual Lifts (A1/A2)", lat: -6.2926, lon: 106.7935, slope: "3.5%", note: "Step-free from Wisma Cheshire" },
        { name: "MRT Dukuh Atas Elevator D1", lat: -6.2015, lon: 106.8226, slope: "4.2%", note: "Direct concourse-to-platform underground lift" },
        { name: "KRL Sudirman West Platform Lift", lat: -6.2024, lon: 106.8233, slope: "2.5%", note: "Verified operational concourse lift to Terowongan Kendal" },
        { name: "JPM Dukuh Atas Moving Ramp", lat: -6.2028, lon: 106.8248, slope: "4.2%", note: "Permen PUPR 14/2017 compliant moving ramp" },
        { name: "KRL Kebayoran Accessible Ramp", lat: -6.2372, lon: 106.7835, slope: "4.8%", note: "Skybridge to Transjakarta Corridor 13 with lift" },
        { name: "BNI City Airport Rail Lift", lat: -6.2018, lon: 106.8214, slope: "2.0%", note: "Luggage & wheelchair express lift to JPM Level 2" },
        { name: "Wisma Cheshire Indonesia Ramp", lat: -6.2917, lon: 106.7952, slope: "3.5%", note: "Permanent wheelchair residential center ground-truth anchor" }
      ];

      wheelchairNodes.forEach(node => {
        L.circleMarker([node.lat, node.lon], {
          radius: 7, fillColor: '#10b981', color: '#ffffff', weight: 2, fillOpacity: 0.95
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
        renderHeadToHeadRoute(false);
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
      const p = ROUTE_PRESETS[presetKey];
      if (p && p.defaultTime) {
        setTimeOfDay(p.defaultTime);
      } else {
        renderRouteSolution();
      }
    }

    function onH2HScenarioChange(presetKey) {
      currentPreset = presetKey;
      document.getElementById('route-preset-select').value = presetKey;
      renderHeadToHeadRoute(false);
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

    // Time of Day Slider & Presets
    function onTimeSliderChange(sliderVal) {
      const totalMinutes = parseInt(sliderVal);
      const hours = Math.floor(totalMinutes / 60);
      const mins = totalMinutes % 60;
      const timeStr = `${String(hours).padStart(2, '0')}:${String(mins).padStart(2, '0')}`;
      setTimeOfDay(timeStr, false);
    }

    function setTimeOfDay(timeStr, updateSlider = true) {
      currentTimeOfDay = timeStr;
      if (updateSlider) {
        const [h, m] = timeStr.split(':').map(Number);
        document.getElementById('time-scrubber-input').value = h * 60 + m;
      }

      document.querySelectorAll('.time-pill').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-time') === timeStr);
      });

      updateMicroclimateState(timeStr);
      renderSolarShades(timeStr);
      if (currentTab === 'router') {
        renderRouteSolution();
      } else if (currentTab === 'head2head') {
        renderHeadToHeadRoute(false);
      }
    }

    function updateMicroclimateState(timeStr) {
      const hudTemp = document.getElementById('hud-temp');
      const hudUv = document.getElementById('hud-uv');
      const hudWalkCap = document.getElementById('hud-walkcap');
      const hudCurfew = document.getElementById('hud-curfew');

      const [hours, minutes] = timeStr.split(':').map(Number);
      const totalMinutes = hours * 60 + minutes;

      if (totalMinutes >= 420 && totalMinutes < 630) {
        // Morning Peak 07:00 - 10:30
        hudTemp.innerText = '29.2°C / 31.0°C';
        hudTemp.className = 'metric-val';
        hudUv.innerText = '4.2 (Moderate)';
        hudWalkCap.innerText = '700 m';
        hudCurfew.innerText = 'Morning Peak (High Freq)';
        hudCurfew.style.color = '#38bdf8';
        if (currentBasemap === 'dark') setBasemap('light');
      } else if (totalMinutes >= 630 && totalMinutes < 930) {
        // Midday Peak Sun 10:30 - 15:30
        hudTemp.innerText = '33.8°C / 35.2°C';
        hudTemp.className = 'metric-val hot';
        hudUv.innerText = '8.4 (Very High)';
        hudWalkCap.innerText = '350 m (Cap)';
        hudCurfew.innerText = 'Extreme Thermal Peak';
        hudCurfew.style.color = '#f59e0b';
        if (currentBasemap === 'dark') setBasemap('light');
      } else if (totalMinutes >= 930 && totalMinutes < 1140) {
        // Evening Peak 15:30 - 19:00
        hudTemp.innerText = '31.2°C / 32.8°C';
        hudTemp.className = 'metric-val';
        hudUv.innerText = '2.1 (Low)';
        hudWalkCap.innerText = '650 m';
        hudCurfew.innerText = 'Evening Rush Hour';
        hudCurfew.style.color = '#10b981';
        if (currentBasemap === 'dark') setBasemap('light');
      } else {
        // Night 19:00 - 07:00
        hudTemp.innerText = '26.8°C / 27.5°C';
        hudTemp.className = 'metric-val cool';
        hudUv.innerText = '0.0 (Night)';
        hudWalkCap.innerText = '800 m';
        hudCurfew.innerText = 'Late Curfew (Feeder Cutoff)';
        hudCurfew.style.color = '#fbbf24';
        if (currentBasemap !== 'dark') setBasemap('dark');
      }
    }

    // Render Route Solution for 4-Pillar Router
    function renderRouteSolution() {
      activeRouteLayerGroup.clearLayers();
      pulseLayerGroup.clearLayers();
      resetJourneySimulation();

      const presetData = ROUTE_PRESETS[currentPreset];
      if (!presetData) return;

      const solution = presetData.pillars[currentPillar] || presetData.pillars['fastest'];

      // Header Tagline
      document.getElementById('preset-active-case-tag').innerText = presetData.tagline;
      document.getElementById('route-title-header').innerText = presetData.name;
      document.getElementById('route-arrival-clock').innerText = `Arrival ~${solution.arrivalTime}`;

      // KPIs
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

      // Timeline Breakdown Bar
      document.getElementById('timeline-breakdown-text').innerText = solution.breakdownText;
      document.getElementById('bar-feeder').style.width = solution.barFeederPct + '%';
      document.getElementById('bar-rail').style.width = solution.barRailPct + '%';
      document.getElementById('bar-walk').style.width = solution.barWalkPct + '%';

      // Alert Banner
      const alertsContainer = document.getElementById('dynamic-alerts-container');
      const alert = solution.alert || { type: 'tariff', icon: '⚡', title: 'Route Verified', desc: 'Optimal path computed.' };
      alertsContainer.innerHTML = `
        <div class="alert-banner ${alert.type}">
          <span class="alert-icon">${alert.icon}</span>
          <div><strong>${alert.title}:</strong> ${alert.desc}</div>
        </div>
      `;

      // Turn-by-Turn Steps
      const stepsContainer = document.getElementById('steps-list-container');
      document.getElementById('step-count-badge').innerText = solution.steps.length + ' Steps';
      let stepsHtml = '';
      solution.steps.forEach((st, idx) => {
        stepsHtml += `
          <div class="step-card" id="step-card-${idx}" onclick="onStepCardClick(${idx}, [${st.coord[0]}, ${st.coord[1]}])">
            <div class="step-num-badge">${idx + 1}</div>
            <div class="step-info">
              <div class="step-title-row">
                <span class="step-title">${st.title}</span>
                <span class="step-time-badge">${st.time}</span>
              </div>
              <div class="step-desc">${st.desc}</div>
              <div class="step-meta-row">
                <span class="step-meta-pill"><i data-lucide="navigation-2" style="width: 10px; height: 10px;"></i> ${st.dist}</span>
                <span class="step-meta-pill"><i data-lucide="shield-check" style="width: 10px; height: 10px;"></i> ${st.meta}</span>
              </div>
            </div>
          </div>
        `;
      });
      stepsContainer.innerHTML = stepsHtml;
      lucide.createIcons();

      // Render Active Glowing Polylines on Map
      if (solution.segments) {
        solution.segments.forEach((seg, idx) => {
          let color = '#38bdf8';
          if (seg.mode === 'rail' || seg.mode === 'mrt' || seg.mode === 'lrt') color = '#6366f1';
          else if (seg.mode === 'walk') color = '#10b981';
          else if (seg.mode === 'feeder') color = '#38bdf8';

          // Outer Glow Line
          L.polyline(seg.coords, {
            color: color, weight: 8, opacity: 0.35, lineCap: 'round'
          }).addTo(activeRouteLayerGroup);

          // Inner Solid Line
          const poly = L.polyline(seg.coords, {
            color: color, weight: 5, opacity: 0.95, lineCap: 'round'
          }).bindPopup(`<b>${seg.name}</b><br>Mode: ${seg.mode.toUpperCase()}<br>Duration: ${seg.time}`).addTo(activeRouteLayerGroup);

          // Click polyline -> sync to sidebar card
          poly.on('click', () => {
            highlightStepCard(idx);
          });
        });

        // Origin and Destination Radar Pulse Rings
        const allPoints = solution.segments.flatMap(s => s.coords);
        if (allPoints.length > 0) {
          const originCoord = allPoints[0];
          const destCoord = allPoints[allPoints.length - 1];

          // Origin Pulse
          L.marker(originCoord, {
            icon: L.divIcon({
              html: '<div style="position:relative;"><div class="pulse-ring-element"></div><div style="width:14px; height:14px; border-radius:50%; background:#38bdf8; border:2px solid #fff; box-shadow:0 0 10px #38bdf8;"></div></div>',
              className: 'pulse-icon-origin', iconSize: [14, 14], iconAnchor: [7, 7]
            })
          }).bindPopup('<b>Trip Origin</b>').addTo(pulseLayerGroup);

          // Destination Pulse
          L.marker(destCoord, {
            icon: L.divIcon({
              html: '<div style="position:relative;"><div class="pulse-ring-element pulse-ring-dest"></div><div style="width:14px; height:14px; border-radius:50%; background:#f43f5e; border:2px solid #fff; box-shadow:0 0 10px #f43f5e;"></div></div>',
              className: 'pulse-icon-dest', iconSize: [14, 14], iconAnchor: [7, 7]
            })
          }).bindPopup('<b>Trip Destination</b>').addTo(pulseLayerGroup);

          map.fitBounds(allPoints, { padding: [45, 45] });
        }
      }
    }

    // Step Card Click -> Map Highlight
    function onStepCardClick(idx, coord) {
      highlightStepCard(idx);
      map.flyTo(coord, 16, { duration: 0.8 });
    }

    function highlightStepCard(idx) {
      document.querySelectorAll('.step-card').forEach((c, i) => {
        c.classList.toggle('active-step', i === idx);
      });
      const targetCard = document.getElementById(`step-card-${idx}`);
      if (targetCard) {
        targetCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }

    // Map Click -> Sidebar Scroll Sync
    function syncMapClickToSidebar(stationName) {
      const presetData = ROUTE_PRESETS[currentPreset];
      if (!presetData) return;
      const solution = presetData.pillars[currentPillar] || presetData.pillars['fastest'];
      
      const foundIdx = solution.steps.findIndex(s => s.title.toLowerCase().includes(stationName.toLowerCase()) || s.desc.toLowerCase().includes(stationName.toLowerCase()));
      if (foundIdx !== -1) {
        highlightStepCard(foundIdx);
      }
    }

    // Render Google Maps vs Pijak Head-to-Head
    function renderHeadToHeadRoute(animate = false) {
      activeRouteLayerGroup.clearLayers();
      pulseLayerGroup.clearLayers();
      resetJourneySimulation();

      const h2h = ROUTE_PRESETS[currentPreset] || ROUTE_PRESETS['preset_bsd_kebayoran'];
      const pijak = h2h.pillars['fastest'];
      const gmaps = h2h.gmaps;

      // Update Head to Head Banner & Cards
      document.getElementById('h2h-scenario-select').value = h2h.id;
      document.getElementById('h2h-banner-title').innerHTML = `<i data-lucide="swords" style="width:18px;height:18px;color:#ef4444;"></i> ${h2h.name}`;
      document.getElementById('h2h-banner-sub').innerHTML = `
        <strong>${h2h.tagline}</strong><br />
        Standard Failure vs. Pijak Multimodal Benchmark
      `;

      // GMaps Card
      document.getElementById('h2h-gmaps-badge').innerText = gmaps.failBadge;
      document.getElementById('h2h-gmaps-time').innerText = gmaps.travelTime;
      document.getElementById('h2h-gmaps-walk').innerText = gmaps.walkExposure;
      document.getElementById('h2h-gmaps-fare').innerText = gmaps.fare;
      let gmapsHtml = '';
      gmaps.failPoints.forEach(pt => {
        gmapsHtml += `<div class="h2h-details-item"><i data-lucide="alert-triangle" style="color:#f87171;"></i><span>${pt}</span></div>`;
      });
      document.getElementById('h2h-gmaps-list').innerHTML = gmapsHtml;

      // Pijak Card
      document.getElementById('h2h-pijak-badge').innerText = h2h.pijak.winBadge;
      document.getElementById('h2h-pijak-time').innerText = h2h.pijak.travelTime;
      document.getElementById('h2h-pijak-walk').innerText = h2h.pijak.walkExposure;
      document.getElementById('h2h-pijak-fare').innerText = h2h.pijak.fare;
      let pijakHtml = '';
      h2h.pijak.winPoints.forEach(pt => {
        pijakHtml += `<div class="h2h-details-item"><i data-lucide="check-circle" style="color:#34d399;"></i><span>${pt}</span></div>`;
      });
      document.getElementById('h2h-pijak-list').innerHTML = pijakHtml;

      // Matrix Table
      let matrixHtml = '';
      h2h.matrix.forEach(row => {
        matrixHtml += `
          <tr>
            <td><strong>${row[0]}</strong></td>
            <td class="bad">${row[1]}</td>
            <td class="good">${row[2]} <span style="font-size:9.5px;color:#38bdf8;">(${row[3]})</span></td>
          </tr>
        `;
      });
      document.getElementById('h2h-matrix-body').innerHTML = matrixHtml;
      lucide.createIcons();

      // Render Google Maps Detour (Red Dashed Line)
      L.polyline(gmaps.coords, {
        color: '#ef4444', weight: 4.5, opacity: 0.85, dashArray: '8, 6'
      }).bindPopup(`<b>Google Maps Failure Route</b><br>${gmaps.failTitle}<br>Travel Time: ${gmaps.travelTime}`).addTo(activeRouteLayerGroup);

      // Render Pijak Multimodal Route (Solid Colors)
      pijak.segments.forEach(seg => {
        let color = '#38bdf8';
        if (seg.mode === 'rail' || seg.mode === 'mrt') color = '#6366f1';
        if (seg.mode === 'walk') color = '#10b981';

        L.polyline(seg.coords, { color: color, weight: 6, opacity: 0.95 }).addTo(activeRouteLayerGroup);
      });

      const allPoints = [...gmaps.coords, ...pijak.segments.flatMap(s => s.coords)];
      map.fitBounds(allPoints, { padding: [50, 50] });

      if (animate) {
        toggleJourneySimulation();
      }
    }

    // Animated Journey Simulator Engine
    function setSimSpeed(spd) {
      simSpeedMultiplier = spd;
      document.querySelectorAll('.sim-speed-btn').forEach(btn => {
        btn.classList.toggle('active', btn.id === `sim-spd-${spd}`);
      });
      if (isSimulating) {
        // Restart interval at new speed
        clearInterval(simInterval);
        startSimulationLoop();
      }
    }

    function toggleJourneySimulation() {
      if (isSimulating) {
        pauseJourneySimulation();
      } else {
        startJourneySimulation();
      }
    }

    function startJourneySimulation() {
      isSimulating = true;
      document.getElementById('sim-run-text').innerText = 'Pause Journey';
      document.getElementById('sim-run-icon').setAttribute('data-lucide', 'pause');
      document.getElementById('sim-floating-hud').style.display = 'flex';
      lucide.createIcons();

      const presetData = ROUTE_PRESETS[currentPreset];
      const solution = presetData.pillars[currentPillar] || presetData.pillars['fastest'];
      
      // Flatten coords with metadata
      let flatSteps = [];
      solution.segments.forEach((seg, sIdx) => {
        for (let i = 0; i < seg.coords.length; i++) {
          flatSteps.push({
            coord: seg.coords[i],
            mode: seg.mode,
            name: seg.name,
            speed: seg.speed || '25 km/h',
            segIdx: sIdx,
            progress: Math.round(((flatSteps.length + 1) / 30) * 100)
          });
        }
      });

      if (flatSteps.length < 2) return;

      simulationLayerGroup.clearLayers();
      let stepIdx = 0;

      // Create Commuter Marker with dynamic icon
      simCommuterMarker = L.marker(flatSteps[0].coord, {
        icon: L.divIcon({
          html: '<div style="position:relative; width:34px; height:34px;"><div class="pulse-ring-element" style="border-color:#38bdf8;"></div><div id="commuter-avatar-elem" style="width:34px; height:34px; border-radius:50%; background:#0284c7; border:2px solid #fff; box-shadow:0 0 14px #38bdf8; display:flex; align-items:center; justify-content:center; font-size:16px;">🚶‍♂️</div></div>',
          className: 'commuter-marker-icon', iconSize: [34, 34], iconAnchor: [17, 17]
        })
      }).addTo(simulationLayerGroup);

      window.simData = { steps: flatSteps, currentIdx: 0 };
      startSimulationLoop();
    }

    function startSimulationLoop() {
      const delay = Math.max(300 / simSpeedMultiplier, 80);
      simInterval = setInterval(() => {
        if (!window.simData) return;
        const { steps, currentIdx } = window.simData;

        if (currentIdx >= steps.length) {
          pauseJourneySimulation();
          document.getElementById('sim-hud-title').innerText = 'Destination Arrived! Safe & On-Time';
          document.getElementById('sim-hud-sub').innerText = 'Journey completed successfully.';
          return;
        }

        const cur = steps[currentIdx];
        simCommuterMarker.setLatLng(cur.coord);
        
        // Auto-center map smoothly
        map.panTo(cur.coord, { animate: true, duration: 0.25 });

        // Update commuter avatar icon
        const avatarElem = document.getElementById('commuter-avatar-elem');
        let modeIcon = '🚶‍♂️';
        let modeName = 'Walking';
        if (cur.mode === 'rail') { modeIcon = '🚆'; modeName = 'KRL Rail'; }
        else if (cur.mode === 'mrt') { modeIcon = '🚇'; modeName = 'MRT Subsurface'; }
        else if (cur.mode === 'lrt') { modeIcon = '🚊'; modeName = 'LRT Transit'; }
        else if (cur.mode === 'feeder') { modeIcon = '🚐'; modeName = 'Feeder Bus'; }
        else if (cur.mode === 'lift') { modeIcon = '🛗'; modeName = 'Station Lift'; }

        if (avatarElem) avatarElem.innerText = modeIcon;

        // Update HUD
        document.getElementById('sim-hud-mode').innerHTML = `<span>${modeIcon}</span> <span>${modeName}</span>`;
        document.getElementById('sim-hud-title').innerText = `${cur.name}`;
        document.getElementById('sim-hud-speed').innerText = `${cur.speed}`;
        document.getElementById('sim-hud-progress').innerText = `Point ${currentIdx + 1} of ${steps.length}`;

        // Sync with sidebar card
        highlightStepCard(cur.segIdx);

        window.simData.currentIdx++;
      }, delay);
    }

    function pauseJourneySimulation() {
      isSimulating = false;
      if (simInterval) { clearInterval(simInterval); simInterval = null; }
      document.getElementById('sim-run-text').innerText = 'Resume Journey';
      document.getElementById('sim-run-icon').setAttribute('data-lucide', 'play');
      lucide.createIcons();
    }

    function resetJourneySimulation() {
      pauseJourneySimulation();
      simulationLayerGroup.clearLayers();
      document.getElementById('sim-floating-hud').style.display = 'none';
      document.getElementById('sim-run-text').innerText = 'Simulate Journey';
      window.simData = null;
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
        if (filterType === 'all') r.style.display = '';
        else if (filterType === 'high') r.style.display = (pct >= 90) ? '' : 'none';
        else if (filterType === 'mid') r.style.display = (pct > 0 && pct < 90) ? '' : 'none';
        else if (filterType === 'zero') r.style.display = (pct === 0) ? '' : 'none';
      });
    }

    // Quick Station Focus
    function focusStation(stationId) {
      const st = STATIONS.find(s => s.id === stationId);
      if (st) {
        map.flyTo([st.lat, st.lon], 16, { duration: 1.2 });
      }
    }

    function recenterMap() {
      if (currentTab === 'head2head') {
        renderHeadToHeadRoute(false);
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
        if (isVisible) map.addLayer(grp);
        else map.removeLayer(grp);
      }
    }
  </script>
</body>
</html>
"""
