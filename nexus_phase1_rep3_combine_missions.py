# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# nexus_phase1_rep3_combine_missions.py
# NEXUS Systems — Phase 1
# Scans the dossier vault filtering by operational status and mission codename simultaneously
# Rep 3 — proved keyword is required on the left of in or the terminal rejects the order entirely

def combine_missions(missions,status,keyword):
    result = ""
    i = 0
    

    while i  < len(missions):
        if  in missions[i]["name"] and missions[i]["status"] == status:
            result += "Missions: " + missions[i]["name"] + " | Status: " + missions[i]["status"] + "\n"

        i += 1

    return result

print(combine_missions([{"name": "Ghost Protocol", "status": "Active"}],"Active","Ghost"))   
