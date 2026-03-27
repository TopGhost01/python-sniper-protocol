# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# nexus_phase1_rep1_classify_missions.py
# NEXUS Systems — Phase 1
# For loop with if elif else chain classifying every dossier in the vault by status
# Rep 1 proved the elif chain routes every dossier to a precise outcome and else guarantees no dossier falls through unclassified.

def classify_missions(missions):
    result_vault = []
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

vault = [
    {"name": "IRON GATE", "status": "critical"},
    {"name": "SHADOW RUN", "status": "active"},
    {"name": "COLD HARBOR", "status": "standby"}
]

classify_missions(vault)
