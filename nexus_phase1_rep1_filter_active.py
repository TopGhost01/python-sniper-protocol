# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# nexus_phase1_rep1_filter_active.py
# NEXUS Systems — Phase 1
# For loop with if statement filtering active missions from vault
# Rep 1 identified three production issues. Missing return value. Function name partially mismatched. Data typo in vault. All three corrected in Rep 2 forward.

def filter_active(missions):
    for mission in missions:
        if mission["status"] == "active": 
            print(mission["name"] + " | Status: " + mission["status"].capitalize())
        

missions = [{"name": "Patient A", "status": "stabe"},
            {"name": "Patient B", "status": "critical"},
            {"name": "Patient C", "status": "active"},
            {"name": "Patient D", "status": "discharged"},
            {"name": "Patient E", "status": "active"}]  
filter_active(missions)      
