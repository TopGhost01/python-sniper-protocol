# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# Phase: 1
# Description: Sweep five nodes. Skip legacy firmware. Process functional nodes only.
# What this rep proved: continue skips one dossier without stopping the sweep.


def scan_nodes(agents):
    for agent in agents:
        if agent["firmware"] == "LEGACY":
            continue
        print("NODE PROCESSED: " + agent["name"])
            

agents = [{"name": "Node-1", "firmware": "CURRENT"},
          {"name": "Node-2", "firmware": "LEGACY"},
          {"name": "Node-3", "firmware": "CURRENT"},
          {"name": "Node-4", "firmware": "LEGACY"},
          {"name": "Node-5", "firmware": "CURRENT"}]
scan_nodes(agents)
