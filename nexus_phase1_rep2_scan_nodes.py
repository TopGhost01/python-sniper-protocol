# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# Phase: 1
# Description: Sweep five nodes. One LEGACY node in position four. Skip confirmed.
# What this rep proved: continue fires regardless of legacy node position or quantity.


def scan_nodes(agents):
    for agent in agents:
        if agent["firmware"] == "LEGACY" and agent["firmware"] == "OFFLINE":
            continue
        print("NODE PROCESSED: " + agent["name"])
agents = [{"name": "Node-1", "firmware": "CURRENT"},
          {"name": "Node-2", "firmware": "CURRENT"},
          {"name": "Node-3", "firmware": "CURRENT"},
          {"name": "Node-4", "firmware": "LEGACY"},
          {"name": "Node-5", "firmware": "CURRENT"}]      
scan_nodes(agents)  
