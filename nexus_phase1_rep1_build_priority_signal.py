# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

#File: nexus_phase1_rep1_build_priority_signal.py
# Phase: 1
# Description: Deeper function architecture. Default parameters and multiple return values.
# Proved: Priority secured independently above the try block. Two-value return with type
# contract honored on every path. Default parameter fires when no priority arrives.
def build_priority_signal(node_id, system_class, priority="STANDARD"):
    priority = str(priority).strip()        # above the try — secured first
    try:
        node_id, system_class = node_id.strip(), system_class.strip()
        signal = " :: ".join([node_id, system_class, priority])
        return priority, signal
    except Exception as e:
        print(f"FAILURE ALERT: {AGENT_ID} | DATA: {node_id},{system_class},{priority} | REASON: {e}")
        return priority, "SIGNAL_BUILD_FAILED"
