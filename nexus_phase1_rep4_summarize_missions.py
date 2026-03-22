# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# nexus_phase1_rep4_summarize_missions.py
# NEXUS Systems — Phase 1
# Successfully scanned three mission dossiers and returned a full formatted briefing
# Proved that summarize_missions handles multiple dossiers and stamps the correct total at the bottom

def summarize_missions(missions):
    result = ""
    count = 0
    i = 0

    while i < len(missions):
        result += "Missions: " + missions[i]["name"] + " | status: " + missions[i]["status"] + "\n"
        count += 1
        i += 1
    result +=  "Total Missions: " + str(count)    
    return result
print(summarize_missions([{"name": "Ghost Protocol", "status": "Active"},{"name": "Iron Sentinel", "status": "Active"},{"name": "Dark Recon", "status": "Inactive"}]))
