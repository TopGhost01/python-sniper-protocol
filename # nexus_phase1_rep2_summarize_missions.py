# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# nexus_phase1_rep2_summarize_missions.py
# NEXUS Systems — Phase 1
# Demonstrated that result = "" is mandatory in mixed string and count functions
# Proved that omitting the string builder causes a NameError and breaks the entire briefing

def summarize_missions(missions):
    count = 0
    i = 0 

    while i < len(missions):
        result += "Mission: " + missions[i]["name"] + " | Status: " + missions[i]["status"] + "\n"
        count += 1
        i += 1
        result += "Total Missions: " + str(count)
    return result
print(summarize_missions([{"name": "Ghost Protocol", "Status": "Active"}]))    
