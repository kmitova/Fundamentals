info = input()
bands = {}
durations = {}
total_time = 0
while not info == "start of concert":
    current = info.split("; ")
    action = current[0]
    name = current[1]
    if action == "Add":
        if name not in bands:
            bands[name] = []

        members = current[2].split(", ")
        for member in members:
            if member not in bands[name]:
                bands[name].append(member)
    elif action == "Play":
        time = int(current[2])
        if name not in durations:
            durations[name] = 0
        durations[name] += time
        total_time += time
    info = input()

band_name = input()

sorted_durations = sorted(durations.items(), key=lambda kvp: (-kvp[1], kvp[0]))
print(f"Total time: {total_time}")
for key, value in sorted_durations:
    print(f"{key} -> {value}")
if band_name in bands:
    print(band_name)
    for item in bands[band_name]:
        print(f"=> {item}")
