# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

def filter_missions(missions, status):
    result = ""
    i = 0

    while i < len(missions):
        if missions[i]["status"] == status:
            result += "Mission: " + missions[i]["name"] + "| Status: " + missions[i]["status"] + "\n"
        i += 1

    return result

print(filter_missions([{"name": "Shadow Protocol", "status": "Active"}],"Active"))        
