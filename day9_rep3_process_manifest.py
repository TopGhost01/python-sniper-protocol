# Day 9 — Process Manifest — Clean Build Rep 3
def process_manifest(items):
    result = ""
    i = 0

    while i < len(items):
        result += "Item: " + items[i] + "\n"
        i += 1

    return result

print(process_manifest(["Ammo", "Rifles", "Glocks"]))
