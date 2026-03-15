# Day 10 — NEXUS Mission Logger — Rep 3 — Final Clean Build
def log_missions(missions):
    result = ""


    i = 0

    while i < len(missions):
        result += "Mission: " + missions[i]["name"] + " | Status: " + missions[i]["status"] + "\n" 
        i += 1

    return result


print(log_missions([{"name": "Shadow Protocol", "status": "Pending"}]))

    
