# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it. No system contains it.
# No technology extinguishes it.


# Healthcare sector. Sweep with if gate.
# append on confirmed match. return outside sweep.
# Concatenation locked. Dot notation clean.


def filter_active(missions):
    active_missions = []
    for mission in missions:
        if mission["status"] == "active":
            print(mission["name"] + " | Status: " + mission["status"].capitalize())
            active_missions.append(mission)
    return active_missions       
missions = [{"name": "cardiac_unit_7", "status": "active"},
            {"name": "trauma_bay_3", "status": "inactive"},
            {"name": "icu_protocol_alpha", "status": "pending"},
            {"name": "triage_sentinel_2", "status": "active"}] 
filter_active(missions)
