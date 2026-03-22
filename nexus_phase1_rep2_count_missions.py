# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# nexus_phase1_rep2_count_missions.py
# NEXUS Systems — Phase 1
# Counts confirmed active operations matching a given status
# Rep 2 proved the accumulator advances by one per confirmed match not by arbitrary value

def count_missions(missions,status):
    count = 0 
    i = 0
    while i < len(missions):
        if missions[i]["status"] == status:
            count += 1
        i += 1

    return count
print(count_missions([{"name": "Ghost Protocol", "status": "Active"}],"Active"))   
