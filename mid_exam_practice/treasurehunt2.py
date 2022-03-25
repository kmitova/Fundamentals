treasure = input().split("|")
empty = False
command = input()
stolen = []
while not command == "Yohoho!":
    current = command.split()
    action = current[0]
    if action == "Loot":
        items = current[1:]
        for item in items:
            if item not in treasure:
                treasure.insert(0, item)
    elif action == "Drop":
        index = int(current[1])
        if index in range(len(treasure)):
            item = treasure[index]
            treasure.pop(index)
            treasure.append(item)
    elif action == "Steal":
        count = int(current[1])
        if count > len(treasure):
            print(", ".join(treasure))
            treasure.clear()
            empty = True
        else:
            treasure.reverse()
            stolen = treasure[:count]
            stolen.reverse()
            print(", ".join(stolen))
            treasure.reverse()
            treasure = [el for el in treasure if el not in stolen]
    command = input()

if len(treasure) == 0:
    print("Failed treasure hunt.")
else:
    length_all = 0
    for item in treasure:
        length = len(item)
        length_all += length
    avg = length_all / len(treasure)
    print(f"Average treasure gain: {avg:.2f} pirate credits.")
