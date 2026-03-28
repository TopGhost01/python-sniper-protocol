# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

#File: nexus_phase1_rep2_scan_vault.py
# Phase: 1
# Description: Sweep the vault. First confirmed breach kills the sweep.
# What this rep proved: break terminates on first breach regardless of vault size.

def scan_vault(agents):
    for agent in agents:
        if agent["status"] == "BREACH":
            print("BREACH CONFIRMED. TERMINATE SWEEP.")
            break

agents = [{"name": "Sentinel-1", "status": "CLEAR" },
          {"name": "Sentinel-2", "status": "BREACH"},
          {"name": "Sentinel-3", "status": "CLEAR"},
          {"name": "Sentinel-4", "status": "BREACH"}]    
scan_vault(agents)
