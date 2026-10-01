import os, sys, json, csv

base = '/Users/gading/Documents/Urban_Research'
output_path = f'{base}/empirical_field_data_dashboard.html'

print("Generating Empirical Field Research Dashboard HTML...")

# 1. Weather Data (stdlib csv)
weather_list = []
with open(f'{base}/investigate/field/data/weather_2026-06-18.csv', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        w = {}
        for k, v in row.items():
            if v == '' or v is None:
                w[k] = None
            else:
                try:
                    w[k] = float(v) if '.' in v else int(v)
                except ValueError:
                    w[k] = v
        weather_list.append(w)

# 2. Respondents Data & Demographics (stdlib csv)
with open(f'{base}/investigate/field/data/respondents_2026-06-18.csv', encoding='utf-8') as f:
    resp_rows = list(csv.DictReader(f))

resp_coords = {
    'R01': (-6.2014, 106.8227),
    'R02': (-6.2032, 106.8225),
    'R03': (-6.2018, 106.8228),
    'R04': (-6.1985, 106.8235),
    'R05': (-6.2088, 106.8219),
    'R06': (-6.2095, 106.8212),
    'R07': (-6.2038, 106.8221),
    'R08': (-6.2024, 106.8233),
    'R09': (-6.2076, 106.8223),
    'R10': (-6.2162, 106.8168),
    'R11': (-6.2052, 106.8224),
    'R12': (-6.2222, 106.8092),
    'N01': (-6.2043, 106.8221),
    'N02': (-6.2019, 106.8229),
    'N03': (-6.2021, 106.8226),
    'N04': (-6.2020, 106.8225),
    'N05': (-6.2075, 106.8222),
    'N06': (-6.2036, 106.8224),
    'N07': (-6.2026, 106.8225),
    'N08': (-6.2045, 106.8223),
    'N09': (-6.1995, 106.8185),
    'N10': (-6.1945, 106.8228),
    'N11': (-6.2026, 106.8248),
    'N12': (-6.2025, 106.8247)
}

resp_demographics = {
    'R01': {'gender': 'Male', 'age_bracket': 'Adult (30-49)', 'age_group': 'Adult'},
    'R02': {'gender': 'Male', 'age_bracket': 'Adult (30-49)', 'age_group': 'Adult'},
    'R03': {'gender': 'Male', 'age_bracket': 'Adult (30-49)', 'age_group': 'Adult'},
    'R04': {'gender': 'Male', 'age_bracket': 'Elderly (60+)', 'age_group': 'Elderly'},
    'R05': {'gender': 'Female', 'age_bracket': 'Young Adult (19-29)', 'age_group': 'Young Adult'},
    'R06': {'gender': 'Female', 'age_bracket': 'Teenager (15-18)', 'age_group': 'Teenager'},
    'R07': {'gender': 'Male', 'age_bracket': 'Young Adult (19-29)', 'age_group': 'Young Adult'},
    'R08': {'gender': 'Male', 'age_bracket': 'Adult (30-49)', 'age_group': 'Adult'},
    'R09': {'gender': 'Male', 'age_bracket': 'Adult (30-49)', 'age_group': 'Adult'},
    'R10': {'gender': 'Male', 'age_bracket': 'Adult (30-49)', 'age_group': 'Adult'},
    'R11': {'gender': 'Male', 'age_bracket': 'Middle-Aged (50-59)', 'age_group': 'Middle-Aged'},
    'R12': {'gender': 'Male', 'age_bracket': 'Adult (30-49)', 'age_group': 'Adult'},
    'N01': {'gender': 'Male', 'age_bracket': 'Adult (30-49)', 'age_group': 'Adult'},
    'N02': {'gender': 'Female', 'age_bracket': 'Young Adult (19-29)', 'age_group': 'Young Adult'},
    'N03': {'gender': 'Male', 'age_bracket': 'Adult (30-49)', 'age_group': 'Adult'},
    'N04': {'gender': 'Female', 'age_bracket': 'Young Adult (19-29)', 'age_group': 'Young Adult'},
    'N05': {'gender': 'Male', 'age_bracket': 'Adult (30-49)', 'age_group': 'Adult'},
    'N06': {'gender': 'Male', 'age_bracket': 'Adult (30-49)', 'age_group': 'Adult'},
    'N07': {'gender': 'Male', 'age_bracket': 'Adult (30-49)', 'age_group': 'Adult'},
    'N08': {'gender': 'Female', 'age_bracket': 'Teenager (15-18)', 'age_group': 'Teenager'},
    'N09': {'gender': 'Male', 'age_bracket': 'Elderly (60+)', 'age_group': 'Elderly'},
    'N10': {'gender': 'Male', 'age_bracket': 'Adult (30-49)', 'age_group': 'Adult'},
    'N11': {'gender': 'Male', 'age_bracket': 'Young Adult (19-29)', 'age_group': 'Young Adult'},
    'N12': {'gender': 'Female', 'age_bracket': 'Middle-Aged (50-59)', 'age_group': 'Middle-Aged'}
}

resp_quotes = {
    'R01': {
        'quote': "Kalau itu kan lebih ke luar ya, Bu ya... Sebenarnya kan kalau petugas KAI ya pasti ngamanin asetnya KAI... Baik pun MRT, baik pun kami sebagai keamanan di sini... Ya udah kita di sini aja... Nggak ada kerja sama dari semuanya, cuma polisi.",
        'insight': "Institutional fragmentation: KAI, MRT, Kawis, and MITJ manage separate boundaries; interstitial public spaces are left in a jurisdictional vacuum. Permits require a multi-agency chain (Sekda -> MRT -> Kawis -> MITJ).",
        'tags': ["Jurisdiction Vacuum", "Transit Boundary", "Security Coordination"],
        'full_title': "Petugas Keamanan Kawasan (Area MRT/KAI)"
    },
    'R02': {
        'quote': "Nyaman... karena jalannya enak. Adem ada pohon-pohonnya. Panas, tapi nyaman-nyaman aja.",
        'insight': "Daily pedestrian baseline: Sidewalk expansion and tree buffer make walking pleasant despite direct tropical sun. Heat is tolerated as an inevitable background condition.",
        'tags': ["Daily Commuter", "Tree Buffer", "Heat Tolerance"],
        'full_title': "Pria Pejalan Kaki Harian"
    },
    'R03': {
        'quote': "Kalau aman sih aman... Karena panas ya. Mungkin kalau misalnya pohonnya lebih banyak mungkin lebih nyaman... pasang kanopi ya... Saya relatif ya pas lagi sepi soalnya (merasa aman).",
        'insight': "Counter-commute psychology: Pedestrian feels safer when quiet, contrary to urban 'eyes on the street' theory. Proposes continuous canopies for direct sun.",
        'tags': ["Counter-Commute", "Canopy Request", "Quiet vs Crowded"],
        'full_title': "Pria Pejalan Kaki Mingguan"
    },
    'R04': {
        'quote': "Nyaman, aman... Saya jalan kaki tiap hari 1,5 jam buat olahraga dari Thamrin City ke Semanggi terus putar ke HI... cuma ada titik tertentu dekat Kedubes Jepang / Sarinah yang masih panas.",
        'insight': "Elderly mobility validation: High-quality pedestrian infrastructure enables ~1.5h daily active wellness walks for senior citizens. Reassured by visible police presence.",
        'tags': ["Active Aging", "1.5h Daily Exercise", "Police Reassurance"],
        'full_title': "Bapak Jalan (Lansia 60+)"
    },
    'R05': {
        'quote': "Trotoar ke zebra cross itu terlalu tinggi dan curam banget, licin juga... ini teman saya jatuh dua kali, barusan jatuh lagi pas kita ngobrol... Motor juga suka nyelonong di zebra cross.",
        'insight': "Crucial accessibility defect: Curb ramps to zebra crossings have excessive slope and slippery finish, causing physical falls during crossing while motorbikes fail to yield.",
        'tags': ["Curb Ramp Defect", "Falling Hazard", "Motorbike Failure to Yield"],
        'full_title': "Mba Tangerang Selatan (Commuter TJ)"
    },
    'R06': {
        'quote': "Aman-aman aja sih kak, kita barengan berdua jadi gak takut... gak pernah ada catcalling atau orang aneh-aneh. Jalannya juga luas dan rapi.",
        'insight': "Youth group safety: Walking in pairs/groups provides subjective security against harassment along the broad boulevard for high school students.",
        'tags': ["SMAN 3 Students", "Group Safety", "No Catcalling"],
        'full_title': "Siswi SMAN 3 Teladan (Dua Orang)"
    },
    'R07': {
        'quote': "Siang gini panasnya minta ampun, Mas... males banget jalan jauh, mending naik motor. Tapi kalau malam enak, adem, lampu-lampu gedung bagus... jalan malam mah enjoy.",
        'insight': "Modal shift boundary: Rider enjoys walking at night when temperature cools, but abandons walking for motorbikes during midday due to extreme solar radiation.",
        'tags': ["Motorbike Transition", "Midday Solar Deterrent", "Night Walking Preference"],
        'full_title': "Pengendara Motor dari Tebet"
    },
    'R08': {
        'quote': "Kalau dulu mah sini rawan begal, Mas... dulu kan sebenarnya buat mobil putar balik, makanya ditutup sama Pak Anies karena ada MRT, terus dijadiin TOD... Tadi lihat Mas-mas baju oren yang ngukur nyoret-nyoret? Mau dibuat donat tuh... patung Sudirman mau digeser dibikin muter kayak Semanggi.",
        'insight': "Institutional TOD insider: Historical transformation from vehicular U-turn / begal hotspot to vibrant transit hub. Previews upcoming circular pedestrian deck ('donat') at Sudirman statue.",
        'tags': ["TOD Planning", "Crime Reduction", "Pedestrianization History", "MITJ"],
        'full_title': "Pegawai MITJ (Stasiun Sudirman)"
    },
    'R09': {
        'quote': "Poin-poin rawan itu pas parkiran motor sama di atas JPO... copet, curanmor, jambret... terutama malam hari jam 10 ke atas... Bukan karena gelap, di atas tuh TERANG cuma SEPI. Nunggu momen yang tepat... 6 bulan ini udah berkurang.",
        'insight': "Pivotal environmental criminology insight: Lighting alone does not prevent street crime. Isolation in a well-lit but deserted space (upper JPO deck) after 22:00 is the actual vulnerability factor.",
        'tags': ["Night Crime Hotspot", "Upper JPO", "Lit But Deserted", "Eyes On Street"],
        'full_title': "Informan Keamanan Titik Rawan (Malam)"
    },
    'R10': {
        'quote': "Nyaman sih, lumayan... pohon yang asri, bebas dari polusi karena jaraknya lumayan jauh dari jalan gede... tapi pas nyebrang ke zebra cross agak curam sedikit, takut dari sana ada yang ngebut... bahaya kalau bawa anak.",
        'insight': "Parental safety perspective: Buffering distance from vehicular lanes mitigates exhaust pollution and stress, but steep curb ramps exacerbate crossing risk when guiding young children.",
        'tags': ["Family Pedestrian", "Pollution Buffer", "Curb Drop With Children"],
        'full_title': "Bapak Bawa Anak"
    },
    'R11': {
        'quote': "Trotoarnya udah bagus, udah manusiawi, udah gede... tapi masalahnya kita negara tropis! Studi bandingnya ke negara 4 musim... siang-siang panasnya minta ampun, pohon belum efektif menahan panas... malam hari rimbunnya pohon malah nutupin lampu jalan, jadi gelap dan banyak nyamuk!",
        'insight': "Fundamental critique of post-revitalization design: Copying temperate 4-season models (paved boulevards with saplings) fails tropical climate realities. Trees create nighttime shadow cones over street lamps.",
        'tags': ["Urban Theory", "4-Season Copying", "Thermal Mismatch", "Night Shadowing"],
        'full_title': "Bapak Kritikus Tata Kota"
    },
    'R12': {
        'quote': "Banyak ojol melanggar naik ke trotoar... Satpol PP cuma nanganin PKL, urusan motor itu wewenang Dishub... kalau siang gak ada shelter teduh buat istirahat pejalan kaki.",
        'insight': "Regulatory jurisdictional loophole: Sidewalk vehicular intrusion by motorcycle taxis (ojol) falls between Satpol PP (public order/vendors) and Dishub (transportation/vehicles).",
        'tags': ["Enforcement Gap", "Dishub vs Satpol PP", "Ojol Intrusion", "Lack of Shelter"],
        'full_title': "Satpam / Satpol PP (Mobile Patrol)"
    },
    'N01': {
        'quote': "Nyaman jalan di Sudirman, ada yang panas ada yang teduh. Skala kenyamanan 7/10.",
        'insight': "Baseline stated satisfaction 7/10 from transport worker resting at Karet corner.",
        'tags': ["Taxi Driver", "Shade Intermittency"],
        'full_title': "Bapak Taxi (Belokan Karet)"
    },
    'N02': {
        'quote': "Aman & nyaman jalan di Sudirman; tidak pernah mengalami kriminalitas. Sering jalan pulang jam 1 pagi, aman aja dan penerangan cukup. Tapi pas rush hour pagi & sore banyak rintangan di jalan.",
        'insight': "Exceptional 10/10 safety score for late-night walking (01:00 AM) contrasting with rush-hour pedestrian bottlenecks.",
        'tags': ["Late-Night Walker (01:00)", "High Perceived Safety", "Rush-Hour Bottleneck"],
        'full_title': "Mba 1 (Office Worker - Stasiun Taman Duduk)"
    },
    'N03': {
        'quote': "Nyaman jalan di Sudirman, ada yang panas ada yang teduh. Skala kenyamanan 7/10.",
        'insight': "Middle-aged pedestrian walking across Sudirman overpass; confirms 7/10 comfort baseline.",
        'tags': ["Stated 7/10", "Overpass Walker"],
        'full_title': "Bapak Jalan (Atas Stasiun)"
    },
    'N04': {
        'quote': "Nyaman jalan di Sudirman, ada yang panas ada yang teduh. Skala kenyamanan 7/10.",
        'insight': "Suburban commuter from South Tangerang; corroborates 7/10 rating along station approach.",
        'tags': ["Stated 7/10", "Suburban Commuter"],
        'full_title': "Mba Tangerang Selatan (Atas Stasiun)"
    },
    'N05': {
        'quote': "Ada GAP tanggung jawab masing-masing wilayah — cuma peduli di wilayahnya sendiri, kalau bukan wilayahnya gak peduli. Skala kenyamanan 7/10.",
        'insight': "Frontline security corroborates territorial silo effect across building complexes and public right-of-way.",
        'tags': ["Territorial Silos", "Jurisdiction Gap"],
        'full_title': "Satpam Dekat JPO (2 Orang)"
    },
    'N06': {
        'quote': "Nyaman jalan di Sudirman, ada yang panas ada yang teduh. Skala kenyamanan 7/10.",
        'insight': "Informal street vendor noting alternating thermal micro-climates along the sidewalk tree canopy.",
        'tags': ["Street Vendor (PKL)", "Thermal Micro-climates"],
        'full_title': "PKL (Jalan Raya Sudirman)"
    },
    'N07': {
        'quote': "Kenyamanan jalan cukup baik 7/10.",
        'insight': "Father walking with child on main sidewalk enjoying broad pedestrian space.",
        'tags': ["Father & Child", "Pedestrian Space"],
        'full_title': "Bapak Bawa Anak (Sudirman)"
    },
    'N08': {
        'quote': "Kenyamanan jalan 7/10.",
        'insight': "SMAN 3 student returning from school; notes satisfactory walking quality.",
        'tags': ["High School Commuter", "SMAN 3"],
        'full_title': "Siswi SMAN 3 (Anak Sekolah)"
    },
    'N09': {
        'quote': "Di Kebon Melati ada rumah-rumah pejabat pemerintah; gak pernah banjir karena ada waduk. MRT itu dulunya lapangan tenis.",
        'insight': "Pivotal gradient contact: Only respondent interviewed in the back-street residential zone behind the Sudirman skyscraper wall. Demonstrates informal spatial memory and localized drainage dynamics.",
        'tags': ["Urban Gradient Anchor", "Back-Street Resident", "Kebon Melati", "Spatial Memory"],
        'full_title': "Bapak Lansia Warlok (Kebon Melati)"
    },
    'N10': {
        'quote': "Penumpang sering cancel kalau macet di sekitar stasiun saat jemput; kemacetan parah mulai jam 15:00.",
        'insight': "Transit pickup friction: First/last-mile ride-hailing cancellations caused by station bottleneck congestion.",
        'tags': ["Ride-Hailing Pickup", "Station Congestion", "First-Mile Friction"],
        'full_title': "Driver GrabCar 1 (Sudirman -> GI)"
    },
    'N11': {
        'quote': "Masih ada kriminalitas: di atas jalan raya rawan jambret, curanmor & copet di bawah. Bule pernah dijambret jam 3 subuh. Fasilitas infrastruktur masih banyak yang rusak dan gak rata, SUDAH DILAPORKAN TAPI GAK PERNAH DIGUBRIS PEMERINTAH. Banyak ojol melanggar masuk terowongan pejalan kaki. Parkir karyawan & tenant menutupi jalur aksesibilitas. Ada scam penggalangan dana UNHCR palsu.",
        'insight': "The richest frontline grievance log: uncovers pedestrian tunnel motorcycle violations, ignored maintenance reports, accessibility obstructions by building tenants, and predatory charity scams.",
        'tags': ["Tunnel Violations", "Unresponsive Govt", "Damaged Paving", "Accessibility Obstruction", "Scam"],
        'full_title': "Mas Penjaga MITJ - Mas Arief (Terowongan Kendal)"
    },
    'N12': {
        'quote': "Sering kesandung karena infrastruktur banyak yang rusak dan gak rata; sudah dilaporkan tapi gak pernah digubris. Merasa pemerintah gak peduli & gak menanggapi keluhan rakyat, tidak memperdulikan masalah-masalah kecil. Ibu Lis melakukan charity pribadi & tertutup untuk anak operasi jantung.",
        'insight': "Voice of the citizen: Tripping hazards from broken paver tiles lead to deep disillusionment with municipal accountability ('pemerintah gak peduli masalah kecil'). Independent grassroots philanthropy.",
        'tags': ["Citizen Grievance", "Broken Pavement", "Tripping Hazard", "Govt Disillusionment"],
        'full_title': "Ibu Lis (Terowongan Kendal)"
    }
}

respondents_data = []
for idx, r in enumerate(resp_rows):
    rid = str(r['respondent_id'])
    coord = resp_coords.get(rid, (-6.2030, 106.8225))
    meta = resp_quotes.get(rid, {
        'quote': str(r.get('notes', '') or ''),
        'insight': str(r.get('key_painpoint', '') or ''),
        'tags': [],
        'full_title': str(r.get('role_or_type', '') or '')
    })
    demo = resp_demographics.get(rid, {'gender': 'Unknown', 'age_bracket': 'Adult (30-49)', 'age_group': 'Adult'})
    
    sec = float(r['security_1_10']) if r.get('security_1_10') else None
    comf = float(r['comfort_1_10']) if r.get('comfort_1_10') else None
    heat = float(r['heat_1_10']) if r.get('heat_1_10') else None
    
    respondents_data.append({
        'id': rid,
        'source': str(r.get('source', '') or ''),
        'team': str(r.get('team', '') or ''),
        'timestamp': str(r.get('timestamp', '') or ''),
        'location': str(r.get('location', '') or ''),
        'lat': coord[0],
        'lon': coord[1],
        'class': str(r.get('class', '') or 'unclassified'),
        'role_or_type': str(r.get('role_or_type', '') or ''),
        'gender': demo['gender'],
        'age_bracket': demo['age_bracket'],
        'age_group': demo['age_group'],
        'mobility_mode': str(r.get('mobility_mode', '') or 'walk'),
        'security_1_10': sec,
        'comfort_1_10': comf,
        'heat_1_10': heat,
        'scale_source': str(r.get('scale_source', '') or 'none'),
        'key_painpoint': str(r.get('key_painpoint', '') or ''),
        'notes': str(r.get('notes', '') or ''),
        'quote': meta['quote'],
        'insight': meta['insight'],
        'tags': meta['tags'],
        'full_title': meta['full_title']
    })

# 3. Media Points & Spatial Hotspot Classification (stdlib csv)
with open(f'{base}/investigate/field/photos/media-log_2026-06-18.csv', encoding='utf-8') as f:
    med_rows = list(csv.DictReader(f))
thumb_dir = f'{base}/Documentations/thumbnails'
existing_thumbs = set(os.listdir(thumb_dir)) if os.path.exists(thumb_dir) else set()

def classify_media_asset(lat, lon, fn, mtype):
    # 1. Back-street alleys: Kebon Kacang / Thamrin City back-streets
    if lon < 106.818 and lat > -6.200:
        return (
            'Kebon Kacang & Back-Streets',
            'Back-Street Gradient (Zero Sidewalk)',
            'warning',
            'Residential alleyway one block behind Sudirman commercial towers. Demonstrates stark 0% sidewalk drop-off, uneven road surface, and mixed vehicle-pedestrian conflict.'
        )

    # 2. North transect approach: Bundaran HI / Thamrin
    if lat > -6.198:
        return (
            'Bundaran HI / North Approach',
            'Arterial Boulevard Integration',
            'info',
            'Northern gateway connecting Bundaran HI MRT to Dukuh Atas transit hub, featuring wide standardized pavers and rapid pedestrian throughput.'
        )

    # 3. Kendal Tunnel & Stasiun BNI City / Sudirman link (lat -6.2030 to -6.2012, lon >= 106.8229)
    if -6.2030 <= lat <= -6.2012 and lon >= 106.8229:
        return (
            'Terowongan Kendal & Transit Link',
            'Tunnel Conflict & Motorcycle Intrusion',
            'danger',
            'High-friction pedestrian tunnel where informal vendors, broken paver tiles, and prohibited motorcycle shortcuts create recurring collision hazards (documented by Mas Arief & Ibu Lis).'
        )

    # 4. Dukuh Atas Transit Plaza & Forecourts (lat -6.2025 to -6.2010, lon 106.8220 to 106.8229)
    if -6.2025 <= lat <= -6.2010 and 106.8220 <= lon < 106.8229:
        return (
            'Dukuh Atas Transit Hub',
            'Transit Plaza & Multimodal Transfer',
            'info',
            'Primary multimodal nexus integrating KRL Commuterline, MRT Jakarta, LRT Jabodebek, and Airport Rail Link with wide pedestrian plazas.'
        )

    # 5. Taman Dukuh Atas & Seating Transition (lat -6.2045 to -6.2025)
    if -6.2045 <= lat < -6.2025:
        return (
            'Taman Dukuh Atas & Buffer',
            'Solar Exposure & Shade Canopies',
            'warning',
            'Linear park with public seating; highlights daytime solar radiation gaps where immature tree canopies fail to mitigate 35°C peak heat index.'
        )

    # 6. Sudirman - Karet & JPO Phinisi (lat -6.2088 to -6.2045)
    if -6.2088 <= lat < -6.2045:
        if lon > 106.8220 and lat < -6.2070:
            return (
                'Sudirman - Karet (JPO Phinisi)',
                'Upper JPO Structure & Night Hotspot',
                'danger',
                'Multi-tier landmark pedestrian bridge (JPO Phinisi). Identified by security informants as an isolated hotspot late at night (well-lit but deserted).'
            )
        else:
            return (
                'Sudirman - Karet Corridor',
                'Curb Ramp Drop & Crosswalk Risk',
                'danger',
                'Curb-to-zebra cross transition where multiple respondents flagged dangerous kerb drops and slippery slopes during crossings.'
            )

    # 7. Semanggi Interchange & Bendungan Hilir (lat -6.2190 to -6.2140)
    if -6.2190 <= lat < -6.2140:
        return (
            'Semanggi Interchange & Benhil',
            'Highway Buffer & Heat Island',
            'warning',
            'Expansive cloverleaf intersection where pedestrians traverse extensive unshaded distances exposed to heavy vehicular exhaust and extreme radiant heat.'
        )

    # 8. Polda Metro Jaya & FX Sudirman (lat <= -6.2190)
    if lat < -6.2190:
        return (
            'Polda Metro Jaya & FX Sudirman',
            'Southern Terminus & Street Furniture',
            'info',
            'Southern revitalized pedestrian boulevard featuring high-capacity sidewalks, mature landscaping buffer, and bus stops near GBK/FX.'
        )

    return (
        'Sudirman Central Corridor',
        'Pedestrian Right-of-Way',
        'info',
        'Standard 8–10m revitalized pedestrian corridor with tactile pavers and greenery buffer.'
    )

media_data = []
for idx, r in enumerate(med_rows):
    fn = str(r['filename'])
    base_name, ext = os.path.splitext(fn)
    thumb_name = f'{base_name}.jpg'
    has_thumb = thumb_name in existing_thumbs
    
    lat = float(r['lat'])
    lon = float(r['long'])
    mtype = str(r['type'])
    dur = float(r['duration_s']) if r.get('duration_s') else None
    
    zone, hazard_label, hazard_severity, desc = classify_media_asset(lat, lon, fn, mtype)
    thumb_rel_path = f'./Documentations/thumbnails/{thumb_name}' if has_thumb else None
    raw_rel_path = f'./Documentations/{fn}'
    
    media_data.append({
        'index': idx + 1,
        'filename': fn,
        'type': mtype,
        'datetime_wib': str(r['datetime_wib']),
        'lat': lat,
        'lon': lon,
        'duration_s': dur,
        'has_thumb': has_thumb,
        'thumb_url': thumb_rel_path,
        'raw_url': raw_rel_path,
        'zone': zone,
        'category': hazard_label,
        'severity': hazard_severity,
        'description': desc,
        'in_doc_folder': has_thumb
    })

# 4. Pedestrian Network GeoJSON
with open(f'{base}/investigate/spatial/data/pedestrian_network.geojson') as f:
    pnet_geojson = json.load(f)

# 5. Gradient CSV (stdlib csv)
gradient_data = []
with open(f'{base}/investigate/spatial/data/gradient.csv', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        g = {}
        for k, v in row.items():
            if v == '' or v is None:
                g[k] = 0
            else:
                try:
                    g[k] = float(v) if '.' in v else int(v)
                except ValueError:
                    g[k] = v
        gradient_data.append(g)

# 6. Places POI (stdlib csv)
places_data = []
with open(f'{base}/investigate/spatial/data/dukuh_atas_places.csv', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        p = {}
        for k, v in row.items():
            try:
                p[k] = float(v) if '.' in v else (int(v) if v.isdigit() else v)
            except ValueError:
                p[k] = v
        places_data.append(p)

print(f"Serialized all datasets: {len(respondents_data)} respondents, {len(media_data)} media, {len(weather_list)} weather, {len(pnet_geojson.get('features',[]))} network edges, {len(gradient_data)} gradient rows, {len(places_data)} POIs.")

# Build HTML
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pijak Empirical Field Research Dashboard | Sudirman Corridor Field Day 1</title>
  
  <!-- Modern UI Libraries via CDN -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.2/dist/chart.umd.min.js"></script>
  <script src="https://unpkg.com/lucide@latest"></script>
  
  <style>
    :root {
      --bg-primary: #090d16;
      --bg-surface: #111827;
      --bg-card: #1e293b;
      --bg-card-hover: #283548;
      --border-color: #334155;
      --border-subtle: #1e293b;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --accent-cyan: #06b6d4;
      --accent-blue: #3b82f6;
      --accent-emerald: #10b981;
      --accent-amber: #f59e0b;
      --accent-rose: #f43f5e;
      --accent-purple: #a855f7;
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--bg-primary);
      color: var(--text-main);
      font-family: var(--font-sans);
      line-height: 1.5;
      overflow-x: hidden;
      font-size: 14px;
    }

    /* Scrollbars */
    ::-webkit-scrollbar {
      width: 8px;
      height: 8px;
    }
    ::-webkit-scrollbar-track {
      background: var(--bg-primary);
    }
    ::-webkit-scrollbar-thumb {
      background: var(--border-color);
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: var(--accent-cyan);
    }

    /* Header & Navigation */
    header {
      background: rgba(17, 24, 39, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-color);
      position: sticky;
      top: 0;
      z-index: 1000;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }

    .brand-group {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .brand-logo {
      width: 42px;
      height: 42px;
      border-radius: 10px;
      background: linear-gradient(135deg, #06b6d4, #3b82f6);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 20px;
      color: white;
      box-shadow: 0 4px 14px rgba(6, 182, 212, 0.35);
    }

    .brand-text h1 {
      font-size: 17px;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #fff;
    }

    .brand-text p {
      font-size: 12px;
      color: var(--text-muted);
    }

    .nav-tabs {
      display: flex;
      gap: 6px;
      background: var(--bg-primary);
      padding: 4px;
      border-radius: 10px;
      border: 1px solid var(--border-color);
      flex-wrap: wrap;
    }

    .nav-tab {
      padding: 8px 14px;
      border-radius: 8px;
      border: none;
      background: transparent;
      color: var(--text-muted);
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }

    .nav-tab:hover {
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.05);
    }

    .nav-tab.active {
      color: #fff;
      background: var(--accent-cyan);
      box-shadow: 0 2px 8px rgba(6, 182, 212, 0.4);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .tag-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.3);
      color: var(--accent-emerald);
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
    }

    /* Stat Banner Cards */
    .stats-bar {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      padding: 20px 24px 8px 24px;
    }

    .stat-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 16px 20px;
      position: relative;
      overflow: hidden;
      transition: transform 0.2s ease, border-color 0.2s ease;
    }

    .stat-card:hover {
      transform: translateY(-2px);
      border-color: var(--accent-cyan);
    }

    .stat-card::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: var(--accent-cyan);
    }

    .stat-card.card-blue::before { background: var(--accent-blue); }
    .stat-card.card-amber::before { background: var(--accent-amber); }
    .stat-card.card-rose::before { background: var(--accent-rose); }
    .stat-card.card-emerald::before { background: var(--accent-emerald); }
    .stat-card.card-purple::before { background: var(--accent-purple); }

    .stat-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
    }

    .stat-label {
      font-size: 11px;
      text-transform: uppercase;
      font-weight: 700;
      letter-spacing: 0.05em;
      color: var(--text-muted);
    }

    .stat-val-group {
      display: flex;
      align-items: baseline;
      gap: 8px;
    }

    .stat-val {
      font-size: 28px;
      font-weight: 800;
      color: #fff;
      line-height: 1;
    }

    .stat-subtext {
      font-size: 12px;
      color: var(--text-dim);
      margin-top: 6px;
    }

    /* Main Container */
    main {
      padding: 16px 24px 32px 24px;
    }

    .tab-panel {
      display: none;
    }

    .tab-panel.active {
      display: block;
      animation: fadeIn 0.25s ease-in-out;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(4px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Leaflet Studio Grid */
    .geo-layout {
      display: grid;
      grid-template-columns: 1fr 380px;
      gap: 16px;
      height: calc(100vh - 220px);
      min-height: 600px;
    }

    @media (max-width: 1200px) {
      .geo-layout {
        grid-template-columns: 1fr;
        height: auto;
      }
    }

    .map-pane {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      position: relative;
    }

    .map-toolbar {
      padding: 10px 16px;
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-color);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
      z-index: 500;
    }

    .filter-group {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .filter-btn {
      padding: 6px 12px;
      border-radius: 6px;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
    }

    .filter-btn:hover {
      background: var(--bg-card-hover);
      color: #fff;
    }

    .filter-btn.active {
      background: rgba(6, 182, 212, 0.15);
      border-color: var(--accent-cyan);
      color: var(--accent-cyan);
    }

    .zone-select {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 12px;
      outline: none;
      cursor: pointer;
    }

    #map-view {
      flex: 1;
      width: 100%;
      height: 100%;
      min-height: 500px;
      background: #0f172a;
    }

    .inspector-pane {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }

    .inspector-header {
      padding: 14px 18px;
      border-bottom: 1px solid var(--border-color);
      background: var(--bg-surface);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .inspector-body {
      padding: 16px;
      overflow-y: auto;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .empty-state {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100%;
      text-align: center;
      color: var(--text-dim);
      padding: 40px 20px;
    }

    .detail-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 14px;
    }

    .detail-badge-row {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      margin: 8px 0;
    }

    .badge-pill {
      font-size: 11px;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: 12px;
      background: rgba(255, 255, 255, 0.08);
      color: var(--text-muted);
    }

    .badge-pill.cyan { background: rgba(6, 182, 212, 0.15); color: var(--accent-cyan); border: 1px solid rgba(6, 182, 212, 0.3); }
    .badge-pill.amber { background: rgba(245, 158, 11, 0.15); color: var(--accent-amber); border: 1px solid rgba(245, 158, 11, 0.3); }
    .badge-pill.rose { background: rgba(244, 63, 94, 0.15); color: var(--accent-rose); border: 1px solid rgba(244, 63, 94, 0.3); }
    .badge-pill.emerald { background: rgba(16, 185, 129, 0.15); color: var(--accent-emerald); border: 1px solid rgba(16, 185, 129, 0.3); }
    .badge-pill.purple { background: rgba(168, 85, 247, 0.15); color: var(--accent-purple); border: 1px solid rgba(168, 85, 247, 0.3); }

    .quote-box {
      background: rgba(0, 0, 0, 0.25);
      border-left: 3px solid var(--accent-cyan);
      padding: 10px 12px;
      border-radius: 0 6px 6px 0;
      font-style: italic;
      color: #e2e8f0;
      font-size: 13px;
      margin-top: 8px;
      line-height: 1.5;
    }

    .insight-box {
      background: rgba(245, 158, 11, 0.08);
      border-left: 3px solid var(--accent-amber);
      padding: 10px 12px;
      border-radius: 0 6px 6px 0;
      color: #fed7aa;
      font-size: 12px;
      margin-top: 8px;
      line-height: 1.5;
    }

    .scale-meter-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      margin: 12px 0;
      text-align: center;
    }

    .scale-box {
      background: rgba(0, 0, 0, 0.2);
      border-radius: 6px;
      padding: 8px 4px;
      border: 1px solid var(--border-subtle);
    }

    .scale-title {
      font-size: 10px;
      text-transform: uppercase;
      color: var(--text-dim);
      font-weight: 700;
    }

    .scale-num {
      font-size: 18px;
      font-weight: 800;
      margin-top: 2px;
    }

    .scale-num.good { color: var(--accent-emerald); }
    .scale-num.warning { color: var(--accent-amber); }
    .scale-num.danger { color: var(--accent-rose); }

    /* Map Legends & Overlays */
    .map-legend-panel {
      position: absolute;
      bottom: 24px;
      left: 24px;
      background: rgba(17, 24, 39, 0.92);
      backdrop-filter: blur(8px);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 12px 16px;
      z-index: 400;
      font-size: 12px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
      max-width: 260px;
    }

    .legend-title {
      font-weight: 700;
      margin-bottom: 8px;
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .legend-item {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 5px;
      color: var(--text-muted);
    }

    .legend-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
    }

    .legend-line {
      width: 18px;
      height: 3px;
      border-radius: 2px;
    }

    /* Content Cards & Data Grids */
    .content-grid {
      display: grid;
      gap: 16px;
    }

    .card {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 20px;
    }

    .card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      flex-wrap: wrap;
      gap: 10px;
    }

    .card-title {
      font-size: 16px;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .chart-container {
      position: relative;
      height: 280px;
      width: 100%;
    }

    /* Tables */
    .data-table-wrap {
      overflow-x: auto;
      border-radius: 8px;
      border: 1px solid var(--border-color);
    }

    table.styled-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 13px;
    }

    table.styled-table th {
      background: var(--bg-card);
      padding: 12px 14px;
      color: var(--text-muted);
      font-weight: 600;
      border-bottom: 1px solid var(--border-color);
      white-space: nowrap;
    }

    table.styled-table td {
      padding: 12px 14px;
      border-bottom: 1px solid var(--border-subtle);
      color: var(--text-main);
    }

    table.styled-table tr:hover td {
      background: rgba(255, 255, 255, 0.02);
    }

    /* Search input box */
    .search-input-box {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      color: #fff;
      padding: 6px 12px;
      font-size: 12px;
      outline: none;
      min-width: 220px;
    }

    .search-input-box:focus {
      border-color: var(--accent-cyan);
    }

    /* Media Gallery Grid */
    .media-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 14px;
      margin-top: 14px;
    }

    .media-thumb-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      overflow: hidden;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
    }

    .media-thumb-card:hover {
      transform: translateY(-3px);
      border-color: var(--accent-cyan);
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
    }

    .media-thumb-img-wrap {
      width: 100%;
      height: 140px;
      background: #000;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }

    .media-thumb-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.3s ease;
    }

    .media-thumb-card:hover .media-thumb-img-wrap img {
      transform: scale(1.05);
    }

    .media-type-tag {
      position: absolute;
      top: 8px;
      left: 8px;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(4px);
      border-radius: 4px;
      padding: 2px 6px;
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .media-type-tag.video { color: var(--accent-cyan); }
    .media-type-tag.photo { color: var(--accent-amber); }

    .media-duration-tag {
      position: absolute;
      bottom: 8px;
      right: 8px;
      background: rgba(0, 0, 0, 0.85);
      border-radius: 4px;
      padding: 2px 6px;
      font-size: 10px;
      font-weight: 600;
      color: #fff;
    }

    .media-info {
      padding: 12px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      flex: 1;
    }

    .media-title {
      font-size: 12px;
      font-weight: 700;
      color: #fff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .media-meta {
      font-size: 11px;
      color: var(--text-muted);
      margin-top: 4px;
      line-height: 1.3;
    }

    /* Modal / Lightbox */
    .modal-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(8px);
      z-index: 2000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }

    .modal-backdrop.open {
      display: flex;
      animation: modalFade 0.2s ease;
    }

    @keyframes modalFade {
      from { opacity: 0; transform: scale(0.97); }
      to { opacity: 1; transform: scale(1); }
    }

    .modal-box {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      max-width: 820px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      padding: 20px;
      position: relative;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7);
    }

    .modal-close-btn {
      position: absolute;
      top: 16px;
      right: 16px;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: #fff;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 16px;
      transition: background 0.2s;
      z-index: 10;
    }

    .modal-close-btn:hover {
      background: var(--accent-rose);
    }

    /* Responsive */
    @media (max-width: 768px) {
      header {
        padding: 12px 16px;
      }
      main {
        padding: 12px 16px;
      }
      .stats-bar {
        padding: 12px 16px 0 16px;
        grid-template-columns: 1fr 1fr;
      }
      .nav-tabs {
        width: 100%;
        overflow-x: auto;
      }
    }
  </style>
