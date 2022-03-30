stops = input()

command = input()
while not command == "Travel":
    current = command.split(":")
    action = current[0]
    if action == "Add Stop":
        index = int(current[1])
        string = current[2]
        if index in range(len(stops)):
            stops = stops[:index] + string + stops[index:]
    elif action == "Remove Stop":
        start = int(current[1])
        end = int(current[2])
        if start in range(len(stops)) and end in range(len(stops)):
            stops = stops[:start] + stops[end+1:]
    elif action == "Switch":
        old = current[1]
        new = current[2]
        if old in stops:
            stops = stops.replace(old, new)

    print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")

