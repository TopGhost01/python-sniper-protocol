# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# File: nexus_phase1_rep2_clean_transmission.py
# Phase: 1
# Description: String methods — strip, split, join — structural rep
# What this rep proved: Architect drives all three new syntax lines from memory without scaffold prompts. Explicit delimiter contract confirmed. Chain held end to end.

def clean_transmission(raw_signal):
    stripped = raw_signal.strip()
    components = stripped.split("|")
    clean_signal = " :: ".join(components)
    print(clean_signal)
    return clean_signal
print(clean_transmission(" NOMINAL|STATION_47|SECTOR_EAST "))
