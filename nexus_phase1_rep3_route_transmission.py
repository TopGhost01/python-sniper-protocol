# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# route_transmission locked cold — two default parameters — named constant — upfront normalization — four return values — three clean reps confirmed

AGENT_ID = "RELAY_SENTINEL_04"
VALID_PRIORITIES = {"STANDARD", "URGENT", "DEGRADED"}
DEFAULT_TRANSMISSION_TYPE = "STANDARD_RELAY"

def route_transmission(node_id, transmission_type=DEFAULT_TRANSMISSION_TYPE, priority="STANDARD"):

    priority = str(priority).strip().upper()
    transmission_type = str(transmission_type).strip().upper()
    node_id = str(node_id).strip()

    if priority not in VALID_PRIORITIES:
        print(f"REJECTION: {AGENT_ID} | PRIORITY: {priority} not recognized")
        return priority, "SIGNAL_REJECTED", node_id, 0

    try:
        signal = " :: ".join([node_id, transmission_type, priority])
        attempt_count = 1
        print(f"SIGNAL CONFIRMED: {AGENT_ID} | {signal} | ATTEMPT: {attempt_count}")
        return priority, signal, node_id, attempt_count

    except Exception as e:
        print(f"FAILURE ALERT: {AGENT_ID} | DATA: {node_id}, {transmission_type}, {priority} | REASON: {e}")
        return priority, "SIGNAL_BUILD_FAILED", node_id, 0

# First test — defaults triggered by omission.
priority_a, signal_a, node_a, attempts_a = route_transmission("RELAY_NORTH")
print(priority_a)
print(signal_a)
print(node_a)
print(attempts_a)

# Second test — defaults overridden.
priority_b, signal_b, node_b, attempts_b = route_transmission("RELAY_SOUTH", "ENCRYPTED_RELAY", "urgent")
print(priority_b)
print(signal_b)
print(node_b)
print(attempts_b)
