# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# File: nexus_phase1_rep3_scan_vault.py
# Phase: 1
# Description: Sweep the vault. Breach in position three. Break fires on last dossier.
# What this rep proved: break fires at any vault position. Kill switch is position independent.

def scan_vault(agents):
    for agent in agents:
        if agent["status"] == "BREACH":
            print("BREACH CONFIRMED. SWEEP TERMINATED.")    
            break
agents = [{"name": "Sentinel-1", "status": "CLEAR"},
          {"name": "Sentinel-2", "status": "CLEAR"},
          {"name": "Sentinel-3", "status": "BREACH"}]    
scan_vault(agents)  