</head>
<body>

  <!-- ================================================================== -->
  <!-- HEADER & NAVIGATION                                                -->
  <!-- ================================================================== -->
  <header>
    <div class="brand-group">
      <div class="brand-logo">P</div>
      <div class="brand-text">
        <h1>Pijak Empirical Field Research Dashboard</h1>
        <p>Sudirman Pedestrian Corridor & Dukuh Atas TOD • Field Day 1 (June 18, 2026)</p>
      </div>
    </div>

    <div class="nav-tabs">
      <button class="nav-tab active" onclick="switchTab('geo-studio')">
        <i data-lucide="map"></i> Geo-Studio Map
      </button>
      <button class="nav-tab" onclick="switchTab('respondents-view')">
        <i data-lucide="users"></i> Respondents & Intercepts (24)
      </button>
      <button class="nav-tab" onclick="switchTab('microclimate-view')">
        <i data-lucide="thermometer-sun"></i> Microclimate & Thermal Impact
      </button>
      <button class="nav-tab" onclick="switchTab('gradient-view')">
        <i data-lucide="trending-down"></i> Urban Gradient
      </button>
      <button class="nav-tab" onclick="switchTab('media-gallery')">
        <i data-lucide="image"></i> Field Media & Assets (105)
      </button>
      <button class="nav-tab" onclick="switchTab('synthesis-view')">
        <i data-lucide="file-text"></i> Research Synthesis
      </button>
    </div>

    <div class="header-actions">
      <span class="tag-badge">
        <i data-lucide="check-circle-2" style="width:14px;height:14px;"></i> Ground Truth Verified
      </span>
      <button class="filter-btn" onclick="window.print()" title="Print / Export PDF">
        <i data-lucide="printer" style="width:14px;height:14px;"></i> Export Report
      </button>
    </div>
  </header>

  <!-- ================================================================== -->
  <!-- STAT SUMMARY CARDS BANNER                                          -->
  <!-- ================================================================== -->
  <div class="stats-bar">
    <div class="stat-card card-blue">
      <div class="stat-top">
        <span class="stat-label">Field Intercepts</span>
        <i data-lucide="mic" style="width:16px;height:16px;color:var(--accent-blue);"></i>
      </div>
      <div class="stat-val-group">
        <span class="stat-val">24</span>
        <span style="font-weight:600;color:var(--text-muted);font-size:13px;">respondents</span>
      </div>
      <div class="stat-subtext">12 Audio-recorded + 12 Field Notulen</div>
    </div>

    <div class="stat-card card-amber">
      <div class="stat-top">
        <span class="stat-label">Geotagged Media</span>
        <i data-lucide="camera" style="width:16px;height:16px;color:var(--accent-amber);"></i>
      </div>
      <div class="stat-val-group">
        <span class="stat-val">105</span>
        <span style="font-weight:600;color:var(--text-muted);font-size:13px;">points</span>
      </div>
      <div class="stat-subtext">37 Photos • 68 Videos (84 in Documentations/)</div>
    </div>

    <div class="stat-card card-rose">
      <div class="stat-top">
        <span class="stat-label">Peak Microclimate</span>
        <i data-lucide="sun" style="width:16px;height:16px;color:var(--accent-rose);"></i>
      </div>
      <div class="stat-val-group">
        <span class="stat-val">35°C</span>
        <span style="font-weight:600;color:var(--accent-rose);font-size:13px;">feels like</span>
      </div>
      <div class="stat-subtext">UV Index 8 (Very High) • +3°C Above Normal</div>
    </div>

    <div class="stat-card card-emerald">
      <div class="stat-top">
        <span class="stat-label">Pedestrian Network</span>
        <i data-lucide="git-branch" style="width:16px;height:16px;color:var(--accent-emerald);"></i>
      </div>
      <div class="stat-val-group">
        <span class="stat-val">680</span>
        <span style="font-weight:600;color:var(--text-muted);font-size:13px;">edges</span>
      </div>
      <div class="stat-subtext">OpenSidewalks Schema (~28.5 km mapped)</div>
    </div>

    <div class="stat-card card-purple">
      <div class="stat-top">
        <span class="stat-label">Sidewalk Disparity</span>
        <i data-lucide="shield-alert" style="width:16px;height:16px;color:var(--accent-purple);"></i>
      </div>
      <div class="stat-val-group">
        <span class="stat-val">100% → 0%</span>
      </div>
      <div class="stat-subtext">Sudirman Spine vs Back-Streets Gradient</div>
    </div>
  </div>

  <!-- ================================================================== -->
  <!-- MAIN TABS CONTAINER                                                -->
  <!-- ================================================================== -->
  <main>

    <!-- ============================================================== -->
    <!-- TAB 1: GEO-STUDIO MAP VIEW                                     -->
    <!-- ============================================================== -->
    <div id="geo-studio" class="tab-panel active">
      <div class="geo-layout">
        <div class="map-pane">
          <div class="map-toolbar">
            <div class="filter-group">
              <span style="font-size:11px;font-weight:700;color:var(--text-dim);text-transform:uppercase;">Layers:</span>
              <button class="filter-btn active" id="layer-resp-toggle" onclick="toggleMapLayer('respondents')">
                <i data-lucide="users" style="width:13px;height:13px;"></i> Respondents (24)
              </button>
              <button class="filter-btn active" id="layer-media-toggle" onclick="toggleMapLayer('media')">
                <i data-lucide="camera" style="width:13px;height:13px;"></i> Field Media (105)
              </button>
              <button class="filter-btn active" id="layer-network-toggle" onclick="toggleMapLayer('network')">
                <i data-lucide="git-branch" style="width:13px;height:13px;"></i> Pedestrian Network (680)
              </button>
              <button class="filter-btn" id="layer-places-toggle" onclick="toggleMapLayer('places')">
                <i data-lucide="map-pin" style="width:13px;height:13px;"></i> POIs (110)
              </button>
            </div>

            <div class="filter-group">
              <select id="jump-zone-select" class="zone-select" onchange="jumpToZone(this.value)">
                <option value="">-- Jump to Transect Zone --</option>
                <option value="dukuh_atas">1. Dukuh Atas Transit Hub & Kendal</option>
                <option value="karet">2. Sudirman - Karet & JPO Phinisi</option>
                <option value="semanggi">3. Semanggi Interchange & Atma Jaya</option>
                <option value="senayan">4. Polda Metro Jaya & Senayan</option>
                <option value="kebon_melati">5. Kebon Melati (Urban Gradient)</option>
              </select>
              <input type="text" id="map-search" class="search-input-box" placeholder="Search ID, role, street..." oninput="searchMapPins(this.value)" />
            </div>
          </div>

          <div id="map-view"></div>

          <!-- Map Legend -->
          <div class="map-legend-panel">
            <div class="legend-title">
              <span>Map Legend</span>
              <i data-lucide="layers" style="width:14px;height:14px;"></i>
            </div>
            <div class="legend-item">
              <div class="legend-dot" style="background:#3b82f6;"></div>
              <span>Respondent: Upper / Middle Class</span>
            </div>
            <div class="legend-item">
              <div class="legend-dot" style="background:#f59e0b;"></div>
              <span>Respondent: Bottom / Vulnerable Worker</span>
            </div>
            <div class="legend-item">
              <div class="legend-dot" style="background:#ef4444;"></div>
              <span>Field Geotagged Photo (37)</span>
            </div>
            <div class="legend-item">
              <div class="legend-dot" style="background:#06b6d4;"></div>
              <span>Field Geotagged Video Clip (68)</span>
            </div>
            <div class="legend-item">
              <div class="legend-line" style="background:#06b6d4;"></div>
              <span>Sidewalk Segment (Wide Paved)</span>
            </div>
            <div class="legend-item">
              <div class="legend-line" style="background:#f59e0b;border-top:1px dashed #f59e0b;"></div>
              <span>Zebra Cross / Pedestrian Crossing</span>
            </div>
            <div class="legend-item">
              <div class="legend-line" style="background:#10b981;"></div>
              <span>Dedicated Footway / JPO Link</span>
            </div>
          </div>
        </div>

        <!-- Right Inspector Drawer -->
        <div class="inspector-pane">
          <div class="inspector-header">
            <div style="font-weight:700;display:flex;align-items:center;gap:8px;">
              <i data-lucide="info" style="color:var(--accent-cyan);width:16px;height:16px;"></i>
              <span>Inspector Detail</span>
            </div>
            <span class="badge-pill" id="inspector-badge">Click any marker</span>
          </div>
          <div class="inspector-body" id="inspector-content">
            <div class="empty-state">
              <i data-lucide="crosshair" style="width:48px;height:48px;margin-bottom:12px;opacity:0.4;"></i>
              <h3 style="font-size:15px;color:#fff;margin-bottom:6px;">Select a Point on the Map</h3>
              <p style="font-size:12px;line-height:1.5;">Click any respondent pin, geotagged photo, video point, or street edge to inspect verbatim transcripts, scores, and media previews.</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ============================================================== -->
    <!-- TAB 2: RESPONDENTS & INTERCEPTS VIEW                            -->
    <!-- ============================================================== -->
    <div id="respondents-view" class="tab-panel">
      
      <!-- Charts Row 1: Demographics Breakdown (Age & Gender) -->
      <div class="content-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); margin-bottom: 20px;">
        <div class="card">
          <div class="card-header">
            <div class="card-title"><i data-lucide="users" style="color:var(--accent-rose);"></i> Gender Breakdown</div>
            <span class="badge-pill rose">18M / 6F (75% / 25%)</span>
          </div>
          <div class="chart-container" style="height: 220px;">
            <canvas id="chart-gender-dist"></canvas>
          </div>
        </div>

        <div class="card">
          <div class="card-header">
            <div class="card-title"><i data-lucide="calendar" style="color:var(--accent-purple);"></i> Age Group Profiles</div>
            <span class="badge-pill purple">5 Cohorts</span>
          </div>
          <div class="chart-container" style="height: 220px;">
            <canvas id="chart-age-dist"></canvas>
          </div>
        </div>

        <div class="card">
          <div class="card-header">
            <div class="card-title"><i data-lucide="pie-chart" style="color:var(--accent-cyan);"></i> Socio-Economic Class</div>
            <span class="badge-pill cyan">Frontline vs Commuter</span>
          </div>
          <div class="chart-container" style="height: 220px;">
            <canvas id="chart-class-dist"></canvas>
          </div>
        </div>
      </div>

      <!-- Charts Row 2: Mobility Modes & Perceptions -->
      <div class="content-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 20px;">
        <div class="card">
          <div class="card-header">
            <div class="card-title"><i data-lucide="footprints" style="color:var(--accent-emerald);"></i> Mobility & Access Modes</div>
            <span class="badge-pill emerald">First/Last-Mile</span>
          </div>
          <div class="chart-container" style="height: 240px;">
            <canvas id="chart-modes-dist"></canvas>
          </div>
        </div>

        <div class="card">
          <div class="card-header">
            <div class="card-title"><i data-lucide="bar-chart-2" style="color:var(--accent-amber);"></i> Stated vs Interpreted Comfort Scores</div>
            <span class="badge-pill amber">7.0 Stated vs 4.0-9.0 Range</span>
          </div>
          <div class="chart-container" style="height: 240px;">
            <canvas id="chart-comfort-dist"></canvas>
          </div>
        </div>
      </div>

      <!-- Respondents Full Table -->
      <div class="card" style="margin-bottom: 20px;">
        <div class="card-header">
          <div class="card-title">
            <i data-lucide="table" style="color:var(--accent-cyan);"></i>
            <span>All 24 Field Intercepts & Notulen Records</span>
          </div>
          <div class="filter-group">
            <input type="text" id="resp-table-search" class="search-input-box" placeholder="Filter by role, pain point, name..." oninput="filterRespondentsTable(this.value)" />
          </div>
        </div>

        <div class="data-table-wrap">
          <table class="styled-table" id="resp-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Role / Informant</th>
                <th>Gender</th>
                <th>Age Cohort</th>
                <th>Location</th>
                <th>Class</th>
                <th>Mode</th>
                <th>Comfort</th>
                <th>Security</th>
                <th>Heat Discomfort</th>
                <th>Scale Type</th>
                <th>Key Grievance / Finding</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody id="resp-table-body">
              <!-- Rendered via JS -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- Qualitative Excerpt Cards -->
      <div class="card">
        <div class="card-header">
          <div class="card-title">
            <i data-lucide="message-square" style="color:var(--accent-cyan);"></i>
            <span>Verbatim Audio Transcripts & Field Voices</span>
          </div>
          <span style="font-size:12px;color:var(--text-muted);">Audio Intercepts 01–12 (Recorded 2026-06-18)</span>
        </div>
        <div class="content-grid" style="grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));" id="resp-cards-grid">
          <!-- Rendered via JS -->
        </div>
      </div>

    </div>

    <!-- ============================================================== -->
    <!-- TAB 3: MICROCLIMATE & THERMAL IMPACT VIEW                      -->
    <!-- ============================================================== -->
    <div id="microclimate-view" class="tab-panel">
      
      <div class="card" style="margin-bottom: 20px;">
        <div class="card-header">
          <div>
            <div class="card-title" style="font-size:18px;">
              Synchronized Apple WeatherKit Field Measurements
            </div>
            <p style="font-size:13px;color:var(--text-muted);margin-top:4px;">
              Logged during Field Day 1 (June 18, 2026, 10:20–13:35 WIB) across the Sudirman transect. The field team measured temperatures consistently exceeding the thermal comfort threshold (THI > 27°C), peaking at <strong>35°C Feels-Like</strong> under oppressive <strong>UV 8 (Very High)</strong> solar radiation.
            </p>
          </div>
          <div class="filter-group">
            <span class="badge-pill rose" style="font-size:12px;padding:6px 12px;">
              <i data-lucide="flame" style="width:13px;height:13px;display:inline-block;vertical-align:middle;"></i> Extreme Midday Heat
            </span>
            <span class="badge-pill emerald" style="font-size:12px;padding:6px 12px;">
              <i data-lucide="check" style="width:13px;height:13px;display:inline-block;vertical-align:middle;"></i> 0mm Rain Recorded
            </span>
          </div>
        </div>
      </div>

      <!-- Time Series Charts Grid -->
      <div class="content-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 20px;">
        <div class="card">
          <div class="card-header">
            <div class="card-title"><i data-lucide="thermometer" style="color:var(--accent-rose);"></i> Ambient vs Feels-Like Temperature Timeline (°C)</div>
            <span class="badge-pill rose">Gap: +2°C to +3°C Heat Index</span>
          </div>
          <div class="chart-container" style="height: 300px;">
            <canvas id="chart-weather-temp"></canvas>
          </div>
          <div style="font-size:11px;color:var(--text-dim);margin-top:8px;">
            *Red dashed line indicates the 27°C Temperature-Humidity Index (THI) threshold above which pedestrian discomfort sets in rapidly in tropical cities.
          </div>
        </div>

        <div class="card">
          <div class="card-header">
            <div class="card-title"><i data-lucide="sun" style="color:var(--accent-amber);"></i> Solar UV Index & Humidity Progression</div>
            <span class="badge-pill amber">UV Index 8 (Very High)</span>
          </div>
          <div class="chart-container" style="height: 300px;">
            <canvas id="chart-weather-uv"></canvas>
          </div>
          <div style="font-size:11px;color:var(--text-dim);margin-top:8px;">
            *WHO advisory mandates sun protection (umbrella, continuous shade) from 10:00 to 16:00 WIB.
          </div>
        </div>
      </div>

      <div class="content-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 20px;">
        <div class="card">
          <div class="card-header">
            <div class="card-title"><i data-lucide="wind" style="color:var(--accent-cyan);"></i> Wind Velocity & Gusts (km/h)</div>
            <span class="badge-pill cyan">Near-Stagnant Air</span>
          </div>
          <div class="chart-container" style="height: 250px;">
            <canvas id="chart-weather-wind"></canvas>
          </div>
          <div style="font-size:11px;color:var(--text-dim);margin-top:8px;">
            *Light wind (8–11 km/h) exacerbated perceived heat index, preventing natural radiative convective cooling on paved sidewalks.
          </div>
        </div>

        <div class="card">
          <div class="card-header">
            <div class="card-title"><i data-lucide="activity" style="color:var(--accent-emerald);"></i> Field Weather Logs Table</div>
            <span class="badge-pill emerald">6 Synchronized Epochs</span>
          </div>
          <div class="data-table-wrap" style="max-height: 270px; overflow-y:auto;">
            <table class="styled-table">
              <thead>
                <tr>
                  <th>Time</th>
                  <th>Location</th>
                  <th>Air Temp</th>
                  <th>Feels Like</th>
                  <th>Humidity</th>
                  <th>UV</th>
                  <th>Condition</th>
                </tr>
              </thead>
              <tbody id="weather-table-body">
                <!-- Rendered via JS -->
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </div>

    <!-- ============================================================== -->
    <!-- TAB 4: THE URBAN GRADIENT (Q4)                                  -->
    <!-- ============================================================== -->
    <div id="gradient-view" class="tab-panel">
      
      <div class="card" style="margin-bottom: 20px;">
        <div class="card-header">
          <div>
            <div class="card-title" style="font-size:18px;">
              <i data-lucide="trending-down" style="color:var(--accent-rose);"></i>
              The Infrastructure Drop-Off: The Urban Gradient (Q4)
            </div>
            <p style="font-size:13px;color:var(--text-muted);margin-top:4px;">
              Analysis based on OpenSidewalks spatial audit (<code>gradient.csv</code>). Walking 100 meters off Jalan Sudirman results in a catastrophic drop from world-class wide sidewalks to zero pedestrian infrastructure in residential kampung back-streets.
            </p>
          </div>
          <span class="badge-pill rose" style="font-size:12px;padding:6px 12px;">Severe Pedestrian Disparity</span>
        </div>
      </div>

      <div class="content-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 20px;">
        <div class="card">
          <div class="card-header">
            <div class="card-title">Sidewalk Infrastructure Percentage by Street</div>
          </div>
          <div class="chart-container" style="height: 380px;">
            <canvas id="chart-gradient-streets"></canvas>
          </div>
        </div>

        <div class="card" style="display:flex;flex-direction:column;justify-content:space-between;">
          <div>
            <div class="card-title" style="margin-bottom:12px;color:var(--accent-cyan);">
              The "Skyscraper Wall" Phenomenon
            </div>
            <p style="font-size:13px;color:#cbd5e1;line-height:1.6;margin-bottom:14px;">
              Jalan Jenderal Sudirman displays near 100% sidewalk provision (8–10 meters wide, tactile paving, landscaping). However, secondary streets (Jalan Bendungan Hilir, KH Mas Mansyur) and tertiary lanes (Kebon Melati residential alleys) drop to 0%–20% sidewalk coverage.
            </p>
            
            <div style="background:rgba(245, 158, 11, 0.08);border-left:4px solid var(--accent-amber);padding:14px;border-radius:0 8px 8px 0;margin-bottom:16px;">
              <h4 style="color:var(--accent-amber);font-size:13px;font-weight:700;margin-bottom:6px;">Key Field Contact: Respondent N09 (Bapak Lansia Kebon Melati)</h4>
              <p style="font-style:italic;color:#fef3c7;font-size:13px;line-height:1.5;">
                "Di Kebon Melati ada rumah-rumah pejabat pemerintah; gak pernah banjir karena ada waduk. MRT itu dulunya lapangan tenis."
              </p>
              <div style="font-size:11px;color:var(--text-dim);margin-top:6px;">
                N09 was the solitary resident sampled inside the back-area gradient on Day 1. While the main corridor is sterile and hyper-modern, the back-area maintains informal social memory and unpaved, mixed-traffic pedestrian realities.
              </div>
            </div>
          </div>

          <div class="detail-card">
            <h4 style="font-size:13px;color:var(--accent-emerald);font-weight:700;margin-bottom:6px;">Spatial Network Audit Summary</h4>
            <div style="font-size:12px;color:var(--text-muted);line-height:1.5;">
              680 pedestrian segments mapped across 28.5 km. Over 548 segments have unverified or unknown surface quality in open databases, proving the vital necessity of physical field audits.
            </div>
          </div>
        </div>
      </div>

    </div>

    <!-- ============================================================== -->
    <!-- TAB 5: FIELD MEDIA & ASSETS GALLERY                            -->
    <!-- ============================================================== -->
    <div id="media-gallery" class="tab-panel">
      
      <div class="card" style="margin-bottom:20px;">
        <div class="card-header">
          <div class="card-title">
            <i data-lucide="image" style="color:var(--accent-cyan);"></i>
            <span>Geotagged Photo & Video Evidence Gallery (105 Points)</span>
          </div>
          <div class="filter-group">
            <button class="filter-btn active" onclick="filterGallery('all', this)">All (105)</button>
            <button class="filter-btn" onclick="filterGallery('photo', this)">Photos (37)</button>
            <button class="filter-btn" onclick="filterGallery('video', this)">Videos (68)</button>
            <button class="filter-btn" onclick="filterGallery('has_thumb', this)">Local Files (84)</button>
            <button class="filter-btn" onclick="filterGallery('danger', this)">Micro-Hazards</button>
            <button class="filter-btn" onclick="filterGallery('warning', this)">Thermal / Gradient</button>
          </div>
        </div>

        <div class="media-grid" id="gallery-container">
          <!-- Rendered via JS -->
        </div>
      </div>

    </div>

    <!-- ============================================================== -->
    <!-- TAB 6: RESEARCH SYNTHESIS & FINDINGS                            -->
    <!-- ============================================================== -->
    <div id="synthesis-view" class="tab-panel">
      
      <div class="content-grid" style="grid-template-columns: repeat(auto-fit, minmax(420px, 1fr));">
        
        <!-- Finding 1 -->
        <div class="card" style="border-top:3px solid var(--accent-cyan);">
          <div class="card-header">
            <div class="card-title" style="font-size:15px;">
              <i data-lucide="check-circle" style="color:var(--accent-cyan);"></i>
              1. The Sidewalk Infrastructure Quality Paradox
            </div>
            <span class="badge-pill cyan">Counter-Framing</span>
          </div>
          <p style="font-size:13px;color:#cbd5e1;line-height:1.6;margin-bottom:12px;">
            The mentor flagged the suspicion that pedestrians "walk in the road despite a good sidewalk". The field intercepts strongly rebut this on the main corridor: respondents overwhelmingly rate the trotoar as <em>enak, lega, luas, manusiawi, dan bagus</em> (7/10 to 9/10).
          </p>
          <div class="quote-box">
            "Trotoarnya udah bagus... Udah manusiawi? Udah. Udah gede? Udah."<br/>
            — Bapak Kritik (R11)
          </div>
          <p style="font-size:12px;color:var(--text-muted);margin-top:10px;">
            <strong>Implication:</strong> The design opportunity is NOT "fixing the trotoar", but solving what sits ON TOP of a good sidewalk: extreme climate heat, micro-level tripping hazards, and nighttime isolation.
          </p>
        </div>

        <!-- Finding 2 -->
        <div class="card" style="border-top:3px solid var(--accent-rose);">
          <div class="card-header">
            <div class="card-title" style="font-size:15px;">
              <i data-lucide="sun" style="color:var(--accent-rose);"></i>
              2. Heat as a Four-Season Template Design Failure
            </div>
            <span class="badge-pill rose">Extreme Heat</span>
          </div>
          <p style="font-size:13px;color:#cbd5e1;line-height:1.6;margin-bottom:12px;">
            Heat is the dominant daytime grievance across all demographics (R02, R03, R04, R07, R10, R11, R12). At 35°C feels-like, wide open boulevards act as thermal ovens.
          </p>
          <div class="quote-box">
            "Studi bandingnya ke negara 4 musim... pohon belum efektif menahan panas... malam hari rimbunnya pohon malah nutupin lampu jalan jadi gelap dan banyak nyamuk!" — R11
          </div>
          <p style="font-size:12px;color:var(--text-muted);margin-top:10px;">
            <strong>Implication:</strong> Pedestrians adapt via umbrellas (R05) or abandon walking for motorbikes (R07). Continuous physical sun/rain canopies and optimized tree canopy structures are desperately needed.
          </p>
        </div>

        <!-- Finding 3 -->
        <div class="card" style="border-top:3px solid var(--accent-purple);">
          <div class="card-header">
            <div class="card-title" style="font-size:15px;">
              <i data-lucide="moon" style="color:var(--accent-purple);"></i>
              3. Night Safety: Isolation Hotspots, Not Darkness
            </div>
            <span class="badge-pill purple">Criminology</span>
          </div>
          <p style="font-size:13px;color:#cbd5e1;line-height:1.6;margin-bottom:12px;">
            Daytime safety is rated reassuringly high (police presence, active crowds). Nighttime risk escalates sharply after 22:00 at specific vertical nodes: upper JPO decks and unmonitored parking lots.
          </p>
          <div class="quote-box">
            "Terang sih, di atas terang... cuma SEPI. Nunggu momen yang tepat..."<br/>
            — Informan Keamanan (R09)
          </div>
          <p style="font-size:12px;color:var(--text-muted);margin-top:10px;">
            <strong>Implication:</strong> Simply installing streetlamps is insufficient. Safe night walking requires "eyes on the street", commercial activation, and integrated security patrols.
          </p>
        </div>

        <!-- Finding 4 -->
        <div class="card" style="border-top:3px solid var(--accent-amber);">
          <div class="card-header">
            <div class="card-title" style="font-size:15px;">
              <i data-lucide="alert-triangle" style="color:var(--accent-amber);"></i>
              4. Universal Accessibility Defect: Steep Curb Drops
            </div>
            <span class="badge-pill amber">Injury Hazard</span>
          </div>
          <p style="font-size:13px;color:#cbd5e1;line-height:1.6;margin-bottom:12px;">
            Multiple independent reports verify that the curb-to-zebra cross transition ramp is dangerously steep and slippery when wet.
          </p>
          <div class="quote-box">
            "Perbedaan tinggi trotoar dengan zebra cross kurang... teman aku jatuh 2x kemarin dan barusan tadi... Motor gak mau ngalah sama pejalan kaki." — R05
          </div>
          <p style="font-size:12px;color:var(--text-muted);margin-top:10px;">
            <strong>Implication:</strong> Civil engineering audit of curb transitions: slope gradients, non-slip textured surfaces, and grade-separated raised crosswalks.
          </p>
        </div>

        <!-- Finding 5 -->
        <div class="card" style="border-top:3px solid var(--accent-emerald);">
          <div class="card-header">
            <div class="card-title" style="font-size:15px;">
              <i data-lucide="bike" style="color:var(--accent-emerald);"></i>
              5. Vehicular Intrusion & Inter-Agency Gaps
            </div>
            <span class="badge-pill emerald">Enforcement Gap</span>
          </div>
          <p style="font-size:13px;color:#cbd5e1;line-height:1.6;margin-bottom:12px;">
            Motorcycle taxis (ojol) routinely drive onto pedestrian sidewalks and cut through the Terowongan Kendal pedestrian tunnel, creating acute collision dangers.
          </p>
          <div class="insight-box">
            Enforcement dilemma: Satpol PP monitors informal street vendors (PKL), while moving vehicular violations fall under Dishub (Transportation Agency). Between both, sidewalks remain unpoliced.
          </div>
          <p style="font-size:12px;color:var(--text-muted);margin-top:10px;">
            <strong>Implication:</strong> Physical bollard barriers and unified municipal enforcement task forces.
          </p>
        </div>

        <!-- Finding 6 -->
        <div class="card" style="border-top:3px solid var(--accent-blue);">
          <div class="card-header">
            <div class="card-title" style="font-size:15px;">
              <i data-lucide="network" style="color:var(--accent-blue);"></i>
              6. Institutional Fragmentation & Citizen Voice
            </div>
            <span class="badge-pill">Governance</span>
          </div>
          <p style="font-size:13px;color:#cbd5e1;line-height:1.6;margin-bottom:12px;">
            Transit plazas suffer from territorial siloing: KAI, MRT, Kawis, and MITJ manage separate boundaries; interstitial public spaces are left in a jurisdictional vacuum.
          </p>
          <div class="quote-box">
            "Fasilitas infrastruktur rusak dan gak rata, SUDAH DILAPORKAN TAPI GAK PERNAH DIGUBRIS PEMERINTAH... Sering kesandung." — Mas Arief & Ibu Lis (N11, N12)
          </div>
          <p style="font-size:12px;color:var(--text-muted);margin-top:10px;">
            <strong>Implication:</strong> Direct impetus for Pijak's crowd-sourced geo-hazard reporting interface with automated escalation directly to relevant agency endpoints.
          </p>
        </div>

      </div>

    </div>

  </main>

  <!-- ================================================================== -->
  <!-- MEDIA PREVIEW MODAL / LIGHTBOX                                      -->
  <!-- ================================================================== -->
  <div id="media-modal" class="modal-backdrop" onclick="closeMediaModal(event)">
    <div class="modal-box" onclick="event.stopPropagation()">
      <button class="modal-close-btn" onclick="closeMediaModal()">&times;</button>
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:14px;">
        <i data-lucide="play-circle" style="color:var(--accent-cyan);width:20px;height:20px;"></i>
        <h3 id="modal-title" style="font-size:16px;color:#fff;">Media Asset Preview</h3>
      </div>
      <div id="modal-body-content">
        <!-- Rendered dynamically -->
      </div>
    </div>
  </div>

  <!-- ================================================================== -->
  <!-- DATA & JAVASCRIPT APPLICATION LOGIC                                -->
  <!-- ================================================================== -->
  <script>
    // Embedded Field Research Datasets
    const RESPONDENTS = """ + json.dumps(respondents_data) + """;
    const MEDIA_POINTS = """ + json.dumps(media_data) + """;
    const WEATHER = """ + json.dumps(weather_list) + """;
    const PEDESTRIAN_NET = """ + json.dumps(pnet_geojson) + """;
    const GRADIENT = """ + json.dumps(gradient_data) + """;
    const PLACES = """ + json.dumps(places_data) + """;

    // Application State
    let map = null;
    const layers = {
      network: null,
      media: null,
      respondents: null,
      places: null
    };

    let respondentChartsInit = false;
    let microclimateChartsInit = false;
    let gradientChartsInit = false;

    window.respondentChartsList = [];
    window.microclimateChartsList = [];
    window.gradientChartsList = [];

    // Helper: Determine asset base path relative to HTML location
    function resolveAssetUrl(relPath) {
      if (!relPath) return '';
      const isSub = window.location.pathname.includes('/investigate/field');
      if (isSub) {
        return '../../' + relPath.replace(/^\\.\\//, '');
      }
      return relPath;
    }

    // Initialize application on DOM ready
    document.addEventListener('DOMContentLoaded', () => {
      lucide.createIcons();
      initMap();
      renderRespondentsTable();
      renderRespondentCards();
      renderGalleryItems(MEDIA_POINTS);
      renderWeatherTable();
    });

    // Tab Navigation
    function switchTab(tabId) {
      document.querySelectorAll('.nav-tab').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
      
      const btn = Array.from(document.querySelectorAll('.nav-tab')).find(b => b.getAttribute('onclick').includes(tabId));
      if (btn) btn.classList.add('active');

      const panel = document.getElementById(tabId);
      if (panel) panel.classList.add('active');

      // Trigger map resize if switching to map
      if (tabId === 'geo-studio' && map) {
        setTimeout(() => map.invalidateSize(), 150);
      }

      // Initialize tab charts when activated
      if (tabId === 'microclimate-view') {
        if (!microclimateChartsInit) {
          initMicroclimateCharts();
          microclimateChartsInit = true;
        } else {
          resizeCharts(window.microclimateChartsList);
        }
      } else if (tabId === 'respondents-view') {
        if (!respondentChartsInit) {
          initRespondentCharts();
          respondentChartsInit = true;
        } else {
          resizeCharts(window.respondentChartsList);
        }
      } else if (tabId === 'gradient-view') {
        if (!gradientChartsInit) {
          initGradientCharts();
          gradientChartsInit = true;
        } else {
          resizeCharts(window.gradientChartsList);
        }
      }

      lucide.createIcons();
    }

    function resizeCharts(chartList) {
      if (Array.isArray(chartList)) {
        setTimeout(() => {
          chartList.forEach(c => {
            if (c && typeof c.resize === 'function') c.resize();
          });
        }, 100);
      }
    }

    // Leaflet Map Initialization
    function initMap() {
      map = L.map('map-view', {
        center: [-6.2085, 106.8205],
        zoom: 14,
        zoomControl: true
      });

      // 1. Clean basemap layers without watermark or API key requirements
      const osmStandard = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      });

      const esriCanvas = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}', {
        maxZoom: 16,
        attribution: 'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ'
      });

      const esriSatellite = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
        maxZoom: 18,
        attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS'
      });

      // Default to OSM Standard
      osmStandard.addTo(map);

      // Layer 1: Pedestrian Network
      layers.network = L.geoJSON(PEDESTRIAN_NET, {
        style: function(feature) {
          const kind = (feature.properties && feature.properties.kind) || 'other';
          if (kind === 'sidewalk') {
            return { color: '#06b6d4', weight: 3.5, opacity: 0.85 };
          } else if (kind === 'crossing') {
            return { color: '#f59e0b', weight: 4, dashArray: '4, 4', opacity: 0.9 };
          } else if (kind === 'footway') {
            return { color: '#10b981', weight: 2.5, opacity: 0.85 };
          }
          return { color: '#64748b', weight: 1.5, opacity: 0.6 };
        },
        onEachFeature: function(feature, layer) {
          const p = feature.properties || {};
          layer.bindTooltip(`<strong>${p.street_name || 'Pedestrian Path'}</strong><br/>Kind: ${p.kind || 'unknown'} • Length: ${Math.round(p.length_m || 0)}m`, { sticky: true });
          layer.on('click', () => inspectNetworkEdge(p));
        }
      }).addTo(map);

      // Layer 2: Field Media Points (105)
      const mediaMarkers = [];
      MEDIA_POINTS.forEach((m, idx) => {
        const isPhoto = m.type === 'photo';
        const color = isPhoto ? '#ef4444' : '#06b6d4';
        const iconSvg = isPhoto 
          ? `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="${color}" stroke-width="2.5"><path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/></svg>`
          : `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="${color}" stroke-width="2.5"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg>`;

        const customIcon = L.divIcon({
          className: 'custom-media-marker',
          html: `<div style="background:#111827;border:2px solid ${color};border-radius:50%;width:26px;height:26px;display:flex;align-items:center;justify-content:center;box-shadow:0 3px 8px rgba(0,0,0,0.5);">${iconSvg}</div>`,
          iconSize: [26, 26],
          iconAnchor: [13, 13]
        });

        const marker = L.marker([m.lat, m.lon], { icon: customIcon });
        marker.on('click', () => inspectMedia(m));
        marker.bindTooltip(`<strong>${m.filename}</strong> (${m.type})<br/>${m.category}`, { direction: 'top' });

        const popupContent = `
          <div style="font-family:var(--font-sans);min-width:200px;color:#1e293b;">
            <div style="font-weight:700;font-size:13px;margin-bottom:2px;">${m.filename} (${m.type.toUpperCase()})</div>
            <div style="font-size:11px;color:#64748b;margin-bottom:4px;">📍 ${m.zone}</div>
            <div style="font-size:11px;background:#f1f5f9;padding:4px 6px;border-radius:4px;margin-bottom:8px;font-weight:600;color:#0369a1;">${m.category}</div>
            <div style="display:flex;gap:6px;">
              <button onclick="inspectMediaByIndex(${idx}); map.closePopup();" style="flex:1;background:#0284c7;color:#fff;border:none;border-radius:4px;padding:5px 8px;font-size:11px;cursor:pointer;font-weight:600;">Inspect</button>
              <button onclick="openMediaLightboxByIndex(${idx}); map.closePopup();" style="flex:1;background:#334155;color:#fff;border:none;border-radius:4px;padding:5px 8px;font-size:11px;cursor:pointer;">Preview</button>
            </div>
          </div>
        `;
        marker.bindPopup(popupContent);
        mediaMarkers.push(marker);
      });
      layers.media = L.featureGroup(mediaMarkers).addTo(map);

      // Layer 3: Respondent Intercepts (24)
      const respMarkers = [];
      RESPONDENTS.forEach(r => {
        const isUpper = r.class === 'upper_middle';
        const pinColor = isUpper ? '#3b82f6' : '#f59e0b';
        
        const customIcon = L.divIcon({
          className: 'custom-resp-marker',
          html: `<div style="background:${pinColor};color:#041019;font-weight:800;font-size:10px;border:2px solid #fff;border-radius:8px;padding:2px 5px;box-shadow:0 4px 12px rgba(0,0,0,0.6);display:flex;align-items:center;gap:3px;transform:translate(-50%, -50%);">
            <span>${r.id}</span>
          </div>`,
          iconSize: [32, 20]
        });

        const marker = L.marker([r.lat, r.lon], { icon: customIcon });
        marker.on('click', () => inspectRespondent(r));
        marker.bindTooltip(`<strong>${r.id}: ${r.role_or_type}</strong> (${r.gender}, ${r.age_group})<br/>${r.location}<br/>Comfort: ${r.comfort_1_10 ? r.comfort_1_10 + '/10' : 'N/A'}`, { direction: 'top' });

        const respPopupContent = `
          <div style="font-family:var(--font-sans);min-width:200px;color:#1e293b;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
              <span style="font-weight:800;font-size:14px;color:#1e293b;">${r.id}</span>
              <span style="font-size:10px;padding:2px 6px;background:${isUpper?'#dbeafe':'#fef3c7'};color:${isUpper?'#1e40af':'#92400e'};border-radius:4px;font-weight:700;">${r.gender}, ${r.age_group}</span>
            </div>
            <div style="font-weight:700;font-size:12px;margin-bottom:2px;">${r.role_or_type}</div>
            <div style="font-size:11px;color:#64748b;margin-bottom:6px;">📍 ${r.location}</div>
            <div style="font-size:11px;margin-bottom:8px;">Comfort: <strong>${r.comfort_1_10 ? r.comfort_1_10 + '/10' : 'N/A'}</strong> • Mode: <strong>${r.mobility_mode}</strong></div>
            <button onclick="inspectRespondentById('${r.id}'); map.closePopup();" style="width:100%;background:#2563eb;color:#fff;border:none;border-radius:4px;padding:5px 8px;font-size:11px;cursor:pointer;font-weight:600;">View Profile & Audio Quote</button>
          </div>
        `;
        marker.bindPopup(respPopupContent);
        respMarkers.push(marker);
      });
      layers.respondents = L.featureGroup(respMarkers).addTo(map);

      // Layer 4: Places POI (110)
      const placeMarkers = [];
      PLACES.forEach(p => {
        const m = L.circleMarker([p.lat, p.lon], {
          radius: 4,
          fillColor: '#a855f7',
          color: '#ffffff',
          weight: 1,
          opacity: 0.8,
          fillOpacity: 0.8
        });
        m.bindTooltip(`<strong>${p.name}</strong> (${p.type})`);
        placeMarkers.push(m);
      });
      layers.places = L.featureGroup(placeMarkers);

      // Layer Selector Control
      const baseMaps = {
        "OpenStreetMap (Standard)": osmStandard,
        "Esri Light Canvas (Minimal)": esriCanvas,
        "Esri Satellite (Aerial)": esriSatellite
      };
      const overlayMaps = {
        "Respondents (24)": layers.respondents,
        "Field Media (105)": layers.media,
        "Pedestrian Network (680)": layers.network,
        "Dukuh Atas POIs (110)": layers.places
      };
      L.control.layers(baseMaps, overlayMaps, { position: 'topright' }).addTo(map);
    }

    // Layer Toggle Function
    function toggleMapLayer(layerName) {
      const btn = document.getElementById(`layer-${layerName}-toggle`);
      const group = layers[layerName];
      if (!group) return;

      if (map.hasLayer(group)) {
        map.removeLayer(group);
        btn.classList.remove('active');
      } else {
        map.addLayer(group);
        btn.classList.add('active');
      }
    }

    // Jump to Zone
    function jumpToZone(zoneKey) {
      const zoneCoords = {
        dukuh_atas: { center: [-6.2020, 106.8228], zoom: 16 },
        karet: { center: [-6.2055, 106.8224], zoom: 16 },
        semanggi: { center: [-6.2162, 106.8165], zoom: 16 },
        senayan: { center: [-6.2222, 106.8090], zoom: 16 },
        kebon_melati: { center: [-6.1985, 106.8180], zoom: 16 }
      };

      if (zoneCoords[zoneKey]) {
        map.flyTo(zoneCoords[zoneKey].center, zoneCoords[zoneKey].zoom, { duration: 1.2 });
      } else {
        map.flyTo([-6.2085, 106.8205], 14, { duration: 1.2 });
      }
    }

    function searchMapPins(query) {
      const q = query.toLowerCase().trim();
      if (!q) return;

      // Check respondent ID
      const r = RESPONDENTS.find(x => x.id.toLowerCase() === q || x.role_or_type.toLowerCase().includes(q));
      if (r) {
        locateRespondentOnMap(r.id);
        return;
      }

      // Check media filename
      const m = MEDIA_POINTS.find(x => x.filename.toLowerCase().includes(q) || x.category.toLowerCase().includes(q));
      if (m) {
        map.flyTo([m.lat, m.lon], 17, { duration: 1 });
        inspectMedia(m);
      }
    }

    function inspectRespondentById(id) {
      const r = RESPONDENTS.find(x => x.id === id);
      if (r) inspectRespondent(r);
    }

    function inspectMediaByIndex(idx) {
      const m = MEDIA_POINTS[idx];
      if (m) inspectMedia(m);
    }

    function openMediaLightboxByIndex(idx) {
      const m = MEDIA_POINTS[idx];
      if (m) openMediaLightbox(m.filename, m.type, m.thumb_url, m.datetime_wib, m.category, m.zone, m.description);
    }

    // Inspect Respondent in Sidebar
    function inspectRespondent(r) {
      const badge = document.getElementById('inspector-badge');
      badge.textContent = `Respondent ${r.id}`;
      badge.className = 'badge-pill cyan';

      const isUpper = r.class === 'upper_middle';
      const classColor = isUpper ? 'cyan' : 'amber';

      let scalesHtml = '';
      if (r.comfort_1_10 || r.security_1_10 || r.heat_1_10) {
        scalesHtml = `
          <div class="scale-meter-grid">
            <div class="scale-box">
              <div class="scale-title">Comfort</div>
              <div class="scale-num ${r.comfort_1_10 >= 7 ? 'good' : (r.comfort_1_10 <= 5 ? 'danger' : 'warning')}">${r.comfort_1_10 !== null ? r.comfort_1_10 + '/10' : '—'}</div>
            </div>
            <div class="scale-box">
              <div class="scale-title">Security</div>
              <div class="scale-num ${r.security_1_10 >= 7 ? 'good' : (r.security_1_10 <= 5 ? 'danger' : 'warning')}">${r.security_1_10 !== null ? r.security_1_10 + '/10' : '—'}</div>
            </div>
            <div class="scale-box">
              <div class="scale-title">Heat Discomfort</div>
              <div class="scale-num ${r.heat_1_10 >= 7 ? 'danger' : (r.heat_1_10 <= 5 ? 'good' : 'warning')}">${r.heat_1_10 !== null ? r.heat_1_10 + '/10' : '—'}</div>
            </div>
          </div>
          <div style="font-size:11px;color:var(--text-dim);margin-bottom:10px;">
            Scale Source: <strong>${r.scale_source}</strong> (Analyst coding from transcripts vs explicitly stated)
          </div>
        `;
      }

      const tagsHtml = (r.tags || []).map(t => `<span class="badge-pill">${t}</span>`).join('');

      document.getElementById('inspector-content').innerHTML = `
        <div class="detail-card">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px;">
            <h4 style="font-size:15px;color:#fff;font-weight:700;">${r.full_title}</h4>
            <span class="badge-pill ${classColor}">${r.id}</span>
          </div>
          <div style="font-size:12px;color:var(--text-muted);margin-bottom:10px;">
            📍 ${r.location}<br/>
            👤 Demographics: <strong>${r.gender}</strong>, <strong>${r.age_bracket}</strong><br/>
            ⏰ ${r.timestamp} • Mode: <strong>${r.mobility_mode}</strong>
          </div>
          <div class="detail-badge-row">${tagsHtml}</div>
          ${scalesHtml}
        </div>

        <div class="detail-card">
          <h5 style="font-size:12px;text-transform:uppercase;color:var(--accent-cyan);font-weight:700;margin-bottom:4px;">
            Verbatim Audio Excerpt / Field Notulen
          </h5>
          <div class="quote-box">"${r.quote}"</div>

          <h5 style="font-size:12px;text-transform:uppercase;color:var(--accent-amber);font-weight:700;margin-top:14px;margin-bottom:4px;">
            Analytical Insight & Policy Implication
          </h5>
          <div class="insight-box">${r.insight}</div>
        </div>
      `;
      lucide.createIcons();
    }

    // Inspect Media Point in Sidebar
    function inspectMedia(m) {
      const badge = document.getElementById('inspector-badge');
      badge.textContent = `Media: ${m.filename}`;
      badge.className = 'badge-pill ' + (m.type === 'video' ? 'cyan' : 'rose');

      const resolvedThumb = resolveAssetUrl(m.thumb_url);

      let previewHtml = '';
      if (resolvedThumb) {
        previewHtml = `
          <div style="width:100%;border-radius:8px;overflow:hidden;background:#000;margin-bottom:12px;cursor:pointer;" onclick="openMediaLightbox('${m.filename}', '${m.type}', '${m.thumb_url}', '${m.datetime_wib}', '${m.category}', '${m.zone}', '${m.description.replace(/'/g, "\\\\'")}')">
            <img src="${resolvedThumb}" style="width:100%;height:auto;display:block;max-height:240px;object-fit:cover;" alt="${m.filename}"/>
          </div>
        `;
      } else {
        previewHtml = `
          <div style="padding:24px;background:#0f172a;border-radius:8px;text-align:center;margin-bottom:12px;color:var(--text-dim);">
            <i data-lucide="file-video" style="width:32px;height:32px;margin-bottom:6px;display:inline-block;"></i>
            <p style="font-size:12px;">Logged in Media Log (${m.filename})</p>
          </div>
        `;
      }

      document.getElementById('inspector-content').innerHTML = `
        <div class="detail-card">
          ${previewHtml}
          <h4 style="font-size:14px;color:#fff;font-weight:700;margin-bottom:4px;">${m.filename}</h4>
          <div style="font-size:12px;color:var(--text-muted);margin-bottom:10px;">
            Type: <strong>${m.type.toUpperCase()}</strong> ${m.duration_s ? '(' + Math.round(m.duration_s) + 's duration)' : ''}<br/>
            Captured: ${m.datetime_wib}<br/>
            GPS: ${m.lat.toFixed(5)}, ${m.lon.toFixed(5)}
          </div>
          <div class="detail-badge-row">
            <span class="badge-pill cyan">${m.zone}</span>
            <span class="badge-pill amber">${m.category}</span>
          </div>
        </div>

        <div class="detail-card">
          <h5 style="font-size:12px;text-transform:uppercase;color:var(--accent-cyan);font-weight:700;margin-bottom:6px;">
            Corridor Context & Observation
          </h5>
          <p style="font-size:12px;color:#cbd5e1;line-height:1.5;">
            ${m.description}
          </p>
          <div style="display:flex;gap:8px;margin-top:12px;">
            <button class="filter-btn" style="flex:1;justify-content:center;" onclick="map.flyTo([${m.lat}, ${m.lon}], 17)">
              <i data-lucide="crosshair" style="width:13px;height:13px;"></i> Re-Center Map
            </button>
            <button class="filter-btn" style="flex:1;justify-content:center;" onclick="openMediaLightbox('${m.filename}', '${m.type}', '${m.thumb_url||''}', '${m.datetime_wib}', '${m.category}', '${m.zone}', '${m.description.replace(/'/g, "\\\\'")}')">
              <i data-lucide="maximize-2" style="width:13px;height:13px;"></i> Open Modal
            </button>
          </div>
        </div>
      `;
      lucide.createIcons();
    }

    // Inspect Network Edge
    function inspectNetworkEdge(p) {
      const badge = document.getElementById('inspector-badge');
      badge.textContent = `Edge: ${p.id || 'Segment'}`;
      badge.className = 'badge-pill emerald';

      document.getElementById('inspector-content').innerHTML = `
        <div class="detail-card">
          <h4 style="font-size:15px;color:#fff;font-weight:700;margin-bottom:4px;">${p.street_name || 'Pedestrian Link'}</h4>
          <div style="font-size:12px;color:var(--text-muted);margin-bottom:10px;">
            Classification: <strong>${(p.kind || 'unknown').toUpperCase()}</strong><br/>
            Length: <strong>${Math.round(p.length_m || 0)} meters</strong><br/>
            Surface: <strong>${p.surface || 'standard paving'}</strong>
          </div>
          <div class="detail-badge-row">
            <span class="badge-pill emerald">Sidewalk: ${p.has_sidewalk || 'yes'}</span>
            <span class="badge-pill">Confidence: ${p.confidence || 'high'}</span>
          </div>
        </div>

        <div class="detail-card">
          <h5 style="font-size:12px;text-transform:uppercase;color:var(--accent-cyan);font-weight:700;margin-bottom:6px;">
            OpenSidewalks Ingestion Status
          </h5>
          <p style="font-size:12px;color:#cbd5e1;line-height:1.5;">
            Merged from OpenStreetMap and field audit layers. Represents traversable pedestrian routing geometry for pedestrian accessibility modeling.
          </p>
        </div>
      `;
      lucide.createIcons();
    }

    // Render Table in Respondents Tab
    function renderRespondentsTable(filtered = RESPONDENTS) {
      const tbody = document.getElementById('resp-table-body');
      tbody.innerHTML = filtered.map(r => {
        const comfBadge = r.comfort_1_10 !== null 
          ? `<span style="font-weight:700;color:${r.comfort_1_10>=7?'#10b981':'#f59e0b'}">${r.comfort_1_10}/10</span>` 
          : '<span style="color:var(--text-dim)">—</span>';
        const secBadge = r.security_1_10 !== null 
          ? `<span style="font-weight:700;color:${r.security_1_10>=7?'#10b981':'#f59e0b'}">${r.security_1_10}/10</span>` 
          : '<span style="color:var(--text-dim)">—</span>';
        const heatBadge = r.heat_1_10 !== null 
          ? `<span style="font-weight:700;color:${r.heat_1_10>=7?'#ef4444':'#10b981'}">${r.heat_1_10}/10</span>` 
          : '<span style="color:var(--text-dim)">—</span>';
        const genderBadge = r.gender === 'Female'
          ? `<span class="badge-pill rose" style="font-size:10px;">F</span>`
          : `<span class="badge-pill cyan" style="font-size:10px;">M</span>`;

        return `
          <tr>
            <td><strong>${r.id}</strong></td>
            <td><strong>${r.role_or_type}</strong></td>
            <td>${genderBadge}</td>
            <td style="font-size:11px;color:var(--text-muted);">${r.age_bracket}</td>
            <td style="font-size:12px;">${r.location}</td>
            <td><span class="badge-pill ${r.class==='upper_middle'?'cyan':'amber'}" style="font-size:10px;">${r.class}</span></td>
            <td style="font-size:12px;">${r.mobility_mode}</td>
            <td>${comfBadge}</td>
            <td>${secBadge}</td>
            <td>${heatBadge}</td>
            <td style="font-size:11px;color:var(--text-muted);">${r.scale_source}</td>
            <td style="font-size:12px;max-width:260px;">${r.key_painpoint || r.notes || '—'}</td>
            <td>
              <button class="filter-btn" style="padding:3px 8px;font-size:11px;" onclick="locateRespondentOnMap('${r.id}')">
                <i data-lucide="map-pin" style="width:11px;height:11px;"></i> Map
              </button>
            </td>
          </tr>
        `;
      }).join('');
      lucide.createIcons();
    }

    // Filter Respondents Table
    function filterRespondentsTable(query) {
      const q = query.toLowerCase();
      const filtered = RESPONDENTS.filter(r => 
        r.id.toLowerCase().includes(q) ||
        r.role_or_type.toLowerCase().includes(q) ||
        r.location.toLowerCase().includes(q) ||
        r.gender.toLowerCase().includes(q) ||
        r.age_bracket.toLowerCase().includes(q) ||
        (r.key_painpoint && r.key_painpoint.toLowerCase().includes(q)) ||
        (r.notes && r.notes.toLowerCase().includes(q))
      );
      renderRespondentsTable(filtered);
    }

    // Locate Respondent on Map from Table / Card
    function locateRespondentOnMap(rid) {
      const r = RESPONDENTS.find(x => x.id === rid);
      if (!r) return;

      switchTab('geo-studio');
      setTimeout(() => {
        map.invalidateSize();
        map.flyTo([r.lat, r.lon], 17, { duration: 1 });
        inspectRespondent(r);
      }, 100);
    }

    // Render Audio Excerpt Cards
    function renderRespondentCards() {
      const grid = document.getElementById('resp-cards-grid');
      grid.innerHTML = RESPONDENTS.slice(0, 12).map(r => `
        <div class="card" style="display:flex;flex-direction:column;justify-content:space-between;">
          <div>
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
              <h4 style="font-size:14px;font-weight:700;color:#fff;">${r.full_title}</h4>
              <span class="badge-pill cyan">${r.id}</span>
            </div>
            <div style="font-size:11px;color:var(--text-muted);margin-bottom:10px;">
              📍 ${r.location} • 👤 ${r.gender}, ${r.age_bracket} • ⏰ ${r.timestamp}
            </div>
            <div class="quote-box" style="font-size:12px;">"${r.quote}"</div>
            <div style="font-size:12px;color:#cbd5e1;line-height:1.4;margin-top:8px;">
              <strong>Finding:</strong> ${r.insight}
            </div>
          </div>
          <div style="margin-top:14px;display:flex;justify-content:space-between;align-items:center;">
            <div style="font-size:11px;color:var(--text-dim);">Mode: ${r.mobility_mode}</div>
            <button class="filter-btn" style="padding:4px 10px;font-size:11px;" onclick="locateRespondentOnMap('${r.id}')">
              <i data-lucide="map" style="width:12px;height:12px;"></i> View Location
            </button>
          </div>
        </div>
      `).join('');
      lucide.createIcons();
    }

    // Filter and Render Media Gallery
    function filterGallery(filterType, btnElem) {
      if (btnElem) {
        btnElem.parentElement.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        btnElem.classList.add('active');
      }

      let items = MEDIA_POINTS;
      if (filterType === 'photo') items = MEDIA_POINTS.filter(m => m.type === 'photo');
      else if (filterType === 'video') items = MEDIA_POINTS.filter(m => m.type === 'video');
      else if (filterType === 'has_thumb') items = MEDIA_POINTS.filter(m => m.has_thumb);
      else if (filterType === 'danger') items = MEDIA_POINTS.filter(m => m.severity === 'danger');
      else if (filterType === 'warning') items = MEDIA_POINTS.filter(m => m.severity === 'warning');

      renderGalleryItems(items);
    }
    window.filterGallery = filterGallery;

    function renderGalleryItems(items) {
      const container = document.getElementById('gallery-container');
      container.innerHTML = items.map((m, idx) => {
        const isPhoto = m.type === 'photo';
        const resolvedThumb = resolveAssetUrl(m.thumb_url);

        const imgHtml = resolvedThumb
          ? `<img src="${resolvedThumb}" alt="${m.filename}" loading="lazy" onerror="if(!this.dataset.retried){this.dataset.retried=1;this.src='../../'+this.getAttribute('data-rel');}" data-rel="${m.thumb_url}"/>`
          : `<div style="color:var(--text-dim);font-size:11px;text-align:center;"><i data-lucide="file-video" style="display:inline-block;width:28px;height:28px;margin-bottom:4px;"></i><br/>${m.filename}</div>`;

        return `
          <div class="media-thumb-card" onclick="openMediaLightbox('${m.filename}', '${m.type}', '${m.thumb_url||''}', '${m.datetime_wib}', '${m.category}', '${m.zone}', '${m.description.replace(/'/g, "\\\\'")}')">
            <div class="media-thumb-img-wrap">
              ${imgHtml}
              <span class="media-type-tag ${isPhoto?'photo':'video'}">${m.type}</span>
              ${m.duration_s ? `<span class="media-duration-tag">${Math.round(m.duration_s)}s</span>` : ''}
            </div>
            <div class="media-info">
              <div>
                <div class="media-title" title="${m.filename}">${m.filename}</div>
                <div class="media-meta">${m.category}</div>
              </div>
              <div style="font-size:10px;color:var(--text-dim);margin-top:6px;display:flex;justify-content:space-between;">
                <span>${m.zone.split('&')[0]}</span>
                <span>${m.datetime_wib.split('T')[1].substring(0,5)}</span>
              </div>
            </div>
          </div>
        `;
      }).join('');
      lucide.createIcons();
    }

    // Media Modal / Lightbox with Real Video Playback Support
    function openMediaLightbox(filename, type, thumbUrl, time, category, zone, desc) {
      const modal = document.getElementById('media-modal');
      const title = document.getElementById('modal-title');
      const body = document.getElementById('modal-body-content');

      const isSub = window.location.pathname.includes('/investigate/field');
      const docBase = isSub ? '../../Documentations' : './Documentations';
      const rawAssetUrl = `${docBase}/${filename}`;
      const resolvedThumbUrl = thumbUrl ? (isSub ? '../../' + thumbUrl.replace(/^\\.\\//, '') : thumbUrl) : null;

      title.textContent = `${filename} • ${type.toUpperCase()}`;

      let mediaElem = '';
      if (type === 'video') {
        mediaElem = `
          <div style="text-align:center;background:#000;border-radius:8px;padding:12px;margin-bottom:16px;">
            <video controls autoplay playsinline preload="metadata" style="max-height:55vh;width:100%;border-radius:6px;outline:none;" poster="${resolvedThumbUrl || ''}">
              <source src="${rawAssetUrl}" type="video/quicktime">
              <source src="${rawAssetUrl}" type="video/mp4">
              ${resolvedThumbUrl ? `<img src="${resolvedThumbUrl}" style="max-height:50vh;max-width:100%;border-radius:4px;" alt="${filename}"/>` : ''}
            </video>
            <p style="color:#94a3b8;font-size:11px;margin-top:6px;">
              Direct playback of raw Field Day 1 QuickTime clip. If playback is unsupported by your browser engine, click 'Open Raw Asset' below.
            </p>
          </div>
        `;
      } else if (resolvedThumbUrl) {
        mediaElem = `
          <div style="text-align:center;background:#000;border-radius:8px;padding:12px;margin-bottom:16px;">
            <img src="${resolvedThumbUrl}" style="max-height:55vh;max-width:100%;height:auto;border-radius:4px;" alt="${filename}"/>
          </div>
        `;
      } else {
        mediaElem = `
          <div style="padding:40px;background:#0f172a;text-align:center;border-radius:8px;margin-bottom:16px;">
            <i data-lucide="file-video" style="width:40px;height:40px;color:var(--text-dim);margin-bottom:8px;display:inline-block;"></i>
            <p style="color:var(--text-muted);font-size:13px;">Raw asset catalogued in <code>Documentations/${filename}</code></p>
          </div>
        `;
      }

      body.innerHTML = `
        ${mediaElem}
        <div class="detail-card">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px;flex-wrap:wrap;gap:8px;">
            <div>
              <h4 style="font-size:15px;color:#fff;margin-bottom:4px;font-weight:700;">${category || 'Field Observation'}</h4>
              <div style="font-size:12px;color:var(--text-muted);">📍 ${zone || 'Sudirman Corridor'} • ⏰ ${time || 'Field Day 1'} WIB</div>
            </div>
            <div style="display:flex;gap:6px;">
              <a href="${rawAssetUrl}" target="_blank" download class="filter-btn" style="text-decoration:none;font-size:11px;padding:5px 10px;">
                <i data-lucide="external-link" style="width:12px;height:12px;"></i> Open Raw Asset
              </a>
            </div>
          </div>
          <p style="font-size:12px;color:#cbd5e1;line-height:1.5;margin-top:8px;">
            ${desc || 'Captured along the walking transect during Field Day 1.'}
          </p>
        </div>
      `;

      modal.classList.add('open');
      lucide.createIcons();
    }

    function closeMediaModal(e) {
      const modal = document.getElementById('media-modal');
      const videos = modal.querySelectorAll('video');
      videos.forEach(v => { v.pause(); });
      modal.classList.remove('open');
    }

    // Render Weather Table in Microclimate Tab
    function renderWeatherTable() {
      const tbody = document.getElementById('weather-table-body');
      tbody.innerHTML = WEATHER.map(w => `
        <tr>
          <td><strong>${w.timestamp ? w.timestamp.split('T')[1] : '—'} WIB</strong></td>
          <td>${w.location_label}</td>
          <td><span style="font-weight:700;color:#f43f5e;">${w.temp_c}°C</span></td>
          <td><span style="font-weight:800;color:#f43f5e;">${w.feels_like_c}°C</span></td>
          <td>${w.humidity_pct}%</td>
          <td><span class="badge-pill amber" style="font-size:10px;">UV ${w.uv_index} (${w.uv_label})</span></td>
          <td style="font-size:12px;color:var(--text-muted);">${w.notes || w.condition}</td>
        </tr>
      `).join('');
    }

    // Initialize Microclimate Charts (Chart.js)
    function initMicroclimateCharts() {
      const labels = WEATHER.map(w => w.timestamp.split('T')[1] + ' WIB');
      const temps = WEATHER.map(w => w.temp_c);
      const feels = WEATHER.map(w => w.feels_like_c);
      const humidity = WEATHER.map(w => w.humidity_pct);
      const uvs = WEATHER.map(w => w.uv_index);
      const winds = WEATHER.map(w => w.wind_kmh);
      const gusts = WEATHER.map(w => w.gust_kmh);

      // Chart 1: Temperature vs Feels Like
      const tempChart = new Chart(document.getElementById('chart-weather-temp'), {
        type: 'line',
        data: {
          labels: labels,
          datasets: [
            {
              label: 'Feels-Like Temp (°C)',
              data: feels,
              borderColor: '#f43f5e',
              backgroundColor: 'rgba(244, 63, 94, 0.15)',
              borderWidth: 3,
              fill: true,
              tension: 0.3
            },
            {
              label: 'Ambient Air Temp (°C)',
              data: temps,
              borderColor: '#f59e0b',
              borderWidth: 2,
              borderDash: [4, 4],
              tension: 0.3
            },
            {
              label: 'Comfort Threshold (THI 27°C)',
              data: labels.map(() => 27),
              borderColor: '#10b981',
              borderWidth: 1.5,
              borderDash: [6, 6],
              pointRadius: 0
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { labels: { color: '#94a3b8', font: { size: 11 } } }
          },
          scales: {
            y: { min: 25, max: 38, grid: { color: '#1e293b' }, ticks: { color: '#94a3b8' } },
            x: { grid: { color: '#1e293b' }, ticks: { color: '#94a3b8' } }
          }
        }
      });

      // Chart 2: UV Index & Humidity
      const uvChart = new Chart(document.getElementById('chart-weather-uv'), {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [
            {
              type: 'line',
              label: 'UV Radiation Index',
              data: uvs,
              borderColor: '#f59e0b',
              backgroundColor: '#f59e0b',
              yAxisID: 'yUV',
              borderWidth: 3,
              tension: 0.2
            },
            {
              type: 'bar',
              label: 'Relative Humidity (%)',
              data: humidity,
              backgroundColor: 'rgba(6, 182, 212, 0.35)',
              borderColor: '#06b6d4',
              borderWidth: 1,
              yAxisID: 'yHum',
              borderRadius: 4
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { labels: { color: '#94a3b8', font: { size: 11 } } }
          },
          scales: {
            yUV: { type: 'linear', position: 'left', min: 0, max: 11, grid: { color: '#1e293b' }, ticks: { color: '#f59e0b' } },
            yHum: { type: 'linear', position: 'right', min: 40, max: 80, grid: { display: false }, ticks: { color: '#06b6d4' } },
            x: { grid: { color: '#1e293b' }, ticks: { color: '#94a3b8' } }
          }
        }
      });

      // Chart 3: Wind & Gusts
      const windChart = new Chart(document.getElementById('chart-weather-wind'), {
        type: 'line',
        data: {
          labels: labels,
          datasets: [
            {
              label: 'Wind Gusts (km/h)',
              data: gusts,
              borderColor: '#38bdf8',
              backgroundColor: 'rgba(56, 189, 248, 0.1)',
              fill: true,
              tension: 0.3
            },
            {
              label: 'Sustained Wind (km/h)',
              data: winds,
              borderColor: '#06b6d4',
              borderWidth: 2,
              tension: 0.3
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { labels: { color: '#94a3b8', font: { size: 11 } } }
          },
          scales: {
            y: { min: 0, max: 30, grid: { color: '#1e293b' }, ticks: { color: '#94a3b8' } },
            x: { grid: { color: '#1e293b' }, ticks: { color: '#94a3b8' } }
          }
        }
      });

      window.microclimateChartsList = [tempChart, uvChart, windChart];
    }

    // Initialize Respondent Charts (Demographics, Modes, Comfort)
    function initRespondentCharts() {
      // 1. Gender breakdown
      const maleCount = RESPONDENTS.filter(r => r.gender === 'Male').length;
      const femaleCount = RESPONDENTS.filter(r => r.gender === 'Female').length;

      const genderChart = new Chart(document.getElementById('chart-gender-dist'), {
        type: 'doughnut',
        data: {
          labels: [`Male (${maleCount})`, `Female (${femaleCount})`],
          datasets: [{
            data: [maleCount, femaleCount],
            backgroundColor: ['#3b82f6', '#f43f5e'],
            borderWidth: 0
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { position: 'bottom', labels: { color: '#94a3b8', font: { size: 11 } } } }
        }
      });

      // 2. Age group profiles
      const ageCohorts = {
        'Teen (15-18)': RESPONDENTS.filter(r => r.age_group === 'Teenager').length,
        'Young (19-29)': RESPONDENTS.filter(r => r.age_group === 'Young Adult').length,
        'Adult (30-49)': RESPONDENTS.filter(r => r.age_group === 'Adult').length,
        'Mid (50-59)': RESPONDENTS.filter(r => r.age_group === 'Middle-Aged').length,
        'Senior (60+)': RESPONDENTS.filter(r => r.age_group === 'Elderly').length
      };

      const ageChart = new Chart(document.getElementById('chart-age-dist'), {
        type: 'bar',
        data: {
          labels: Object.keys(ageCohorts),
          datasets: [{
            label: 'Respondents',
            data: Object.values(ageCohorts),
            backgroundColor: '#a855f7',
            borderRadius: 4
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { display: false } },
          scales: {
            y: { grid: { color: '#1e293b' }, ticks: { color: '#94a3b8', stepSize: 2 } },
            x: { grid: { display: false }, ticks: { color: '#94a3b8', font: { size: 10 } } }
          }
        }
      });

      // 3. Social class breakdown
      const upperCount = RESPONDENTS.filter(r => r.class === 'upper_middle').length;
      const bottomCount = RESPONDENTS.filter(r => r.class === 'bottom').length;
      const unclassCount = RESPONDENTS.length - upperCount - bottomCount;

      const classChart = new Chart(document.getElementById('chart-class-dist'), {
        type: 'doughnut',
        data: {
          labels: [`Upper/Middle (${upperCount})`, `Bottom/Workers (${bottomCount})`, `Residents (${unclassCount})`],
          datasets: [{
            data: [upperCount, bottomCount, unclassCount],
            backgroundColor: ['#06b6d4', '#f59e0b', '#64748b'],
            borderWidth: 0
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { position: 'bottom', labels: { color: '#94a3b8', font: { size: 10 } } } }
        }
      });

      // 4. Mobility modes breakdown
      const modeCounts = {};
      RESPONDENTS.forEach(r => {
        const m = r.mobility_mode || 'walk';
        modeCounts[m] = (modeCounts[m] || 0) + 1;
      });

      const modesChart = new Chart(document.getElementById('chart-modes-dist'), {
        type: 'bar',
        data: {
          labels: Object.keys(modeCounts),
          datasets: [{
            label: 'Respondents',
            data: Object.values(modeCounts),
            backgroundColor: '#10b981',
            borderRadius: 4
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { display: false } },
          scales: {
            y: { grid: { color: '#1e293b' }, ticks: { color: '#94a3b8' } },
            x: { grid: { display: false }, ticks: { color: '#94a3b8', font: { size: 10 } } }
          }
        }
      });

      // 5. Stated vs Interpreted comfort ratings
      const statedComfort = RESPONDENTS.filter(r => r.scale_source === 'stated' && r.comfort_1_10 !== null).map(r => r.comfort_1_10);
      const interpretedComfort = RESPONDENTS.filter(r => r.scale_source === 'interpreted' && r.comfort_1_10 !== null).map(r => r.comfort_1_10);
      
      const avgStated = (statedComfort.reduce((a,b)=>a+b,0) / statedComfort.length).toFixed(1);
      const avgInterpreted = (interpretedComfort.reduce((a,b)=>a+b,0) / interpretedComfort.length).toFixed(1);

      const comfortChart = new Chart(document.getElementById('chart-comfort-dist'), {
        type: 'bar',
        data: {
          labels: ['Stated Comfort (Notulen 7/10)', 'Interpreted Comfort (Audio 4-9/10)'],
          datasets: [{
            label: 'Average Score (1-10)',
            data: [avgStated, avgInterpreted],
            backgroundColor: ['#f59e0b', '#06b6d4'],
            borderRadius: 6
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: { min: 0, max: 10, grid: { color: '#1e293b' }, ticks: { color: '#94a3b8' } },
            x: { grid: { display: false }, ticks: { color: '#94a3b8' } }
          }
        }
      });

      window.respondentChartsList = [genderChart, ageChart, classChart, modesChart, comfortChart];
    }

    // Initialize Urban Gradient Charts
    function initGradientCharts() {
      const topStreets = GRADIENT.filter(g => g.total_len_m > 200).slice(0, 10);
      const gradientChart = new Chart(document.getElementById('chart-gradient-streets'), {
        type: 'bar',
        data: {
          labels: topStreets.map(s => s.street_name.replace('Jalan ', '')),
          datasets: [
            {
              label: 'Sidewalk Length (m)',
              data: topStreets.map(s => s.sidewalk_len_m),
              backgroundColor: '#06b6d4',
              borderRadius: 4
            },
            {
              label: 'Total Street Length (m)',
              data: topStreets.map(s => s.total_len_m),
              backgroundColor: 'rgba(255, 255, 255, 0.1)',
              borderRadius: 4
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          indexAxis: 'y',
          plugins: { legend: { labels: { color: '#94a3b8' } } },
          scales: {
            x: { grid: { color: '#1e293b' }, ticks: { color: '#94a3b8' } },
            y: { grid: { display: false }, ticks: { color: '#94a3b8', font: { size: 11 } } }
          }
        }
      });

      window.gradientChartsList = [gradientChart];
    }
  </script>
</body>
</html>
"""

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Generated standalone dashboard at: {output_path} ({os.path.getsize(output_path) / 1024:.1f} KB)")

# Also create copy in investigate/field/ for convenient co-location
field_path = f'{base}/investigate/field/empirical_field_data_dashboard.html'
with open(field_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Copied companion dashboard to: {field_path}")
