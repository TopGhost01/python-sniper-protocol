# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# nexus_phase1_rep2_scan_threats.py
# NEXUS Systems — Phase 1
# For loop scanning threat dossiers with capitalize() and concatenated print output
# Rep 2 proved that concatenation controls display spacing precisely where comma separation cannot.

def scan_threats(missions):
    for mission in missions:
        print(mission["name"], "| Status:", mission["status"]. capitalize())
missions = [{"name": "Iron Sentinel","status":"active"},
            {"name": "Phantom Strike","status":"pending"},
            {"name": "Ghost Recon","status":"inactive"}]
scan_threats(missions)
