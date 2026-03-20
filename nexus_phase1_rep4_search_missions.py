# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

def search_missions(missions, keyword):
    result = ""    
    i = 0

    while i < len(missions):
        if keyword in missions[i]["name"]:
            result += "Missions: " + missions[i]["name"] + " | Status: " + missions[i]["status"] + "\n"
        i += 1

    return result
print(search_missions([{"name": "Ghost Protocol", "status": "Active"}],"Ghost")) 
