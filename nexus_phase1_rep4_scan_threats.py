# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# nexus_phase1_rep4_scan_threats.py
# NEXUS Systems — Phase 1
# For loop scanning four threat dossiers with capitalize() and concatenated print output
# Rep 4 proved the vault scales seamlessly and concatenation maintains clean output regardless of dossier volume.

def scan_threats(missions):
    for mission in missions:
        print(mission["name"] + " | Status: " + mission["status"].capitalize())
missions = [{"name": "Ghost Recon", "status": "inactive"},
            {"name": "Phantom Strike", "status": "pending"},
            {"name": "Iron Sentinel", "status": "active"},
            {"name": "Planetary Rebirth", "status": "classified"}]
scan_threats(missions)
            
