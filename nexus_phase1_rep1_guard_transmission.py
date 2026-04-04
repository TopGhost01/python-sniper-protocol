#A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# File: nexus_phase1_rep1_guard_transmission.py
# Phase: 1
# Description: try/except wraps string chain and file write — both at-risk
# What this rep proves: failure path is the kill switch signal
# Every sovereign system knows the difference between success and silence
AGENT_ID = "NEXUS-RELAY-7"
def guard_transmission(filename,raw_signal):
    try:
        stripped = raw_signal.strip()
        components = stripped.split("|")
        clean_signal = " :: ".join(components)
        with open(filename,"a") as vault:
            vault.write(clean_signal + "\n")
        print(f"[{AGENT_ID}] ARCHIVED: {clean_signal}")
        return clean_signal
    except Exception as e:
        print(f"[{AGENT_ID}] ARCHIVE FAILURE: {e}")
        return None
TELEMETRY_LOG = "telemetry_archive.txt"
SIGNALS = [
        "  HR-112|SPO2-97|NOMINAL  ",
        "  HR-58|SPO2-84|CRITICAL  ",
        "  HR-88|SPO2-95|STABLE  ",
    ]
for signal in SIGNALS:
    guard_transmission(TELEMETRY_LOG, signal)
