# mock_data.py

# --- Mock Bus Stops (10) ---
BUS_STOPS = [
    {"id": "BS1", "name": "Central Station", "lat": 40.7128, "lon": -74.0060},
    {"id": "BS2", "name": "5th Avenue", "lat": 40.7142, "lon": -74.0039},
    {"id": "BS3", "name": "Broadway & 7th", "lat": 40.7158, "lon": -74.0015},
    {"id": "BS4", "name": "Union Square", "lat": 40.7359, "lon": -73.9911},
    {"id": "BS5", "name": "City Park", "lat": 40.7306, "lon": -73.9866},
    {"id": "BS6", "name": "East Village", "lat": 40.7265, "lon": -73.9815},
    {"id": "BS7", "name": "Grand Street", "lat": 40.7181, "lon": -73.9959},
    {"id": "BS8", "name": "Harbor Point", "lat": 40.7001, "lon": -74.0120},
    {"id": "BS9", "name": "South Ferry", "lat": 40.7031, "lon": -74.0170},
    {"id": "BS10", "name": "West End", "lat": 40.7489, "lon": -73.9873},
]

# --- Mock Bus Routes (10) ---
BUS_ROUTES = [
    {"id": "B1", "name": "Downtown Loop", "stops": ["BS1","BS2","BS3","BS4"], "frequency_min": 10},
    {"id": "B2", "name": "Uptown Express", "stops": ["BS4","BS5","BS6","BS7"], "frequency_min": 15},
    {"id": "B3", "name": "Crosstown", "stops": ["BS2","BS5","BS8"], "frequency_min": 12},
    {"id": "B4", "name": "Waterfront Line", "stops": ["BS8","BS9","BS1"], "frequency_min": 20},
    {"id": "B5", "name": "Heritage Loop", "stops": ["BS7","BS6","BS5","BS4","BS3"], "frequency_min": 8},
    {"id": "B6", "name": "Park Connector", "stops": ["BS5","BS1","BS9"], "frequency_min": 18},
    {"id": "B7", "name": "West Shuttle", "stops": ["BS10","BS4","BS2"], "frequency_min": 14},
    {"id": "B8", "name": "East Shuttle", "stops": ["BS6","BS5","BS2"], "frequency_min": 16},
    {"id": "B9", "name": "Night Owl", "stops": ["BS1","BS3","BS7","BS10"], "frequency_min": 30},
    {"id": "B10","name": "Tourist Circle", "stops": ["BS9","BS8","BS7","BS6","BS5"], "frequency_min": 25},
]

# --- Mock Transit Stops (10) ---
TRANSIT_STOPS = [
    {"id": "TS1", "name": "Main Metro Station", "lat": 40.7306, "lon": -73.9352},
    {"id": "TS2", "name": "North Metro", "lat": 40.7406, "lon": -73.9452},
    {"id": "TS3", "name": "South Metro", "lat": 40.7206, "lon": -73.9252},
    {"id": "TS4", "name": "East Junction", "lat": 40.7506, "lon": -73.9552},
    {"id": "TS5", "name": "West Junction", "lat": 40.7106, "lon": -73.9152},
    {"id": "TS6", "name": "River Park", "lat": 40.7350, "lon": -73.9600},
    {"id": "TS7", "name": "Industrial Hub", "lat": 40.7250, "lon": -73.9700},
    {"id": "TS8", "name": "Airport Terminal", "lat": 40.7500, "lon": -73.9000},
    {"id": "TS9", "name": "University Station", "lat": 40.7450, "lon": -73.9400},
    {"id": "TS10","name": "Central Market", "lat": 40.7320, "lon": -73.9500},
]

# --- Mock Transit Routes (10) ---
TRANSIT_ROUTES = [
    {"id": "T1", "name": "Metro Line A", "stops": ["TS1","TS2","TS4"], "frequency_min": 8},
    {"id": "T2", "name": "Metro Line B", "stops": ["TS3","TS1","TS5"], "frequency_min": 10},
    {"id": "T3", "name": "Metro Line C", "stops": ["TS6","TS7","TS8"], "frequency_min": 12},
    {"id": "T4", "name": "Metro Line D", "stops": ["TS1","TS9","TS10"], "frequency_min": 9},
    {"id": "T5", "name": "Tram Line 1", "stops": ["TS2","TS4","TS6","TS8"], "frequency_min": 7},
    {"id": "T6", "name": "Tram Line 2", "stops": ["TS5","TS7","TS9"], "frequency_min": 11},
    {"id": "T7", "name": "Light Rail A", "stops": ["TS3","TS10","TS1"], "frequency_min": 6},
    {"id": "T8", "name": "Light Rail B", "stops": ["TS2","TS5","TS8"], "frequency_min": 13},
    {"id": "T9", "name": "Airport Express", "stops": ["TS8","TS1"], "frequency_min": 5},
    {"id": "T10","name": "University Connector", "stops": ["TS9","TS10"], "frequency_min": 15},
]
