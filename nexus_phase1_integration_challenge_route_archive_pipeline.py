# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

AGENT_ID = "RELAY_SENTINEL_04"
VALID_PRIORITIES = {"STANDARD", "URGENT", "DEGRADED"}
DEFAULT_TRANSMISSION_TYPE = "STANDARD_RELAY"
LOG_FILE = "nexus_signal_archive.txt"

def route_transmission(node_id, transmission_type=DEFAULT_TRANSMISSION_TYPE, priority="STANDARD"):
    priority = str(priority).strip().upper()
    node_id = str(node_id).strip()
    transmission_type = str(transmission_type).strip().upper()
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

def archive_transmission(filename, raw_signal):
    try:
        with open(filename, "w") as f:
            f.write(raw_signal)
        print(f"ARCHIVE CONFIRMED: {AGENT_ID} | VAULT: {filename}")
        return raw_signal
    except Exception as e:
        print(f"ARCHIVE FAILURE: {AGENT_ID} | VAULT: {filename} | REASON: {e}")
        return "SIGNAL_ARCHIVE_FAILED"


priority_a, signal_a, node_a, attempts_a = route_transmission("RELAY_NORTH")
if signal_a not in ("SIGNAL_REJECTED", "SIGNAL_BUILD_FAILED"):
    archive_transmission(LOG_FILE, signal_a)
print(priority_a)
print(signal_a)
print(node_a)
print(attempts_a)


priority_result, signal_result, node_result, attempts_result = route_transmission(
    "RELAY_NORTH", "ENCRYPTED_RELAY", "urgent"
)
if signal_result not in ("SIGNAL_REJECTED", "SIGNAL_BUILD_FAILED"):
    archive_transmission(LOG_FILE, signal_result)
print(priority_result)
print(signal_result)
print(node_result)
print(attempts_result)
