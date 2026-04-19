# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# Build Two locked cold — build_priority_signal — rotated vault data — RELAY_SENTINEL_04 — three clean reps confirmed sovereign

AGENT_ID = "SIGNAL_OPERATIVE_01"
VALID_PRIORITIES = {"STANDARD", "URGENT", "DEGRADED"}

def build_priority_signal(node_id, system_class, priority="STANDARD"):
    priority = str(priority).strip().upper()

    if priority not in VALID_PRIORITIES:
        print(f"REJECTION: {AGENT_ID} | PRIORITY: {priority} not recognized")
        return priority, "SIGNAL_REJECTED"

    try:
        node_id = str(node_id).strip()
        system_class = str(system_class).strip()
        signal = " :: ".join([node_id, system_class, priority])
        print(f"SIGNAL CONFIRMED: {AGENT_ID} | {signal}")
        return priority, signal
    except Exception as e:
        print(f"FAILURE ALERT: {AGENT_ID} | DATA: {node_id}, {system_class}, {priority} | REASON: {e}")
        return priority, "SIGNAL_BUILD_FAILED"

priority_result, signal_result = build_priority_signal("NODE_ALPHA", "RECON_ARRAY", "urgent")
print(priority_result)
print(signal_result)
