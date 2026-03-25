# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# nexus_phase1_rep3_filter_active.py
# NEXUS Systems — Phase 1
# For loop with if statement filtering active cyber threats using append and return
# Rep 3 proved the return value must be caught by the pipeline or the filtered collection disappears silently.

def filter_active(missions):
    active_missions = []
    for mission in missions:
        if mission["status"] == "active":
            print(mission["name"] + " | Status: " + mission["status"].capitalize())
            active_missions.append(mission)
    return active_missions
missions = [{"name": "Agent Cipher", "status": "active"},
            {"name": "Agent Phantom", "status": "dormant"},
            {"name": "Agent Sentinel", "status": "neutralized"},
            {"name": "Agent Viper", "status": "active"},
            {"name": "Agent Recon", "status": "unconfirmed"}]      
filter_active(missions)  
