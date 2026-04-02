# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# Phase: 1
# Description: archive_transmission with try except — error handling Block 1
# What this rep proved: try except structure understood. Success path and failure path separated cleanly. return None inside except confirmed. print and return clean_signal outside try except confirmed.


def archive_transmission(filename,raw_signal):
    stripped = raw_signal.strip()   
    components = stripped.split("|")
    clean_signal = " :: ".join(components)
    try:
        with open(filename,"w")as f:
            f.write(clean_signal)
    except Exception as e:
        print(f"NEXUS ARCHIVE FAILURE: {e}")    
        return None
    print(clean_signal)    
    return clean_signal
archive_transmission("nexus_archive.txt", " DISPATCH_7 | NOMINAL | PRIORITY 89")
