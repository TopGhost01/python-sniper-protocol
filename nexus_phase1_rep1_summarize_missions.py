# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# nexus_phase1_rep1_summarize_missions.py
# NEXUS Systems — Phase 1
# Multi-line formatted string output using str() converter
# Proved that integers must be converted to strings before attaching to a string builder

def summarize_missions(missions):
    result = ""
    count = 0 
    i = 0
    while i < len(missions):
        result += "Missions: " + missions[i]["name"] + " | Status: " + missions[i]["status"] + "\n"
        count += 1
        i += 1
        result += "Total Missions: " + str(count)
    return result
print(summarize_missions([{"name": "Ghost Protocol", "status": "Active"}]))  
