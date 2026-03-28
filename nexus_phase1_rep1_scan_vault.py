# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# Description: Sweep the vault. First confirmed breach kills the sweep.
# What this rep proved: break terminates the sweep(loop) on first match.
# Sovereign.


def scan_vault(agents):
    for agent in agents:
        if agent["status"] == "BREACH":
            print("BREACH CONFIRMED. SWEEP TERMINATED.")
            break

agents = [{"name": "Sentinel-1", "status": "CLEAR"},
          {"name": "Sentinel-2", "status": "BREACH"},
          {"name": "Sentinel-3", "status": "CLEAR"}]
scan_vault(agents)
