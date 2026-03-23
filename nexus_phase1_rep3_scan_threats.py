# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# nexus_phase1_rep3_scan_threats.py
# NEXUS Systems — Phase 1
# For loop scanning threat dossiers with capitalize() and concatenated print output
# Rep 3 proved concatenation controls every character in the output string with surgical precision.

def scan_threats(missions):
    for mission in missions:
        print(mission["name"] + " | Status: " + mission["status"].capitalize())
missions = [{"name": "Phantom Strike", "status": "pending"},
            {"name": "Iron Sentinel", "status": "inactive"},
            {"name": "Ghost Recon", "status": "active"}]   

scan_threats(missions)    
