# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# nexus_phase1_rep2_combine_missions.py
# NEXUS Systems — Phase 1
# Scans the dossier vault filtering by operational status and mission codename simultaneously
# Rep 2 — proved function returns empty when keyword has no match in the vault

def combine_missions(missions,status,keyword):
    result = ""
    i = 0
    

    while i  < len(missions):
        if keyword in missions[i]["name"] and missions[i]["status"] == status:
            result += "Missions: " + missions[i]["name"] + " | Status: " + missions[i]["status"] + "\n"

        i += 1

    return result

print(combine_missions([{"name": "Ghost Protocol", "status": "Active"}],"Active","Classified")) 
