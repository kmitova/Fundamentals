items = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
won = False
while True:
    data = input()
    split_data = data.split()
    for index in range(0, len(split_data), 2):
        quantity = int(split_data[index])
        material = split_data[index+1].lower()
        if material in items:
            items[material] += quantity
            for k, v in items.items():
                if k == "shards" and v >= 250:
                    items[k] -= 250
                    print("Shadowmourne obtained!")
                    won = True
                elif k == "fragments" and v >= 250:
                    items[k] -= 250
                    print("Valanyr obtained!")
                    won = True
                elif k == "motes" and v >= 250:
                    items[k] -= 250
                    print("Dragonwrath obtained!")
                    won = True
        else:
            if material not in junk:
                junk[material] = quantity
            else:
                junk[material] += quantity

        if won:
            break
    if won:
        break

for k, v in items.items():
    print(f"{k}: {v}")

for k, v in junk.items():
    print(f"{k}: {v}")
