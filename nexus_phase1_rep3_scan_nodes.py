# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# Description: Seven agent vault. Three LEGACY nodes across positions one five and seven.
# What this rep proved: continue fires on every match regardless of position or quantity



def scan_nodes(agents):
    for agent in agents:
        if agent["firmware"] == "LEGACY":
            continue
        print("NODE PROCESSED: " + agent["name"])
agents = [{"name": "Node-1", "firmware": "LEGACY"},
          {"name": "Node-2", "firmware": "CURRENT"},
          {"name": "Node-3", "firmware": "CURRENT"},
          {"name": "Node-4", "firmware": "CURRENT"},
          {"name": "Node-5", "firmware": "LEGACY"},
          {"name": "Node-6", "firmware": "CURRENT"},
           {"name": "Node-7", "firmware": "LEGACY"}]        
scan_nodes(agents)



if agent["firmware"] == "LEGACY":
