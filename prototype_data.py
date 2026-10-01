# prototype_data.py
# Comprehensive spatial presets, stations, and scenarios for Pijak Prototype

STATIONS_DATA = [
    {"id": "binus_bsd", "name": "Apple Dev Academy @ BINUS (BSD)", "type": "origin", "lat": -6.3023, "lon": 106.6522, "desc": "Campus transit pick-up bay at Green Office Park 9 (GOP 9)"},
    {"id": "rawa_buntu", "name": "Stasiun KRL Rawa Buntu", "type": "krl", "lat": -6.3204, "lon": 106.6718, "desc": "KRL Commuter Line Green Line (Rangkasbitung Line)"},
    {"id": "sudimara", "name": "Stasiun KRL Sudimara", "type": "krl", "lat": -6.2952, "lon": 106.7115, "desc": "KRL Commuter Line Green Line"},
    {"id": "jurang_mangu", "name": "Stasiun KRL Jurang Mangu", "type": "krl", "lat": -6.2844, "lon": 106.7303, "desc": "Bintaro Xchange Transit Hub"},
    {"id": "pondok_ranji", "name": "Stasiun KRL Pondok Ranji", "type": "krl", "lat": -6.2750, "lon": 106.7454, "desc": "KRL Commuter Line Green Line"},
    {"id": "kebayoran", "name": "Stasiun KRL Kebayoran", "type": "krl", "lat": -6.2374, "lon": 106.7836, "desc": "Skybridge connection to Transjakarta Corridor 13 (Velbak)"},
    {"id": "palmerah", "name": "Stasiun KRL Palmerah", "type": "krl", "lat": -6.2081, "lon": 106.7972, "desc": "KRL Green Line station near DPR/MPR & Gelora"},
    {"id": "tanah_abang", "name": "Stasiun KRL Tanah Abang", "type": "krl", "lat": -6.1856, "lon": 106.8110, "desc": "Major Commuter Line Interchange (Green & Loop Line)"},
    {"id": "kuburan_lama", "name": "Jl. Kuburan Lama (Palmerah / Kebayoran)", "type": "dest", "lat": -6.2345, "lon": 106.7820, "desc": "Destination residential zone off Jl. Kebayoran Lama commercial spine"},
    {"id": "dukuh_atas_mrt", "name": "Stasiun MRT Dukuh Atas BNI", "type": "mrt", "lat": -6.2014, "lon": 106.8227, "desc": "Multimodal TOD Spine, North-South Line"},
    {"id": "menara_bca", "name": "Menara BCA / Grand Indonesia", "type": "dest", "lat": -6.1955, "lon": 106.8218, "desc": "Prime Commercial & Retail Tower (East Mall Entrance)"},
    {"id": "sudirman_krl", "name": "Stasiun KRL Sudirman", "type": "krl", "lat": -6.2024, "lon": 106.8233, "desc": "KRL Cikarang / Loop Line trunk station"},
    {"id": "bni_city", "name": "Stasiun BNI City (KA Bandara)", "type": "airport", "lat": -6.2018, "lon": 106.8214, "desc": "Soekarno-Hatta Airport Rail Link (Basoetta)"},
    {"id": "dukuh_atas_lrt", "name": "Stasiun LRT Dukuh Atas", "type": "lrt", "lat": -6.2028, "lon": 106.8248, "desc": "LRT Jabodebek Cibubur & Bekasi Lines terminus"},
    {"id": "setiabudi_lrt", "name": "Stasiun LRT Setiabudi", "type": "lrt", "lat": -6.2088, "lon": 106.8290, "desc": "LRT Jabodebek Station with JPM pedestrian skybridge"},
    {"id": "tebet_krl", "name": "Stasiun KRL Tebet", "type": "krl", "lat": -6.2265, "lon": 106.8582, "desc": "KRL Bogor Line transit hub with JakLingko feeder integration"},
    {"id": "mega_kuningan", "name": "Mega Kuningan Financial District", "type": "dest", "lat": -6.2285, "lon": 106.8275, "desc": "Central Business District (Menara BTPN / Bellagio)"},
    {"id": "bundaran_hi", "name": "Stasiun MRT Bundaran HI", "type": "mrt", "lat": -6.1925, "lon": 106.8231, "desc": "North terminus of MRT Line 1 (Plaza Indonesia concourse)"},
    {"id": "setiabudi_mrt", "name": "Stasiun MRT Setiabudi Astra", "type": "mrt", "lat": -6.2088, "lon": 106.8219, "desc": "MRT North-South Line"},
    {"id": "benhil_mrt", "name": "Stasiun MRT Bendungan Hilir", "type": "mrt", "lat": -6.2145, "lon": 106.8184, "desc": "MRT North-South Line"},
    {"id": "istora_mrt", "name": "Stasiun MRT Istora Mandiri", "type": "mrt", "lat": -6.2195, "lon": 106.8080, "desc": "Gelora Bung Karno East Gate"},
    {"id": "senayan_mrt", "name": "Stasiun MRT Senayan", "type": "mrt", "lat": -6.2253, "lon": 106.8027, "desc": "Senayan commercial and sports center"},
    {"id": "csw_asean", "name": "CSW / ASEAN Multimodal Interchange", "type": "mrt", "lat": -6.2386, "lon": 106.7988, "desc": "Iconic 5-level interchange: MRT ASEAN + TJ Corridor 1 & 13"},
    {"id": "blok_m", "name": "Stasiun MRT Blok M BCA", "type": "mrt", "lat": -6.2445, "lon": 106.7981, "desc": "Major transit hub with integrated bus terminal"},
    {"id": "fatmawati", "name": "Stasiun MRT Fatmawati Indomaret", "type": "mrt", "lat": -6.2928, "lon": 106.7937, "desc": "Elevated MRT station with accessible lifts and tactile paths"},
    {"id": "wisma_cheshire", "name": "Wisma Cheshire Indonesia", "type": "accessibility", "lat": -6.2917, "lon": 106.7952, "desc": "Residential home for persons with severe physical disabilities (320m from MRT Fatmawati)"}
]

BUILDINGS_DATA = [
    {"name": "Wisma 46 (BNI)", "height": 262, "lat": -6.2030, "lon": 106.8215, "radius": 25},
    {"name": "Menara Astra", "height": 261, "lat": -6.2065, "lon": 106.8220, "radius": 28},
    {"name": "Menara BCA", "height": 230, "lat": -6.1955, "lon": 106.8218, "radius": 28},
    {"name": "Grand Indonesia East/West", "height": 160, "lat": -6.1945, "lon": 106.8205, "radius": 40},
    {"name": "UOB Plaza / Thamrin Nine", "height": 383, "lat": -6.1995, "lon": 106.8225, "radius": 32},
    {"name": "Chase Plaza", "height": 110, "lat": -6.2085, "lon": 106.8210, "radius": 22},
    {"name": "Indofood Tower", "height": 192, "lat": -6.2078, "lon": 106.8228, "radius": 26},
    {"name": "Shangri-La Jakarta", "height": 140, "lat": -6.2038, "lon": 106.8190, "radius": 35},
    {"name": "Dukuh Atas TOD Hub / JPM", "height": 38, "lat": -6.2020, "lon": 106.8235, "radius": 22},
    {"name": "Menara BTPN (Mega Kuningan)", "height": 164, "lat": -6.2285, "lon": 106.8275, "radius": 25},
    {"name": "World Capital Tower", "height": 244, "lat": -6.2295, "lon": 106.8260, "radius": 28}
]

