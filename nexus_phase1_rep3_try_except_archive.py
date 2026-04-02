# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# Description: archive_transmission with try except — error handling Block 3
# What this rep proved: Total blank screen reconstruction.










def archive_transmission(filename,raw_signal):
    stripped = raw_signal.strip()
    components = stripped.split("|")
    clean_signal = " :: ".join(components)
    try:
        with open(filename,"w") as f:
            f.write(clean_signal)
    except Exception as e:
        print(f"NEXUS ARCHIVE FAILURE: {e}")      
        return None
    print(clean_signal)
    return clean_signal
archive_transmission("nexus_archive.txt", " DISPATCH_098_1 | NOMINAL | PRIORITY 09 ")  
