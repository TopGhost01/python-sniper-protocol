# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# File: nexus_phase1_integration_challenge_scan_vault.py
# Phase: 1
# Description: Eight operative vault. Break on COMPROMISED. Collect SOVEREIGN. Return vault.
# What this rep proved: Classification, accumulation, and flow control wired together under pressure.

def scan_vault(operatives):
    sovereign_operatives = []
    for operative in operatives:
        if operative["status"] == "COMPROMISED":
            print("COMPROMISED CONFIRMED. SWEEP TERMINATED.")
            break
        elif operative["clearance"] == "SOVEREIGN":
            sovereign_operatives.append(operative)
    return sovereign_operatives  
vault = [{"name": "Cipher-1", "clearance":"SOVEREIGN", "status": "ACTIVE"},
         {"name": "Cipher-2", "clearance": "CLASSIFIED", "status": "ACTIVE"},
         {"name": "Cipher-3", "clearance": "RESTRICTED", "status": "ACTIVE"},
         {"name": "Cipher-4", "clearance": "SOVEREIGN", "status": "COMPROMISED"},
         {"name": "Cipher-5", "clearance": "CLASSIFIED","status": "ACTIVE"},
         {"name": "Cipher-6", "clearance": "RESTRICTED","status": "ACTIVE"},
         {"name": "Cipher-7", "clearance": "SOVEREIGN", "status": "ACTIVE"}]    
scan_vault(vault)