PRESETS_DATA = {
    "preset_bsd_kebayoran": {
        "id": "preset_bsd_kebayoran",
        "name": "Apple Dev Academy (BSD) ➔ Jl. Kuburan Lama",
        "tagline": "Case 1 · Late-Night Curfew Commute (22:30 WIB)",
        "defaultTime": "22:30",
        "gmaps": {
            "travelTime": "3h 32m – 7h 50m",
            "walkExposure": "47 min unlit got",
            "fare": "Rp 92.000+ (Taxi)",
            "failBadge": "Curfew Failure",
            "failTitle": "The Kalideres/Airport Detour & Dark Alley Walk",
            "failPoints": [
                "Fails to chain first-mile feeder to KRL; routes commuter 38 km north via expressway shoulders.",
                "Directs commuter into pitch-black suburban alleys (gang tikus) with open gutters (got).",
                "Flags transit as 'Unavailable until 03:35 AM tomorrow' or forces surge-priced private taxi."
            ],
            "coords": [
                [-6.3023, 106.6522], [-6.2800, 106.6600], [-6.2400, 106.6700],
                [-6.1900, 106.6800], [-6.1550, 106.7050], [-6.1580, 106.7400],
                [-6.1650, 106.7700], [-6.1900, 106.7900], [-6.2081, 106.7972],
                [-6.2200, 106.7900], [-6.2345, 106.7820]
            ]
        },
        "pijak": {
            "travelTime": "40 min Total",
            "walkExposure": "8 min (Lit)",
            "fare": "Rp 3.000",
            "winBadge": "Proven Solution",
            "winTitle": "Synchronized Multimodal Feeder + KRL Trunk",
            "winPoints": [
                "Feeder Integration: 6-min shuttle/ojol drop-off at Stasiun Rawa Buntu North Gate.",
                "KRL Express Trunk: 26-min high-speed Commuter Line directly to Kebayoran (Rp 3.000).",
                "Passive Surveillance: 8-min walk strictly routed along Jl. Kebayoran Lama commercial spine with active 24h warung."
            ]
        },
        "matrix": [
            ["Total Travel Duration", "3h 32m – 7h 50m", "40 min (Arrival 23:18)", "91% Faster"],
            ["Out-of-Pocket Fare", "Rp 92.000+ (Taxi)", "Rp 3.000 (KRL)", "Saves Rp 89.000"],
            ["Pedestrian Dark Exposure", "47 min unlit got", "8 min continuous light", "Zero unlit alleys"],
            ["Crime / Begal Vulnerability", "Severe (Gang Tikus)", "Protected (Commercial Spine)", "Continuous Eyes on Street"],
            ["Wheelchair Feasibility", "0% (Overpass Stairs)", "100% Step-Free Ramps & Lifts", "Permen PUPR Compliant"]
        ],
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
                "alert": {
                    "type": "night",
                    "icon": "🌙",
                    "title": "Night Safety Active (22:30 WIB)",
                    "desc": "Bypassed unlit alleyways; routed along illuminated commercial corridor with 24h storefronts, CCTV, and continuous streetlamps."
                },
                "steps": [
                    {"title": "Depart Apple Developer Academy @ BINUS", "time": "22:30 WIB", "desc": "Walk 50m to GOP 9 campus multimodal pick-up bay.", "dist": "50m", "meta": "Lit Campus Bay", "mode": "walk", "coord": [-6.3023, 106.6522]},
                    {"title": "Board Feeder Shuttle to Stn. Rawa Buntu", "time": "22:32 WIB", "desc": "Transit connector via Jl. BSD Grand Boulevard directly to Stasiun Rawa Buntu.", "dist": "3.2 km", "meta": "In-vehicle (6 min)", "mode": "feeder", "coord": [-6.3120, 106.6620]},
                    {"title": "Tap In at Stasiun KRL Rawa Buntu", "time": "22:39 WIB", "desc": "Tap in at fare gates (Platform 1, Direction Tanah Abang). Synchronized transfer.", "dist": "30m", "meta": "Fare: Rp 3.000", "mode": "rail", "coord": [-6.3204, 106.6718]},
                    {"title": "Board KRL Commuter Line (Green Line)", "time": "22:42 WIB", "desc": "Ride 4 stops: Sudimara, Jurang Mangu, Pondok Ranji to Stasiun Kebayoran.", "dist": "16.5 km", "meta": "Air-conditioned (26 min)", "mode": "rail", "coord": [-6.2750, 106.7454]},
                    {"title": "Alight Stn. Kebayoran & Walk to Jl. Kuburan Lama", "time": "23:10 WIB", "desc": "Exit North concourse; walk 550m along illuminated sidewalk on Jl. Kebayoran Lama.", "dist": "550m", "meta": "Lighting 2/2 · 0 steps", "mode": "walk", "coord": [-6.2345, 106.7820]}
                ],
                "segments": [
                    {"name": "Campus Feeder Shuttle", "mode": "feeder", "time": "6 min", "speed": "32 km/h", "coords": [[-6.3023, 106.6522], [-6.3080, 106.6580], [-6.3150, 106.6650], [-6.3204, 106.6718]]},
                    {"name": "KRL Commuter Line (Green Line)", "mode": "rail", "time": "26 min", "speed": "65 km/h", "coords": [[-6.3204, 106.6718], [-6.2952, 106.7115], [-6.2844, 106.7303], [-6.2750, 106.7454], [-6.2374, 106.7836]]},
                    {"name": "Illuminated Last-Mile Walk", "mode": "walk", "time": "8 min", "speed": "4.8 km/h", "coords": [[-6.2374, 106.7836], [-6.2360, 106.7830], [-6.2345, 106.7820]]}
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
                "alert": {
                    "type": "night",
                    "icon": "🛡️",
                    "title": "Maximum Passive Surveillance",
                    "desc": "100% route follows primary commercial arteries with active night street vendors and bright luminaire coverage."
                },
                "steps": [
                    {"title": "GOP 9 Air-Conditioned Shuttle Pick-up", "time": "22:30 WIB", "desc": "Board protected shuttle at GOP 9 lobby directly to Rawa Buntu.", "dist": "3.2 km", "meta": "Comfortable AC", "mode": "feeder", "coord": [-6.3023, 106.6522]},
                    {"title": "Platform Boarding at Stasiun Rawa Buntu", "time": "22:40 WIB", "desc": "Enter via accessible ramp; board quiet carriage.", "dist": "40m", "meta": "Protected Waiting Area", "mode": "rail", "coord": [-6.3204, 106.6718]},
                    {"title": "KRL Commuter Line to Kebayoran", "time": "22:44 WIB", "desc": "Smooth rail journey with CCTV surveillance throughout.", "dist": "16.5 km", "meta": "26 min", "mode": "rail", "coord": [-6.2750, 106.7454]},
                    {"title": "Protected Night Walk via Main Arterial", "time": "23:13 WIB", "desc": "Bypasses dark Gang Kebon Sayur. Uses 100% lit commercial frontage with active warung.", "dist": "580m", "meta": "Eyes on the Street", "mode": "walk", "coord": [-6.2345, 106.7820]}
                ],
                "segments": [
                    {"name": "BSD Comfort Shuttle", "mode": "feeder", "time": "8 min", "speed": "30 km/h", "coords": [[-6.3023, 106.6522], [-6.3080, 106.6580], [-6.3150, 106.6650], [-6.3204, 106.6718]]},
                    {"name": "KRL Commuter Line", "mode": "rail", "time": "26 min", "speed": "65 km/h", "coords": [[-6.3204, 106.6718], [-6.2952, 106.7115], [-6.2844, 106.7303], [-6.2750, 106.7454], [-6.2374, 106.7836]]},
                    {"name": "Lit Commercial Corridor Walk", "mode": "walk", "time": "9 min", "speed": "4.5 km/h", "coords": [[-6.2374, 106.7836], [-6.2365, 106.7832], [-6.2355, 106.7828], [-6.2345, 106.7820]]}
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
                "alert": {
                    "type": "tariff",
                    "icon": "💰",
                    "title": "Zero Extra Markup",
                    "desc": "Total trip utilizes flat statutory Rp 3.000 KRL commuter fare and free student/campus feeder."
                },
                "steps": [
                    {"title": "Board Free Campus Shuttle to Rawa Buntu", "time": "22:30 WIB", "desc": "Zero-fare student connector to Stasiun Rawa Buntu.", "dist": "3.2 km", "meta": "Fare: Rp 0", "mode": "feeder", "coord": [-6.3023, 106.6522]},
                    {"title": "KRL Commuter Line Trunk", "time": "22:42 WIB", "desc": "Standard statutory distance fare (first 25 km is flat Rp 3.000).", "dist": "16.5 km", "meta": "Fare: Rp 3.000", "mode": "rail", "coord": [-6.2750, 106.7454]},
                    {"title": "Walk to Destination via Jl. Kebayoran Lama", "time": "23:12 WIB", "desc": "Direct walk along sidewalk (Rp 0).", "dist": "600m", "meta": "Fare: Rp 0", "mode": "walk", "coord": [-6.2345, 106.7820]}
                ],
                "segments": [
                    {"name": "Campus Shuttle", "mode": "feeder", "time": "10 min", "speed": "28 km/h", "coords": [[-6.3023, 106.6522], [-6.3080, 106.6580], [-6.3150, 106.6650], [-6.3204, 106.6718]]},
                    {"name": "KRL Commuter Line", "mode": "rail", "time": "26 min", "speed": "65 km/h", "coords": [[-6.3204, 106.6718], [-6.2952, 106.7115], [-6.2844, 106.7303], [-6.2750, 106.7454], [-6.2374, 106.7836]]},
                    {"name": "Pedestrian Walk", "mode": "walk", "time": "9 min", "speed": "4.5 km/h", "coords": [[-6.2374, 106.7836], [-6.2360, 106.7830], [-6.2345, 106.7820]]}
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
                "alert": {
                    "type": "wheelchair",
                    "icon": "♿",
                    "title": "Strict Step-Free Verification",
                    "desc": "0 steps encountered. Elevators at Rawa Buntu & Kebayoran verified online. Max cross-slope 4.5% (Permen PUPR 14/2017 compliant)."
                },
                "steps": [
                    {"title": "GOP 9 Accessible Pick-up Bay", "time": "22:30 WIB", "desc": "Flush curb-cut roll onto accessible WAV feeder.", "dist": "30m", "meta": "Slope 3.5%", "mode": "lift", "coord": [-6.3023, 106.6522]},
                    {"title": "Rawa Buntu Station Elevator", "time": "22:40 WIB", "desc": "Street-to-concourse lift to Platform 1. Platform gap < 3cm.", "dist": "50m", "meta": "Operational Lift", "mode": "lift", "coord": [-6.3204, 106.6718]},
                    {"title": "Accessible Carriage KRL", "time": "22:45 WIB", "desc": "Carriage 4 with designated wheelchair securement bays.", "dist": "16.5 km", "meta": "Dedicated Bay", "mode": "rail", "coord": [-6.2750, 106.7454]},
                    {"title": "Stasiun Kebayoran North Lift & Ramp Concourse", "time": "23:14 WIB", "desc": "Platform lift to street level. Continuous 1.8m wide sidewalk with drop-curbs to Jl. Kuburan Lama.", "dist": "580m", "meta": "0 Steps · Slope 4.5%", "mode": "walk", "coord": [-6.2345, 106.7820]}
                ],
                "segments": [
                    {"name": "WAV Feeder", "mode": "feeder", "time": "8 min", "speed": "28 km/h", "coords": [[-6.3023, 106.6522], [-6.3080, 106.6580], [-6.3150, 106.6650], [-6.3204, 106.6718]]},
                    {"name": "Accessible KRL Line", "mode": "rail", "time": "26 min", "speed": "65 km/h", "coords": [[-6.3204, 106.6718], [-6.2952, 106.7115], [-6.2844, 106.7303], [-6.2750, 106.7454], [-6.2374, 106.7836]]},
                    {"name": "Step-Free Ramp Roll", "mode": "walk", "time": "12 min", "speed": "3.5 km/h", "coords": [[-6.2374, 106.7836], [-6.2360, 106.7830], [-6.2345, 106.7820]]}
                ]
            }
        }
    },

    "preset_dukuh_menara_bca": {
        "id": "preset_dukuh_menara_bca",
        "name": "MRT Dukuh Atas ➔ Menara BCA / Grand Indonesia",
        "tagline": "Case 2 · Midday Tropical Heat & CoolWalks (12:00 WIB)",
        "defaultTime": "12:00",
        "gmaps": {
            "travelTime": "18 min (Sun-Baked)",
            "walkExposure": "850 m Unshaded",
            "fare": "Rp 0 (Direct Walk)",
            "failBadge": "Heat Stroke Risk",
            "failTitle": "Direct Sun-Baked Concrete Plaza & Overpass",
            "failPoints": [
                "Routes pedestrian across unshaded concrete plaza on Jl. Jend. Sudirman under UV 8.4 Very High radiation.",
                "Felt temperature surges to 35.2°C; asphalt surface temperature exceeds 52°C, causing severe thermal exhaustion.",
                "Ignores fully air-conditioned and shaded subterranean connectors (Terowongan Kendal and JPM)."
            ],
            "coords": [
                [-6.2014, 106.8227], [-6.2010, 106.8220], [-6.1990, 106.8225],
                [-6.1970, 106.8228], [-6.1960, 106.8225], [-6.1955, 106.8218]
            ]
        },
        "pijak": {
            "travelTime": "7 min Total",
            "walkExposure": "280 m (100% Shaded)",
            "fare": "Rp 0",
            "winBadge": "CoolWalks Optimized",
            "winTitle": "Terowongan Kendal + Dense Mahogany Tree Canopy",
            "winPoints": [
                "100% Solar Shade: Routes through pedestrianized Terowongan Kendal tunnel (UV drops to 0.0).",
                "Thermal Comfort: Dense mahogany tree canopy on Jl. Blora and Jl. Teluk Betung lowers felt temp to 28.5°C (-6.7°C).",
                "Strict Exposure Cap: Walk distance restricted to ≤ 300m sheltered path straight to Menara BCA lobby."
            ]
        },
        "matrix": [
            ["Thermal Exposure (Felt Temp)", "35.2°C (Extreme Heat)", "28.5°C (CoolWalks Shaded)", "6.7°C Temperature Relief"],
            ["Solar UV Radiation Index", "8.4 (Very High / Danger)", "0.0 – 1.2 (Protected)", "86% UV Reduction"],
            ["Direct Sun Walk Distance", "850 m unshaded asphalt", "0 m direct sun (Canopy/Tunnel)", "100% Shaded Path"],
            ["Heat Stroke / Sunburn Risk", "High (>15 min in UV 8.4)", "Zero Risk (Sheltered Corridor)", "Certified Safe for Elderly/Children"],
            ["Walk Duration", "18 min agonizing heat", "7 min refreshing stroll", "61% Time Saved"]
        ],
        "pillars": {
            "fastest": {
                "arrivalTime": "12:07 PM",
                "totalTime": "7 min",
                "timeSub": "Direct Cool Corridor",
                "fare": "Rp 0",
                "fareSub": "Pedestrian Path",
                "walkDist": "280 m",
                "walkTime": "7 min walk",
                "transitTime": "0 min",
                "transitSub": "Pure Walking",
                "comfortScore": "94%",
                "comfortSub": "100% Shaded Tunnel",
                "accessibleScore": "100%",
                "accessibleSub": "0 Steps",
                "breakdownText": "Tunnel (3m) · Shaded Canopy (4m)",
                "barFeederPct": 0,
                "barRailPct": 0,
                "barWalkPct": 100,
                "alert": {
                    "type": "thermal",
                    "icon": "☀️",
                    "title": "Midday Solar Heat Alert (35.2°C Feels-Like)",
                    "desc": "Direct sun paths pruned by CoolWalks ray-casting algorithm. Commuter strictly routed through Terowongan Kendal tunnel and tree canopies."
                },
                "steps": [
                    {"title": "Exit MRT Dukuh Atas via Kendal Concourse", "time": "12:00 PM", "desc": "Take escalators to covered Terowongan Kendal promenade. 100% solar shade.", "dist": "60m", "meta": "UV 0.0 · Temp 27°C", "mode": "walk", "coord": [-6.2014, 106.8227]},
                    {"title": "Traverse Terowongan Kendal Pedestrian Tunnel", "time": "12:02 PM", "desc": "Walk through pedestrianized tunnel with active Difabis coffee stalls and street murals.", "dist": "120m", "meta": "100% Solar Shade", "mode": "walk", "coord": [-6.2005, 106.8223]},
                    {"title": "Shaded Sidewalk on Jl. Blora & Jl. Teluk Betung", "time": "12:04 PM", "desc": "Walk beneath continuous mature mahogany tree canopy. Ambient temp cools to 28.5°C.", "dist": "100m", "meta": "Tree Canopy 92%", "mode": "walk", "coord": [-6.1975, 106.8218]},
                    {"title": "Arrive Menara BCA / Grand Indonesia Lobby", "time": "12:07 PM", "desc": "Direct step-free entrance to Menara BCA East Mall lobby.", "dist": "0m", "meta": "Air-Conditioned Mall", "mode": "walk", "coord": [-6.1955, 106.8218]}
                ],
                "segments": [
                    {"name": "Terowongan Kendal Shaded Promenade", "mode": "walk", "time": "3 min", "speed": "4.5 km/h", "coords": [[-6.2014, 106.8227], [-6.2010, 106.8224], [-6.2000, 106.8222]]},
                    {"name": "Jl. Blora Mahogany Tree Buffer", "mode": "walk", "time": "2 min", "speed": "4.5 km/h", "coords": [[-6.2000, 106.8222], [-6.1985, 106.8220], [-6.1970, 106.8219]]},
                    {"name": "Jl. Teluk Betung Shaded Sidewalk", "mode": "walk", "time": "2 min", "speed": "4.5 km/h", "coords": [[-6.1970, 106.8219], [-6.1960, 106.8218], [-6.1955, 106.8218]]}
                ]
            },
            "comfort": {
                "arrivalTime": "12:06 PM",
                "totalTime": "6 min",
                "timeSub": "Maximum Thermal Relief",
                "fare": "Rp 0",
                "fareSub": "Pedestrian Path",
                "walkDist": "260 m",
                "walkTime": "6 min walk",
                "transitTime": "0 min",
                "transitSub": "Pure Walking",
                "comfortScore": "98%",
                "comfortSub": "Feels Like 27.8°C",
                "accessibleScore": "100%",
                "accessibleSub": "0 Steps",
                "breakdownText": "Tunnel (3m) · Canopy Walk (3m)",
                "barFeederPct": 0,
                "barRailPct": 0,
                "barWalkPct": 100,
                "alert": {
                    "type": "thermal",
                    "icon": "🌳",
                    "title": "Optimal Microclimate Shade Canopy",
                    "desc": "Zero direct sunlight exposure. Ray-casting verifies 98% continuous shade factor $S_e(t)$ along building overhangs."
                },
                "steps": [
                    {"title": "Terowongan Kendal Shaded Departure", "time": "12:00 PM", "desc": "Covered promenade with zero sun exposure.", "dist": "120m", "meta": "UV 0.0", "mode": "walk", "coord": [-6.2014, 106.8227]},
                    {"title": "Building Colonnade & Tree Canopy", "time": "12:03 PM", "desc": "Walk under Grand Indonesia covered retail colonnade.", "dist": "140m", "meta": "100% Covered", "mode": "walk", "coord": [-6.1975, 106.8218]},
                    {"title": "Enter Menara BCA Ground Lobby", "time": "12:06 PM", "desc": "Direct revolving door entry.", "dist": "0m", "meta": "0 Steps", "mode": "walk", "coord": [-6.1955, 106.8218]}
                ],
                "segments": [
                    {"name": "Covered Tunnel Walk", "mode": "walk", "time": "3 min", "speed": "4.5 km/h", "coords": [[-6.2014, 106.8227], [-6.2000, 106.8222]]},
                    {"name": "Grand Indonesia Colonnade", "mode": "walk", "time": "3 min", "speed": "4.5 km/h", "coords": [[-6.2000, 106.8222], [-6.1975, 106.8218], [-6.1955, 106.8218]]}
                ]
            },
            "cheapest": {
                "arrivalTime": "12:07 PM",
                "totalTime": "7 min",
                "timeSub": "Rp 0 Zero Cost",
                "fare": "Rp 0",
                "fareSub": "100% Free Pedestrian",
                "walkDist": "280 m",
                "walkTime": "7 min walk",
                "transitTime": "0 min",
                "transitSub": "Walk",
                "comfortScore": "94%",
                "comfortSub": "Shaded Path",
                "accessibleScore": "100%",
                "accessibleSub": "0 Steps",
                "breakdownText": "Free Shaded Walk (7m)",
                "barFeederPct": 0,
                "barRailPct": 0,
                "barWalkPct": 100,
                "alert": {
                    "type": "tariff",
                    "icon": "💰",
                    "title": "Zero Tariff Walking Connector",
                    "desc": "Direct urban pedestrian shortcut. Completely eliminates taxi drop-off charges or short-hop vehicle fares."
                },
                "steps": [
                    {"title": "Walk via Terowongan Kendal", "time": "12:00 PM", "desc": "Pedestrian tunnel connecting MRT directly to Thamrin-BCA zone.", "dist": "140m", "meta": "Fare: Rp 0", "mode": "walk", "coord": [-6.2014, 106.8227]},
                    {"title": "Canopy Walk to Menara BCA", "time": "12:04 PM", "desc": "Free public sidewalk under tree cover.", "dist": "140m", "meta": "Fare: Rp 0", "mode": "walk", "coord": [-6.1955, 106.8218]}
                ],
                "segments": [
                    {"name": "Free Shaded Connector", "mode": "walk", "time": "7 min", "speed": "4.5 km/h", "coords": [[-6.2014, 106.8227], [-6.2000, 106.8222], [-6.1975, 106.8218], [-6.1955, 106.8218]]}
                ]
            },
            "wheelchair": {
                "arrivalTime": "12:08 PM",
                "totalTime": "8 min",
                "timeSub": "100% Step-Free",
                "fare": "Rp 0",
                "fareSub": "Accessible Walkway",
                "walkDist": "290 m",
                "walkTime": "8 min roll",
                "transitTime": "0 min",
                "transitSub": "Smooth Surface",
                "comfortScore": "96%",
                "comfortSub": "Slope < 2%",
                "accessibleScore": "100%",
                "accessibleSub": "0 Curb Drops",
                "breakdownText": "Concourse Roll (4m) · Paved Ramp (4m)",
                "barFeederPct": 0,
                "barRailPct": 0,
                "barWalkPct": 100,
                "alert": {
                    "type": "wheelchair",
                    "icon": "♿",
                    "title": "Level-Grade Step-Free Corridor",
                    "desc": "Continuous polished concrete and smooth granite paving. Flush transition across Terowongan Kendal with zero threshold obstacles."
                },
                "steps": [
                    {"title": "MRT Dukuh Atas Platform Lift D1", "time": "12:00 PM", "desc": "Take concourse elevator to Kendal street level.", "dist": "30m", "meta": "Elevator Verified", "mode": "lift", "coord": [-6.2014, 106.8227]},
                    {"title": "Roll via Kendal Step-Free Promenade", "time": "12:03 PM", "desc": "Flat grade (slope 1.2%), tactile tiles on right boundary.", "dist": "140m", "meta": "0 Steps · Slope 1.2%", "mode": "walk", "coord": [-6.2000, 106.8222]},
                    {"title": "Enter Menara BCA Step-Free Ramp Gate", "time": "12:06 PM", "desc": "Direct automatic sliding door entrance with flush transition plate.", "dist": "120m", "meta": "Flush Entry (0cm)", "mode": "walk", "coord": [-6.1955, 106.8218]}
                ],
                "segments": [
                    {"name": "Level-Grade Kendal Walk", "mode": "walk", "time": "8 min", "speed": "3.8 km/h", "coords": [[-6.2014, 106.8227], [-6.2000, 106.8222], [-6.1975, 106.8218], [-6.1955, 106.8218]]}
                ]
            }
        }
    },

    "preset_sudirman_dukuh_setiabudi": {
        "id": "preset_sudirman_dukuh_setiabudi",
        "name": "KRL Sudirman ➔ MRT Dukuh Atas ➔ LRT Setiabudi",
        "tagline": "Case 3 · Wheelchair Independent Transit Transfer (14:00 WIB)",
        "defaultTime": "14:00",
        "gmaps": {
            "travelTime": "38 min (Hazardous)",
            "walkExposure": "420 m Broken Sidewalk",
            "fare": "Rp 5.000",
            "failBadge": "Wheelchair Trap",
            "failTitle": "20cm Broken Curb Drops & Slippery Ramps",
            "failPoints": [
                "Routes wheelchair user across busy Jl. Blora vehicular intersection with 20cm broken curb drops and zero curb-cuts.",
                "Directs commuter into steep overpass ramp (>15% gradient), exceeding biomechanical push limits and risking wheelchair tip-over.",
                "Fails to identify non-functioning lifts on Jl. Galunggung; commuter gets trapped on high sidewalk ledge with no escape ramp."
            ],
            "coords": [
                [-6.2024, 106.8233], [-6.2035, 106.8238], [-6.2050, 106.8250],
                [-6.2070, 106.8270], [-6.2088, 106.8290]
            ]
        },
        "pijak": {
            "travelTime": "9 min Total",
            "walkExposure": "380 m (100% Step-Free)",
            "fare": "Rp 3.000",
            "winBadge": "100% Certified Step-Free",
            "winTitle": "JPM Multimodal Bridge & Operational Lifts",
            "winPoints": [
                "Continuous Certified Level Grade: KRL Sudirman West Lift to Kendal promenade (0 steps, <2.5% slope).",
                "JPM Covered Skybridge: Seamless moving ramps and indoor elevators linking MRT Dukuh Atas directly to LRT Setiabudi.",
                "Field-Audit Verified: Every ramp complies with Permen PUPR 14/2017 (slope ≤ 8.33%, tactile guiding blocks intact)."
            ]
        },
        "matrix": [
            ["Step-Free Accessibility", "28% (Trapped by 20cm drop-offs)", "100% (Certified Zero Steps)", "Full Independent Mobility"],
            ["Max Ramp Gradient", ">15% (Dangerous Tip-Over Risk)", "4.2% (Permen PUPR Compliant)", "Biomechanical Strain Safe"],
            ["Elevator Reliability Check", "Unverified (Routes to broken lifts)", "Live API Verified Operational", "Zero Stranded Risk"],
            ["Transfer Time", "38 min struggle & detour", "9 min seamless indoor transfer", "76% Faster Transfer"],
            ["Vehicle Traffic Conflict", "High (Unprotected Jl. Blora cross)", "Zero (Grade-separated JPM)", "100% Pedestrian Safe"]
        ],
        "pillars": {
            "fastest": {
                "arrivalTime": "14:09 WIB",
                "totalTime": "9 min",
                "timeSub": "Direct JPM Link",
                "fare": "Rp 3.000",
                "fareSub": "Integrated TOD",
                "walkDist": "380 m",
                "walkTime": "9 min roll",
                "transitTime": "0 min",
                "transitSub": "Inter-Hub Walk",
                "comfortScore": "96%",
                "comfortSub": "Covered Skybridge",
                "accessibleScore": "100%",
                "accessibleSub": "0 Steps Guaranteed",
                "breakdownText": "Lift Access (2m) · JPM Connector (5m) · LRT Lift (2m)",
                "barFeederPct": 0,
                "barRailPct": 0,
                "barWalkPct": 100,
                "alert": {
                    "type": "wheelchair",
                    "icon": "♿",
                    "title": "100% Step-Free Transit Transfer Verified",
                    "desc": "KRL Sudirman West Lift ➔ Terowongan Kendal level grade ➔ JPM Multiguna skybridge ➔ LRT Setiabudi platform lift. R05 field data audit certified."
                },
                "steps": [
                    {"title": "KRL Sudirman Platform 1 West Lift", "time": "14:00 WIB", "desc": "Take elevator from KRL platform to Kendal street level. 0 threshold bump.", "dist": "30m", "meta": "Lift Operational", "mode": "lift", "coord": [-6.2024, 106.8233]},
                    {"title": "Terowongan Kendal Level Promenade", "time": "14:02 WIB", "desc": "Roll across flat paved promenade to MRT Dukuh Atas entrance.", "dist": "90m", "meta": "Slope 1.8%", "mode": "walk", "coord": [-6.2018, 106.8230]},
                    {"title": "Enter JPM (Jembatan Penyeberangan Multiguna)", "time": "14:04 WIB", "desc": "Elevated multimodal connection bridge with moving walkway and gentle ramps.", "dist": "180m", "meta": "Ramp Slope 4.2%", "mode": "walk", "coord": [-6.2025, 106.8242]},
                    {"title": "LRT Setiabudi Concourse Elevator", "time": "14:07 WIB", "desc": "Direct elevator ride from JPM bridge concourse to LRT train platform.", "dist": "80m", "meta": "Level Platform Gap < 3cm", "mode": "lift", "coord": [-6.2088, 106.8290]}
                ],
                "segments": [
                    {"name": "KRL West Concourse Lift Link", "mode": "walk", "time": "2 min", "speed": "3.5 km/h", "coords": [[-6.2024, 106.8233], [-6.2020, 106.8231]]},
                    {"name": "Kendal Step-Free Promenade", "mode": "walk", "time": "3 min", "speed": "4.0 km/h", "coords": [[-6.2020, 106.8231], [-6.2014, 106.8227], [-6.2020, 106.8238]]},
                    {"name": "JPM Dukuh Atas Skybridge", "mode": "walk", "time": "4 min", "speed": "4.0 km/h", "coords": [[-6.2020, 106.8238], [-6.2028, 106.8248], [-6.2055, 106.8268], [-6.2088, 106.8290]]}
                ]
            },
            "comfort": {
                "arrivalTime": "14:10 WIB",
                "totalTime": "10 min",
                "timeSub": "100% Climate-Controlled",
                "fare": "Rp 3.000",
                "fareSub": "TOD Standard",
                "walkDist": "380 m",
                "walkTime": "10 min roll",
                "transitTime": "0 min",
                "transitSub": "Sheltered Walk",
                "comfortScore": "98%",
                "comfortSub": "Air-Conditioned JPM",
                "accessibleScore": "100%",
                "accessibleSub": "0 Steps",
                "breakdownText": "Indoor Skybridge (10m)",
                "barFeederPct": 0,
                "barRailPct": 0,
                "barWalkPct": 100,
                "alert": {
                    "type": "wheelchair",
                    "icon": "🛋️",
                    "title": "Air-Conditioned Indoor Transfer",
                    "desc": "Fully sheltered from tropical heat and rain. Smooth rubber floor tiles provide superior traction for manual and motorized wheelchairs."
                },
                "steps": [
                    {"title": "KRL Sudirman Elevator", "time": "14:00 WIB", "desc": "Concourse elevator with braille voice annunciator.", "dist": "30m", "meta": "Lift Verified", "mode": "lift", "coord": [-6.2024, 106.8233]},
                    {"title": "JPM Covered Moving Ramps", "time": "14:03 WIB", "desc": "Roll along covered skybridge overlooking Dukuh Atas reservoir.", "dist": "270m", "meta": "Zero Rain / Sun Exposure", "mode": "walk", "coord": [-6.2028, 106.8248]},
                    {"title": "LRT Setiabudi Elevator to Platform", "time": "14:08 WIB", "desc": "Step-free boarding on LRT Jabodebek.", "dist": "80m", "meta": "Level Boarding", "mode": "lift", "coord": [-6.2088, 106.8290]}
                ],
                "segments": [
                    {"name": "Sudirman Concourse Link", "mode": "walk", "time": "3 min", "speed": "3.5 km/h", "coords": [[-6.2024, 106.8233], [-6.2020, 106.8231]]},
                    {"name": "JPM Climate-Controlled Skybridge", "mode": "walk", "time": "7 min", "speed": "3.5 km/h", "coords": [[-6.2020, 106.8231], [-6.2028, 106.8248], [-6.2055, 106.8268], [-6.2088, 106.8290]]}
                ]
            },
            "cheapest": {
                "arrivalTime": "14:09 WIB",
                "totalTime": "9 min",
                "timeSub": "Rp 0 Transfer Walk",
                "fare": "Rp 3.000",
                "fareSub": "Statutory Fare",
                "walkDist": "380 m",
                "walkTime": "9 min roll",
                "transitTime": "0 min",
                "transitSub": "Pedestrian Transfer",
                "comfortScore": "96%",
                "comfortSub": "Free Skybridge",
                "accessibleScore": "100%",
                "accessibleSub": "0 Steps",
                "breakdownText": "Free Step-Free Skybridge (9m)",
                "barFeederPct": 0,
                "barRailPct": 0,
                "barWalkPct": 100,
                "alert": {
                    "type": "tariff",
                    "icon": "💰",
                    "title": "Zero Extra Inter-Hub Surcharge",
                    "desc": "JPM Dukuh Atas is free public pedestrian infrastructure connecting KRL, MRT, and LRT hubs without paying double gate fees."
                },
                "steps": [
                    {"title": "Free Public Transfer via JPM", "time": "14:00 WIB", "desc": "No extra toll or fare to cross between stations.", "dist": "380m", "meta": "Rp 0 Inter-Hub", "mode": "walk", "coord": [-6.2024, 106.8233]}
                ],
                "segments": [
                    {"name": "JPM Free Pedestrian Skybridge", "mode": "walk", "time": "9 min", "speed": "3.8 km/h", "coords": [[-6.2024, 106.8233], [-6.2028, 106.8248], [-6.2088, 106.8290]]}
                ]
            },
            "wheelchair": {
                "arrivalTime": "14:09 WIB",
                "totalTime": "9 min",
                "timeSub": "100% Step-Free Standard",
                "fare": "Rp 3.000",
                "fareSub": "Permen PUPR 14/2017",
                "walkDist": "380 m",
                "walkTime": "9 min roll",
                "transitTime": "0 min",
                "transitSub": "Continuous Tactile",
                "comfortScore": "98%",
                "comfortSub": "Slope 4.2%",
                "accessibleScore": "100%",
                "accessibleSub": "0 Steps Guaranteed",
                "breakdownText": "Lift 1 (2m) · JPM Ramp (5m) · Lift 2 (2m)",
                "barFeederPct": 0,
                "barRailPct": 0,
                "barWalkPct": 100,
                "alert": {
                    "type": "wheelchair",
                    "icon": "♿",
                    "title": "Accessibility Golden Standard",
                    "desc": "Verified continuous path: ramp slope 4.2% (limit is 8.33%), tactile guidance for vision-impaired, and dual elevators in active operational state."
                },
                "steps": [
                    {"title": "KRL Sudirman Platform Elevator", "time": "14:00 WIB", "desc": "Door width 1.1m, wheelchair turning radius 1.5m accommodated.", "dist": "30m", "meta": "100% Compliant", "mode": "lift", "coord": [-6.2024, 106.8233]},
                    {"title": "JPM Accessible Ramp Corridor", "time": "14:03 WIB", "desc": "Continuous handrails at 70cm and 90cm height. Slope 4.2%.", "dist": "270m", "meta": "Slope 4.2% · Handrails OK", "mode": "walk", "coord": [-6.2028, 106.8248]},
                    {"title": "LRT Setiabudi Elevator Entry", "time": "14:07 WIB", "desc": "Direct access to fare gates and train platform. Level boarding.", "dist": "80m", "meta": "0 Steps Total", "mode": "lift", "coord": [-6.2088, 106.8290]}
                ],
                "segments": [
                    {"name": "Step-Free Verified Link", "mode": "walk", "time": "9 min", "speed": "3.8 km/h", "coords": [[-6.2024, 106.8233], [-6.2018, 106.8230], [-6.2028, 106.8248], [-6.2088, 106.8290]]}
                ]
            }
        }
    },

    "preset_tebet_megakuningan": {
        "id": "preset_tebet_megakuningan",
        "name": "Stasiun KRL Tebet ➔ Mega Kuningan",
        "tagline": "Case 4 · Peak Hour Multimodal Shortcut (08:30 WIB)",
        "defaultTime": "08:30",
        "gmaps": {
            "travelTime": "55 – 70 min (Gridlock)",
            "walkExposure": "350 m in Traffic Fumes",
            "fare": "Rp 45.000 (Taxi)",
            "failBadge": "Traffic Crawl",
            "failTitle": "The Casablanca Flyover Congestion Nightmare",
            "failPoints": [
                "Routes commuter via single bus or taxi directly into extreme morning peak gridlock on Jl. Casablanca and Dr. Satrio underpass.",
                "Vehicle travel speed drops to 4.2 km/h; commuter wastes 45+ minutes idling in heavy exhaust emissions.",
                "Misses synchronized JakLingko JAK.43 feeder shortcut utilizing dedicated contraflow lanes and quiet arterial connectors."
            ],
            "coords": [
                [-6.2265, 106.8582], [-6.2250, 106.8520], [-6.2240, 106.8450],
                [-6.2235, 106.8380], [-6.2250, 106.8320], [-6.2285, 106.8275]
            ]
        },
        "pijak": {
            "travelTime": "22 min Total",
            "walkExposure": "220 m (Protected)",
            "fare": "Rp 3.000",
            "winBadge": "40 Mins Saved",
            "winTitle": "KRL + JakLingko JAK.43 Feeder Bypass",
            "winPoints": [
                "High-Frequency Trunk: KRL Commuter Line to Stasiun Tebet with synchronized feeder bays.",
                "JakLingko JAK.43 Feeder: Utilizes contraflow busway lane bypassing Flyover Casablanca bottleneck (Tariff: Rp 0).",
                "Sheltered Footway: 220m walk directly to Menara BTPN / World Capital Tower lobby."
            ]
        },
        "matrix": [
            ["Peak Hour Travel Time", "55 – 70 min (Severe Gridlock)", "22 min (Feeder Shortcut)", "40 Minutes Saved (64% Faster)"],
            ["Total Commute Cost", "Rp 45.000 – Rp 65.000 (Surge Taxi)", "Rp 3.000 (KRL + Free JakLingko)", "94% Fare Reduction"],
            ["Vehicle Emission Exposure", "High (45m trapped in bumper fumes)", "Minimal (Swift dedicated bus lane)", "Healthier Commute"],
            ["Reliability / Arrival Variance", "± 25 min unpredictable delay", "± 3 min GTFS Timetable sync", "Guaranteed On-Time Arrival"],
            ["First/Last Mile Walk", "350 m unbuffered beside speeding bikes", "220 m protected office concourse", "High Pedestrian Safety"]
        ],
        "pillars": {
            "fastest": {
                "arrivalTime": "08:52 AM",
                "totalTime": "22 min",
                "timeSub": "Bypasses Congestion",
                "fare": "Rp 3.000",
                "fareSub": "Saves Rp 42.000",
                "walkDist": "220 m",
                "walkTime": "3 min walk",
                "transitTime": "19 min",
                "transitSub": "KRL + JAK.43",
                "comfortScore": "89%",
                "comfortSub": "Contraflow Bypass",
                "accessibleScore": "94%",
                "accessibleSub": "Low Floor Feeder",
                "breakdownText": "KRL Rail (7m) · JakLingko Feeder (12m) · Walk (3m)",
                "barFeederPct": 55,
                "barRailPct": 32,
                "barWalkPct": 13,
                "alert": {
                    "type": "tariff",
                    "icon": "⚡",
                    "title": "Peak Hour Multimodal Priority",
                    "desc": "Chained KRL + JakLingko JAK.43 route cuts through Casablanca gridlock using dedicated transit lanes. Rp 0 JakLingko feeder integration."
                },
                "steps": [
                    {"title": "Alight at Stasiun KRL Tebet West Gate", "time": "08:30 AM", "desc": "Exit West Concourse directly into integrated JakLingko feeder bay.", "dist": "30m", "meta": "Feeder Bay Integrated", "mode": "walk", "coord": [-6.2265, 106.8582]},
                    {"title": "Board JakLingko JAK.43 (Tebet - Kuningan)", "time": "08:33 AM", "desc": "Board air-conditioned Mikrotrans minibus with Tap-On-Bus (TOB) validator.", "dist": "3.8 km", "meta": "Fare: Rp 0 (JakLingko)", "mode": "feeder", "coord": [-6.2255, 106.8480]},
                    {"title": "Alight at Halte Mega Kuningan Barat", "time": "08:48 AM", "desc": "Drop-off right at Mega Kuningan perimeter gate.", "dist": "20m", "meta": "Contraflow Bypass", "mode": "feeder", "coord": [-6.2275, 106.8290]},
                    {"title": "Walk to Menara BTPN / World Capital Tower", "time": "08:49 AM", "desc": "Walk along broad landscaped sidewalk with ornamental trees and bollards.", "dist": "220m", "meta": "Protected Footway", "mode": "walk", "coord": [-6.2285, 106.8275]}
                ],
                "segments": [
                    {"name": "Tebet Feeder Bay Connection", "mode": "walk", "time": "2 min", "speed": "4.5 km/h", "coords": [[-6.2265, 106.8582], [-6.2260, 106.8575]]},
                    {"name": "JakLingko JAK.43 Feeder Line", "mode": "feeder", "time": "15 min", "speed": "26 km/h", "coords": [[-6.2260, 106.8575], [-6.2250, 106.8510], [-6.2238, 106.8420], [-6.2245, 106.8340], [-6.2275, 106.8290]]},
                    {"name": "Mega Kuningan Arterial Walk", "mode": "walk", "time": "3 min", "speed": "4.8 km/h", "coords": [[-6.2275, 106.8290], [-6.2280, 106.8282], [-6.2285, 106.8275]]}
                ]
            },
            "comfort": {
                "arrivalTime": "08:55 AM",
                "totalTime": "25 min",
                "timeSub": "Seated AC Shuttle",
                "fare": "Rp 3.000",
                "fareSub": "Statutory Rate",
                "walkDist": "220 m",
                "walkTime": "3 min walk",
                "transitTime": "22 min",
                "transitSub": "Air-Conditioned",
                "comfortScore": "94%",
                "comfortSub": "Guaranteed Seat",
                "accessibleScore": "94%",
                "accessibleSub": "Low Floor",
                "breakdownText": "JakLingko (18m) · Protected Walk (4m)",
                "barFeederPct": 70,
                "barRailPct": 15,
                "barWalkPct": 15,
                "alert": {
                    "type": "tariff",
                    "icon": "🛋️",
                    "title": "Air-Conditioned Mikrotrans Comfort",
                    "desc": "Modern low-emission microbus with guaranteed seating, CCTV passenger monitoring, and contactless tap."
                },
                "steps": [
                    {"title": "Board Air-Conditioned Mikrotrans JAK.43", "time": "08:30 AM", "desc": "Board premium fleet with tinted UV windows.", "dist": "3.8 km", "meta": "AC Temp 23°C", "mode": "feeder", "coord": [-6.2265, 106.8582]},
                    {"title": "Smooth Ride through Kuningan Arterial", "time": "08:35 AM", "desc": "Bypasses gridlock via designated feeder corridor.", "dist": "3.8 km", "meta": "18 min ride", "mode": "feeder", "coord": [-6.2245, 106.8340]},
                    {"title": "Walk to Menara BTPN Lobby", "time": "08:52 AM", "desc": "Tree-shaded morning footway.", "dist": "220m", "meta": "Tree Shaded", "mode": "walk", "coord": [-6.2285, 106.8275]}
                ],
                "segments": [
                    {"name": "JakLingko Feeder Transit", "mode": "feeder", "time": "18 min", "speed": "24 km/h", "coords": [[-6.2265, 106.8582], [-6.2250, 106.8510], [-6.2238, 106.8420], [-6.2245, 106.8340], [-6.2275, 106.8290]]},
                    {"name": "Shaded Footway", "mode": "walk", "time": "4 min", "speed": "4.5 km/h", "coords": [[-6.2275, 106.8290], [-6.2285, 106.8275]]}
                ]
            },
            "cheapest": {
                "arrivalTime": "08:52 AM",
                "totalTime": "22 min",
                "timeSub": "Rp 0 JakLingko Feeder",
                "fare": "Rp 3.000",
                "fareSub": "94% vs Taxi (Rp 45k)",
                "walkDist": "220 m",
                "walkTime": "3 min walk",
                "transitTime": "19 min",
                "transitSub": "Statutory Rate",
                "comfortScore": "89%",
                "comfortSub": "Integrated Tariff",
                "accessibleScore": "94%",
                "accessibleSub": "Low Floor",
                "breakdownText": "KRL (7m) · Free JakLingko (12m) · Walk (3m)",
                "barFeederPct": 55,
                "barRailPct": 32,
                "barWalkPct": 13,
                "alert": {
                    "type": "tariff",
                    "icon": "💰",
                    "title": "Subsidized Public Transit Rate",
                    "desc": "Provincial Jakarta subsidy ensures JakLingko Mikrotrans is 100% free of charge (Rp 0) when tapped with JakLingko card."
                },
                "steps": [
                    {"title": "KRL Commuter Line to Tebet", "time": "08:30 AM", "desc": "Rp 3.000 flat commuter fare.", "dist": "2.5 km", "meta": "Fare: Rp 3.000", "mode": "rail", "coord": [-6.2265, 106.8582]},
                    {"title": "JakLingko JAK.43 Feeder", "time": "08:35 AM", "desc": "Free subsidized feeder microbus.", "dist": "3.8 km", "meta": "Fare: Rp 0", "mode": "feeder", "coord": [-6.2245, 106.8340]},
                    {"title": "Walk to Mega Kuningan Office", "time": "08:49 AM", "desc": "Short walk along sidewalk.", "dist": "220m", "meta": "Fare: Rp 0", "mode": "walk", "coord": [-6.2285, 106.8275]}
                ],
                "segments": [
                    {"name": "KRL Rail Trunk", "mode": "rail", "time": "7 min", "speed": "50 km/h", "coords": [[-6.2150, 106.8550], [-6.2265, 106.8582]]},
                    {"name": "JakLingko JAK.43 (Rp 0)", "mode": "feeder", "time": "12 min", "speed": "26 km/h", "coords": [[-6.2265, 106.8582], [-6.2245, 106.8340], [-6.2275, 106.8290]]},
                    {"name": "Pedestrian Walk", "mode": "walk", "time": "3 min", "speed": "4.8 km/h", "coords": [[-6.2275, 106.8290], [-6.2285, 106.8275]]}
                ]
            },
            "wheelchair": {
                "arrivalTime": "08:56 AM",
                "totalTime": "26 min",
                "timeSub": "Low-Floor Accessible",
                "fare": "Rp 3.000",
                "fareSub": "Statutory Rate",
                "walkDist": "240 m",
                "walkTime": "5 min roll",
                "transitTime": "21 min",
                "transitSub": "Ramp Feeder",
                "comfortScore": "91%",
                "comfortSub": "Step-Free Ramp",
                "accessibleScore": "96%",
                "accessibleSub": "0 Steps",
                "breakdownText": "Accessible KRL (8m) · Low Floor Bus (13m) · Roll (5m)",
                "barFeederPct": 50,
                "barRailPct": 32,
                "barWalkPct": 18,
                "alert": {
                    "type": "wheelchair",
                    "icon": "♿",
                    "title": "Low-Floor Boarding Verified",
                    "desc": "Stasiun Tebet West Ramp connects directly to dedicated low-floor accessible feeder pick-up bay with flush boarding."
                },
                "steps": [
                    {"title": "Stasiun Tebet West Accessible Ramp", "time": "08:30 AM", "desc": "Roll down gentle ramp (slope 3.8%) into feeder terminal.", "dist": "40m", "meta": "Slope 3.8%", "mode": "lift", "coord": [-6.2265, 106.8582]},
                    {"title": "Board Low-Floor Mikrotrans", "time": "08:34 AM", "desc": "Manual fold-out ramp boarding; securement bay available.", "dist": "3.8 km", "meta": "Low-Floor Entry", "mode": "feeder", "coord": [-6.2245, 106.8340]},
                    {"title": "Mega Kuningan Paved Sidewalk Roll", "time": "08:50 AM", "desc": "Continuous flush curb-cuts on Jl. Mega Kuningan Barat.", "dist": "200m", "meta": "0 Curb Drops", "mode": "walk", "coord": [-6.2285, 106.8275]}
                ],
                "segments": [
                    {"name": "Tebet Ramp Link", "mode": "walk", "time": "3 min", "speed": "3.5 km/h", "coords": [[-6.2265, 106.8582], [-6.2260, 106.8575]]},
                    {"name": "Low Floor Feeder", "mode": "feeder", "time": "15 min", "speed": "24 km/h", "coords": [[-6.2260, 106.8575], [-6.2245, 106.8340], [-6.2275, 106.8290]]},
                    {"name": "Flush Sidewalk Roll", "mode": "walk", "time": "5 min", "speed": "3.5 km/h", "coords": [[-6.2275, 106.8290], [-6.2285, 106.8275]]}
                ]
            }
        }
    },

    "preset_bni_bundaranhi": {
        "id": "preset_bni_bundaranhi",
        "name": "Stasiun BNI City (KA Bandara) ➔ MRT Bundaran HI",
        "tagline": "Case 5 · Airport Heavy Luggage / Stroller (16:45 WIB)",
        "defaultTime": "16:45",
        "gmaps": {
            "travelTime": "24 min (Driveway Hazard)",
            "walkExposure": "450 m Heavy Dragging",
            "fare": "Rp 25.000 (Short Taxi)",
            "failBadge": "Luggage Hazard",
            "failTitle": "12% Vehicle Ramp & Traffic Crosswalk Hazard",
            "failPoints": [
                "Directs traveler with 25kg rolling suitcase or baby stroller up a steep 12% vehicular driveway ramp.",
                "Forces passenger to cross 6 lanes of speeding Sudirman traffic at surface grade with no pedestrian signal.",
                "Sidewalk surface has open drainage grates, broken pavers, and 15cm unramped curb edges that damage luggage wheels."
            ],
            "coords": [
                [-6.2018, 106.8214], [-6.2005, 106.8210], [-6.1980, 106.8220],
                [-6.1950, 106.8228], [-6.1925, 106.8231]
            ]
        },
        "pijak": {
            "travelTime": "11 min Total",
            "walkExposure": "150 m (Smooth Roll)",
            "fare": "Rp 4.000",
            "winBadge": "Luggage-Friendly",
            "winTitle": "Step-Free JPM Bridge + Level-Boarding MRT",
            "winPoints": [
                "Continuous Flat Rolling: BNI City Terminal elevator to JPM covered bridge with rubberized expansion joints.",
                "Rapid Underground Rail: 1 stop on MRT Jakarta (Dukuh Atas to Bundaran HI) with level boarding (gap < 3cm).",
                "Direct Mall Concourse: Elevator directly into Grand Indonesia / Plaza Indonesia air-conditioned shopping concourses."
            ]
        },
        "matrix": [
            ["Luggage Dragging Effort", "Severe (Steep 12% ramp & broken curb)", "Effortless (100% Flat Rolling)", "Zero Wheel Damage"],
            ["Total Travel Time", "24 min dangerous drag / traffic wait", "11 min seamless transit", "54% Faster Commute"],
            ["Total Travel Cost", "Rp 25.000 (Surge airport cab)", "Rp 4.000 (MRT Ticket)", "84% Cost Savings"],
            ["Vehicular Conflict / Danger", "High (Oncoming taxis & 6-lane cross)", "Zero (Grade-separated JPM & Metro)", "100% Protected Corridor"],
            ["Baby Stroller Feasibility", "0% (Impossible over open drain got)", "100% (Certified Smooth Wheel Roll)", "Stress-Free for Families"]
        ],
        "pillars": {
            "fastest": {
                "arrivalTime": "16:56 WIB",
                "totalTime": "11 min",
                "timeSub": "Direct MRT Link",
                "fare": "Rp 4.000",
                "fareSub": "MRT Standard",
                "walkDist": "150 m",
                "walkTime": "3 min roll",
                "transitTime": "8 min",
                "transitSub": "MRT Line 1",
                "comfortScore": "97%",
                "comfortSub": "Rubberized Joints",
                "accessibleScore": "100%",
                "accessibleSub": "0 Steps Guaranteed",
                "breakdownText": "JPM Bridge (3m) · MRT Trunk (5m) · Mall Lift (3m)",
                "barFeederPct": 0,
                "barRailPct": 65,
                "barWalkPct": 35,
                "alert": {
                    "type": "tariff",
                    "icon": "🧳",
                    "title": "Luggage & Stroller Smooth-Rolling Corridor",
                    "desc": "Seamless level transition from Airport Rail (Basoetta) to MRT Jakarta. Zero curb lifting; rubberized bridge expansion joints prevent wheel jamming."
                },
                "steps": [
                    {"title": "BNI City Airport Terminal Concourse Elevator", "time": "16:45 WIB", "desc": "Take terminal lift to Level 2 JPM pedestrian connector bridge.", "dist": "30m", "meta": "Wide Elevator Door", "mode": "lift", "coord": [-6.2018, 106.8214]},
                    {"title": "Roll via JPM Skybridge to MRT Dukuh Atas", "time": "16:47 WIB", "desc": "Smooth covered moving walkway and bridge with zero threshold steps.", "dist": "80m", "meta": "Rubber Expansion Joints", "mode": "walk", "coord": [-6.2014, 106.8227]},
                    {"title": "Board MRT Jakarta North-South Line", "time": "16:50 WIB", "desc": "Travel 1 stop underground to Stasiun MRT Bundaran HI. Platform gap < 3cm.", "dist": "1.2 km", "meta": "Fare: Rp 4.000 · 3 min", "mode": "mrt", "coord": [-6.1970, 106.8229]},
                    {"title": "Arrive MRT Bundaran HI & Grand Indonesia", "time": "16:55 WIB", "desc": "Take concourse lift directly into Plaza Indonesia / Grand Indonesia East Mall.", "dist": "40m", "meta": "Direct Mall Concourse", "mode": "lift", "coord": [-6.1925, 106.8231]}
                ],
                "segments": [
                    {"name": "BNI City Terminal JPM Link", "mode": "walk", "time": "3 min", "speed": "4.0 km/h", "coords": [[-6.2018, 106.8214], [-6.2016, 106.8220], [-6.2014, 106.8227]]},
                    {"name": "MRT Jakarta (Underground Trunk)", "mode": "mrt", "time": "5 min", "speed": "60 km/h", "coords": [[-6.2014, 106.8227], [-6.1970, 106.8229], [-6.1925, 106.8231]]},
                    {"name": "Bundaran HI Mall Concourse", "mode": "walk", "time": "3 min", "speed": "4.0 km/h", "coords": [[-6.1925, 106.8231], [-6.1920, 106.8230]]}
                ]
            },
            "comfort": {
                "arrivalTime": "16:58 WIB",
                "totalTime": "13 min",
                "timeSub": "100% Air-Conditioned",
                "fare": "Rp 4.000",
                "fareSub": "MRT Standard",
                "walkDist": "150 m",
                "walkTime": "3 min roll",
                "transitTime": "10 min",
                "transitSub": "Air-Conditioned",
                "comfortScore": "99%",
                "comfortSub": "Zero Ambient Heat",
                "accessibleScore": "100%",
                "accessibleSub": "0 Steps",
                "breakdownText": "JPM (3m) · MRT Metro (6m) · Concourse (4m)",
                "barFeederPct": 0,
                "barRailPct": 65,
                "barWalkPct": 35,
                "alert": {
                    "type": "tariff",
                    "icon": "❄️",
                    "title": "Continuous Climate Control",
                    "desc": "From the airport train cabin to the shopping mall lobby, the commuter never steps into tropical heat or automotive exhaust."
                },
                "steps": [
                    {"title": "BNI City Air-Conditioned Terminal", "time": "16:45 WIB", "desc": "Take express luggage elevator.", "dist": "30m", "meta": "Luggage Trolley Allowed", "mode": "lift", "coord": [-6.2018, 106.8214]},
                    {"title": "MRT Jakarta Subterranean Line", "time": "16:50 WIB", "desc": "Spacious carriage with dedicated luggage racks and stroller spaces.", "dist": "1.2 km", "meta": "Air-Conditioned 21°C", "mode": "mrt", "coord": [-6.1970, 106.8229]},
                    {"title": "Direct Indoor Concourse Entry", "time": "16:56 WIB", "desc": "Step-free roll into hotel / mall entrance.", "dist": "40m", "meta": "Indoor Escalator & Lift", "mode": "walk", "coord": [-6.1925, 106.8231]}
                ],
                "segments": [
                    {"name": "Airport Skybridge", "mode": "walk", "time": "3 min", "speed": "4.0 km/h", "coords": [[-6.2018, 106.8214], [-6.2014, 106.8227]]},
                    {"name": "MRT Subsurface Metro", "mode": "mrt", "time": "6 min", "speed": "60 km/h", "coords": [[-6.2014, 106.8227], [-6.1925, 106.8231]]},
                    {"name": "Plaza Indonesia Concourse", "mode": "walk", "time": "4 min", "speed": "3.8 km/h", "coords": [[-6.1925, 106.8231], [-6.1920, 106.8230]]}
                ]
            },
            "cheapest": {
                "arrivalTime": "16:56 WIB",
                "totalTime": "11 min",
                "timeSub": "Statutory MRT",
                "fare": "Rp 4.000",
                "fareSub": "84% vs Taxi (Rp 25k)",
                "walkDist": "150 m",
                "walkTime": "3 min roll",
                "transitTime": "8 min",
                "transitSub": "MRT Standard",
                "comfortScore": "97%",
                "comfortSub": "Integrated Fare",
                "accessibleScore": "100%",
                "accessibleSub": "0 Steps",
                "breakdownText": "JPM (3m) · MRT (5m) · Walk (3m)",
                "barFeederPct": 0,
                "barRailPct": 65,
                "barWalkPct": 35,
                "alert": {
                    "type": "tariff",
                    "icon": "💰",
                    "title": "Short-Hop MRT Savings",
                    "desc": "Just Rp 4.000 for a 1-stop MRT hop vs Rp 25.000 minimum taxi fare flagfall in Sudirman corridor."
                },
                "steps": [
                    {"title": "JPM Connector to MRT", "time": "16:45 WIB", "desc": "Free pedestrian bridge.", "dist": "80m", "meta": "Fare: Rp 0", "mode": "walk", "coord": [-6.2018, 106.8214]},
                    {"title": "MRT 1-Stop Hop to Bundaran HI", "time": "16:50 WIB", "desc": "Statutory base fare Rp 4.000.", "dist": "1.2 km", "meta": "Fare: Rp 4.000", "mode": "mrt", "coord": [-6.1925, 106.8231]}
                ],
                "segments": [
                    {"name": "Free JPM Connector", "mode": "walk", "time": "3 min", "speed": "4.0 km/h", "coords": [[-6.2018, 106.8214], [-6.2014, 106.8227]]},
                    {"name": "MRT Jakarta Hop", "mode": "mrt", "time": "5 min", "speed": "60 km/h", "coords": [[-6.2014, 106.8227], [-6.1925, 106.8231]]},
                    {"name": "Concourse Exit", "mode": "walk", "time": "3 min", "speed": "4.0 km/h", "coords": [[-6.1925, 106.8231], [-6.1920, 106.8230]]}
                ]
            },
            "wheelchair": {
                "arrivalTime": "16:56 WIB",
                "totalTime": "11 min",
                "timeSub": "100% Step-Free Verified",
                "fare": "Rp 4.000",
                "fareSub": "MRT Standard",
                "walkDist": "150 m",
                "walkTime": "3 min roll",
                "transitTime": "8 min",
                "transitSub": "Dual Elevators",
                "comfortScore": "99%",
                "comfortSub": "Zero Curb Drops",
                "accessibleScore": "100%",
                "accessibleSub": "0 Steps Guaranteed",
                "breakdownText": "Lift 1 (1m) · JPM (2m) · MRT Lift (2m) · Train (5m)",
                "barFeederPct": 0,
                "barRailPct": 65,
                "barWalkPct": 35,
                "alert": {
                    "type": "wheelchair",
                    "icon": "♿",
                    "title": "Heavy Luggage & Wheelchair Compliant",
                    "desc": "Elevator door clearance 1.1m; platform vertical misalignment < 1.5cm; horizontal gap < 3cm. 100% compliant with Permen PUPR 14/2017."
                },
                "steps": [
                    {"title": "BNI City Express Elevator to JPM", "time": "16:45 WIB", "desc": "Spacious lift for 2 luggage trolleys and wheelchair.", "dist": "30m", "meta": "Lift Verified", "mode": "lift", "coord": [-6.2018, 106.8214]},
                    {"title": "JPM Level Skybridge Roll", "time": "16:47 WIB", "desc": "Flat grade, rubber expansion plates, zero bumps.", "dist": "80m", "meta": "0 Bumps", "mode": "walk", "coord": [-6.2014, 106.8227]},
                    {"title": "MRT Dukuh Atas Platform Lift D1", "time": "16:49 WIB", "desc": "Take lift directly to platform level. Level boarding.", "dist": "20m", "meta": "Level Boarding", "mode": "lift", "coord": [-6.2014, 106.8227]},
                    {"title": "MRT Bundaran HI North Lift", "time": "16:54 WIB", "desc": "Direct elevator into Plaza Indonesia concourse.", "dist": "20m", "meta": "0 Steps Total", "mode": "lift", "coord": [-6.1925, 106.8231]}
                ],
                "segments": [
                    {"name": "Level Connector", "mode": "walk", "time": "3 min", "speed": "3.8 km/h", "coords": [[-6.2018, 106.8214], [-6.2014, 106.8227]]},
                    {"name": "MRT Jakarta Metro", "mode": "mrt", "time": "5 min", "speed": "60 km/h", "coords": [[-6.2014, 106.8227], [-6.1925, 106.8231]]},
                    {"name": "Mall Entrance Roll", "mode": "walk", "time": "3 min", "speed": "3.8 km/h", "coords": [[-6.1925, 106.8231], [-6.1920, 106.8230]]}
                ]
            }
        }
    },

    "preset_wisma_cheshire": {
        "id": "preset_wisma_cheshire",
        "name": "Wisma Cheshire ➔ Dukuh Atas TOD Nexus",
        "tagline": "Case 6 · Wisma Cheshire Ground-Truth Benchmark (10:00 WIB)",
        "defaultTime": "10:00",
        "gmaps": {
            "travelTime": "1h 15m (Hazardous)",
            "walkExposure": "950 m Broken Curbs",
            "fare": "Rp 35.000",
            "failBadge": "Mobility Failure",
            "failTitle": "Broken Sidewalks & Unramped Fatmawati Arterial",
            "failPoints": [
                "Routes manual wheelchair commuter through open drainage trenches (got) along Jl. RS Fatmawati.",
                "Encounter 18cm drop-offs with no curb-cuts, forcing wheelchair users onto high-speed motorcycle lanes.",
                "Fails to verify whether MRT station elevators are operational or accessible from residential street."
            ],
            "coords": [
                [-6.2917, 106.7952], [-6.2930, 106.7970], [-6.2900, 106.8020],
                [-6.2700, 106.8040], [-6.2400, 106.8050], [-6.2014, 106.8227]
            ]
        },
        "pijak": {
            "travelTime": "32 min Total",
            "walkExposure": "450 m (100% Step-Free)",
            "fare": "Rp 11.000",
            "winBadge": "Verified Co-Tested",
            "winTitle": "Continuous Tactile Path + MRT Fatmawati Elevators",
            "winPoints": [
                "Co-Tested with Permanent Manual Wheelchair Users: Route audited with residents of Wisma Cheshire Indonesia.",
                "Permen PUPR 14/2017 Compliant: Max ramp gradient 3.5%, continuous sidewalk clearance 1.6m.",
                "Level-Boarding MRT Trunk: MRT Fatmawati dual elevators to Dukuh Atas TOD Nexus (0 steps)."
            ]
        },
        "matrix": [
            ["Step-Free Accessibility", "15% (Blocked by open gutters)", "100% (Certified Continuous Ramps)", "Empowered Independent Mobility"],
            ["Max Slope Gradient", ">14% on roadside ditches", "3.5% (Well under 8.33% limit)", "Zero Biomechanical Strain"],
            ["Total Travel Time", "1h 15m dangerous detour", "32 min seamless MRT transit", "57% Faster Commute"],
            ["Elevator & Ramp Audit", "Unverified generic map data", "Ground-truth field verified with residents", "100% Proven Feasible"],
            ["Out-of-Pocket Fare", "Rp 35.000 (Forced accessible cab)", "Rp 11.000 (Standard MRT Fare)", "69% Fare Savings"]
        ],
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
                "alert": {
                    "type": "wheelchair",
                    "icon": "♿",
                    "title": "Participatory Ground-Truth Validated",
                    "desc": "Audited with permanent manual wheelchair residents of Wisma Cheshire. Eliminates unexpected 20cm drops that destroy independence."
                },
                "steps": [
                    {"title": "Roll from Wisma Cheshire Indonesia Gate", "time": "10:00 AM", "desc": "Exit residential gate on Jl. Wijaya Kusuma; continuous paved sidewalk.", "dist": "320m", "meta": "Slope 3.5%", "mode": "walk", "coord": [-6.2917, 106.7952]},
                    {"title": "Enter MRT Fatmawati Station Entrance A", "time": "10:06 AM", "desc": "Street-to-concourse Lift A1, followed by Concourse-to-platform Lift A2.", "dist": "50m", "meta": "Lifts Verified Online", "mode": "lift", "coord": [-6.2928, 106.7937]},
                    {"title": "Board MRT Jakarta North-South Line", "time": "10:09 AM", "desc": "Ride 8 stations: Cipete, Haji Nawi, Blok A, Blok M, ASEAN, Senayan, Istora, Benhil to Dukuh Atas.", "dist": "11.2 km", "meta": "21 min transit", "mode": "mrt", "coord": [-6.2445, 106.7981]},
                    {"title": "Alight MRT Dukuh Atas & Roll to JPM Concourse", "time": "10:30 AM", "desc": "Take Elevator D1 to concourse level; roll up gentle ramp to multimodal nexus.", "dist": "80m", "meta": "Slope 4.8% · 0 Steps", "mode": "walk", "coord": [-6.2014, 106.8227]}
                ],
                "segments": [
                    {"name": "Jl. Wijaya Kusuma Sidewalk", "mode": "walk", "time": "6 min", "speed": "3.5 km/h", "coords": [[-6.2917, 106.7952], [-6.2922, 106.7942], [-6.2928, 106.7937]]},
                    {"name": "MRT Jakarta Trunk Line", "mode": "mrt", "time": "21 min", "speed": "60 km/h", "coords": [[-6.2928, 106.7937], [-6.2787, 106.7972], [-6.2555, 106.7975], [-6.2445, 106.7981], [-6.2386, 106.7988], [-6.2253, 106.8027], [-6.2145, 106.8184], [-6.2014, 106.8227]]},
                    {"name": "Dukuh Atas TOD Ramp", "mode": "walk", "time": "3 min", "speed": "3.8 km/h", "coords": [[-6.2014, 106.8227], [-6.2020, 106.8235]]}
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
                "alert": {
                    "type": "wheelchair",
                    "icon": "🌳",
                    "title": "Shaded Sidewalk & Level Boarding",
                    "desc": "Tree-shaded residential footway followed by fully air-conditioned MRT transit."
                },
                "steps": [
                    {"title": "Paved Roll from Wisma Cheshire", "time": "10:00 AM", "desc": "Tree-shaded route along residential corridor to MRT Fatmawati.", "dist": "320m", "meta": "Shaded 82%", "mode": "walk", "coord": [-6.2917, 106.7952]},
                    {"title": "MRT Fatmawati Dual Elevators", "time": "10:06 AM", "desc": "Protected lift lobby into air-conditioned concourse.", "dist": "50m", "meta": "Lifts OK", "mode": "lift", "coord": [-6.2928, 106.7937]},
                    {"title": "MRT Jakarta Transit", "time": "10:09 AM", "desc": "Smooth carriage ride with wheelchair docking points.", "dist": "11.2 km", "meta": "21 min", "mode": "mrt", "coord": [-6.2445, 106.7981]},
                    {"title": "Arrive Dukuh Atas TOD Interchange", "time": "10:32 AM", "desc": "Step-free connection through Terowongan Kendal to Sudirman KRL and LRT.", "dist": "80m", "meta": "100% Covered", "mode": "walk", "coord": [-6.2014, 106.8227]}
                ],
                "segments": [
                    {"name": "Tree Shaded Roll", "mode": "walk", "time": "6 min", "speed": "3.5 km/h", "coords": [[-6.2917, 106.7952], [-6.2922, 106.7942], [-6.2928, 106.7937]]},
                    {"name": "MRT Rail Line", "mode": "mrt", "time": "21 min", "speed": "60 km/h", "coords": [[-6.2928, 106.7937], [-6.2787, 106.7972], [-6.2555, 106.7975], [-6.2445, 106.7981], [-6.2386, 106.7988], [-6.2253, 106.8027], [-6.2145, 106.8184], [-6.2014, 106.8227]]},
                    {"name": "Covered Interchange", "mode": "walk", "time": "6 min", "speed": "3.8 km/h", "coords": [[-6.2014, 106.8227], [-6.2020, 106.8235]]}
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
                "alert": {
                    "type": "tariff",
                    "icon": "💰",
                    "title": "Flat Rp 3.500 Busway Alternative",
                    "desc": "Transjakarta Corridor 1E + Corridor 1 with accessible boarding ramps and flat statutory tariff."
                },
                "steps": [
                    {"title": "Roll from Wisma Cheshire to Halte RS Fatmawati", "time": "10:00 AM", "desc": "Roll to Transjakarta low-floor bus stop on Jl. RS Fatmawati.", "dist": "380m", "meta": "Sidewalk Paved", "mode": "walk", "coord": [-6.2917, 106.7952]},
                    {"title": "Board Transjakarta 1E (Pondok Labu - Blok M)", "time": "10:08 AM", "desc": "Low-floor bus with fold-out wheelchair boarding ramp. Flat fare.", "dist": "6.8 km", "meta": "Fare: Rp 3.500", "mode": "feeder", "coord": [-6.2787, 106.7972]},
                    {"title": "Transfer to Corridor 1 at Blok M Hub to Dukuh Atas", "time": "10:28 AM", "desc": "Free within-station transfer to Corridor 1 directly to Halte Dukuh Atas 1.", "dist": "5.2 km", "meta": "Free Transfer (Rp 0)", "mode": "rail", "coord": [-6.2253, 106.8027]},
                    {"title": "Exit Halte Dukuh Atas via Ramp", "time": "10:45 AM", "desc": "Gentle ramped skybridge to Dukuh Atas pedestrian concourse.", "dist": "140m", "meta": "Slope 5.8%", "mode": "walk", "coord": [-6.2014, 106.8227]}
                ],
                "segments": [
                    {"name": "Sidewalk Roll", "mode": "walk", "time": "7 min", "speed": "3.5 km/h", "coords": [[-6.2917, 106.7952], [-6.2922, 106.7942], [-6.2928, 106.7937]]},
                    {"name": "Transjakarta Busway", "mode": "rail", "time": "37 min", "speed": "22 km/h", "coords": [[-6.2928, 106.7937], [-6.2445, 106.7981], [-6.2014, 106.8227]]},
                    {"name": "TOD Skybridge Roll", "mode": "walk", "time": "4 min", "speed": "3.8 km/h", "coords": [[-6.2014, 106.8227], [-6.2020, 106.8235]]}
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
                "alert": {
                    "type": "wheelchair",
                    "icon": "♿",
                    "title": "Wisma Cheshire Gold Standard Path",
                    "desc": "100% verified step-free roll from Wisma Cheshire entrance to MRT Fatmawati lifts and Dukuh Atas concourse."
                },
                "steps": [
                    {"title": "Wisma Cheshire Ramp Departure", "time": "10:00 AM", "desc": "Step-free ramp descent (slope 3.5%) onto Jl. Wijaya Kusuma. No open gutters.", "dist": "320m", "meta": "Permen PUPR Compliant", "mode": "walk", "coord": [-6.2917, 106.7952]},
                    {"title": "MRT Fatmawati Station Lift A1 & A2", "time": "10:06 AM", "desc": "Elevator door width 1.1m (exceeds 0.9m standard). Audible and braille floor buttons.", "dist": "50m", "meta": "100% Functional", "mode": "lift", "coord": [-6.2928, 106.7937]},
                    {"title": "Dedicated Accessible MRT Train Car", "time": "10:09 AM", "desc": "Automatic level platform boarding; platform horizontal gap < 3cm, vertical gap < 1.5cm.", "dist": "11.2 km", "meta": "Wheelchair Anchor Bay", "mode": "mrt", "coord": [-6.2445, 106.7981]},
                    {"title": "Dukuh Atas BNI Lift D1 to JPM Concourse", "time": "10:30 AM", "desc": "Direct underground lift into JPM Dukuh Atas multimodal hub. 0 steps encountered throughout journey.", "dist": "80m", "meta": "0 Steps Total", "mode": "lift", "coord": [-6.2014, 106.8227]}
                ],
                "segments": [
                    {"name": "Accessible Sidewalk", "mode": "walk", "time": "6 min", "speed": "3.5 km/h", "coords": [[-6.2917, 106.7952], [-6.2922, 106.7942], [-6.2928, 106.7937]]},
                    {"name": "Level-Boarding MRT", "mode": "mrt", "time": "21 min", "speed": "60 km/h", "coords": [[-6.2928, 106.7937], [-6.2787, 106.7972], [-6.2555, 106.7975], [-6.2445, 106.7981], [-6.2386, 106.7988], [-6.2253, 106.8027], [-6.2145, 106.8184], [-6.2014, 106.8227]]},
                    {"name": "TOD Multi-Level Ramp", "mode": "walk", "time": "3 min", "speed": "3.8 km/h", "coords": [[-6.2014, 106.8227], [-6.2020, 106.8235]]}
                ]
            }
        }
    }
}
