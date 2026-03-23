# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# nexus_phase1_rep1_scan_threats.py
# NEXUS Systems — Phase 1
# For loop scanning threat dossiers with capitalize() display standardization
# Rep 1 proved the for loop scans every dossier automatically and capitalize() standardizes display output regardless of storage format.

def scan_threats(missions):
    for mission in missions:
        print(mission["name"], "| Status:", mission["status"]. capitalize())
missions = [{"name": "Iron Sentinel", "status": "active"},
            {"name": "Phantom Strike", "status": "pending"},
            {"name": "Ghost Recon", "status": "inactive"}]   
scan_threats(missions)     
