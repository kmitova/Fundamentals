loot = input().split("|")
command = input()

while not command == "Yohoho!":
    tokens = command.split(" ")
    if tokens[0] == "Loot":
        items = tokens[1:]
        [loot.insert(0, x) for x in items if x not in loot]
    elif tokens[0] == "Drop":
        idx = int(tokens[1])
        if idx >= 0 and idx < len(loot):
            item = loot[idx]
            loot.append(loot.pop(idx))
    elif tokens[0] == "Steal":
        count = int(tokens[1])
        if count > len(loot):
            count = len(loot)
        stolen = loot[len(loot) - count:]
        loot = loot[:len(loot) - count]
        print(", ".join(stolen))

    command = input()

if len(loot) == 0:
    print("Failed treasure hunt.")
else:
    average_gain = sum([len(x) for x in loot]) / len(loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")


