# A human being born in a box under a microscope in a lab
# arrives with a spirit that animates it uniquely.
# No environment creates it.
# No system contains it.
# No technology extinguishes it.

# Phase 1 | Thread Two | File I/O
# Description: Receives a raw signal and a filename. Decontaminates, dissects, assembles, writes to disk.
# What this rep proved: New syntax retyped from memory. With block architecture sovereign. String chain from instinct.


def archive_transmission(filename,raw_signal):
    stripped = raw_signal.strip()
    components = stripped.split("|")
    clean_signal = " :: ".join(components)
    with open(filename,"w") as f:
        f.write(clean_signal)
 
    print(clean_signal)    
    return clean_signal
archive_transmission("nexus_archive.txt", " DISPLAY_15 | NOMINIAL | PRIORITY TWO ")
