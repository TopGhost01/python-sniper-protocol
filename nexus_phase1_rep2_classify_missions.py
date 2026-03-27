# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# Phase: 1 | Function: classify_missions
# Description: Sweep over a vault of mission dictionaries.
# if elif else classification chain routes each dossier.
# Accumulator collects every labeled result.
# Rep proved: return outside the loop delivers the full vault.

def classify_missions(missions):
    result_vault= []
    for mission in missions:
        status = mission["status"]
        if status == "critical":
            label = "Mission " + mission["name"] + ": Immediate deployment ordered."
        elif status == "active":
            label = "Mission " + mission["name"] + ": Standard briefing in progress."
        else:
            label = "Mission " + mission["name"] + ": Holding orders issued."    
        result_vault.append(label)   
        print(label) 
    return result_vault
vault = [{"name": "Iron Gate", "status": "critical"},
         {"name": "Shadow Run", "status": "active"},
         {"name": "Cold Harbor", "status": "standby"}] 
classify_missions(vault)  
