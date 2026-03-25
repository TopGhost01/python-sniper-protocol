# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# nexus_phase1_rep2_filter_active.py
# NEXUS Systems — Phase 1
# For loop with if statement filtering active drones from vault using append and return
# Rep 2 proved the append and return architecture separates confirmed matches from the vault and delivers the filtered collection to command.

def filter_active(missions):
    active_missions = []
    for mission in missions:
        if mission["status"] == "active":
            print(mission["name"] + " | Status: " + mission["status"].capitalize())
            active_missions.append(mission)
    return active_missions
missions = [{"name": "Alpha Drone", "status": "active"},
            {"name": "Viper Drone", "status": "standby"},
            {"name": "Phantom Drone", "status": "returning"},
            {"name": "Sentinel Drone", "status": "offline"},
            {"name": "Orbit Drone", "status": "active"}]
filter_active(missions)
