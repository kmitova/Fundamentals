num = int(input())

plants = {}

for i in range(num):
    info = input()
    current = info.split("<->")
    name = current[0]
    rarity = current[1]
    if name not in plants:
        plants[name] = {"rarity": rarity, "rating": []}
    else:
        plants[name]["rarity"] = rarity

command = input()

while not command == "Exhibition":
    current = command.split(": ")
    action = current[0]
    if action == "Rate":
        info = current[1].split(" - ")
        plant = info[0]
        rating = float(info[1])
        if plant not in plants:
            print("error")
        else:
            plants[plant]["rating"].append(rating)
    elif action == "Update":
        info = current[1].split(" - ")
        plant = info[0]
        new_rarity = info[1]
        if plant not in plants:
            print("error")
        else:
            plants[plant]["rarity"] = new_rarity
    elif action == "Reset":
        plant = current[1]
        if plant not in plants:
            print("error")
        else:
            plants[plant]["rating"].clear()
    command = input()

print("Plants for the exhibition:")

for key, value in plants.items():
    rarity = value["rarity"]
    if len(value["rating"]) > 0:
        rating = sum(value["rating"]) / len(value["rating"])
    else:
        rating = 0
    print(f"- {key}; Rarity: {rarity}; Rating: {rating:.2f}")
