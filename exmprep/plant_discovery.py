lines = int(input())
plants = {}
for line in range(lines):
    info = input()
    current = info.split("<->")
    plant = current[0]
    rarity = int(current[1])
    plants[plant] = [rarity]

command = input()
while not command == "Exhibition":
    current = command.split(": ")
    action = current[0]
    if action == "Rate":
        plant, rating = current[1].split(" - ")
        if plant in plants:
            plants[plant].append(int(rating))
        else:
            print("error")
    elif action == "Update":
        plant, rarity = current[1].split(" - ")
        if plant in plants:
            plants[plant][0] = int(rarity)
        else:
            print("error")
    elif action == "Reset":
        plant = current[1]
        if plant in plants:
            del plants[plant][1:]
        else:
            print("error")
    command = input()

# print(plants)

for key, value in plants.items():
    if len(value) > 1:
        plants[key] = [value[0], sum(value[1:]) / len(value[1:])]
# print(plants)

sorted_plants = (sorted(plants.items(), key=lambda kvp: -kvp[1][0]))
# sorted_plants2 = sorted(sorted_plants.items(), key=lambda kvp: -kvp[1][1]
# print(sorted_plants)
print(f"Plants for the exhibition:")
for key, value in sorted_plants:
    if len(value) > 1:
        print(f"- {key}; Rarity: {value[0]}; Rating: {value[1]:.2f}")
    else:
        print(f"- {key}; Rarity: {value[0]}; Rating: 0.00")


# another solution
num = int(input())
plants = {}
for i in range(num):
    command = input().split("<->")
    plant = command[0]
    rarity = int(command[1])
    if plant not in plants.keys():
        plants[plant] = []
        plants[plant].append(rarity)
    else:
        plants[plant] = []
        plants[plant].append(rarity)

while True:
    command = input()
    if command == "Exhibition":
        break
    current_command = command.split(": ")[0]
    second_part = command.split(": ")[1]
    if "Rate" in command:
        plant_to_be_rated = second_part.split(" - ")[0]
        rating_plant = int(second_part.split(" - ")[1])
        if plant_to_be_rated not in plants.keys():
            print("error")
        else:
            plants[plant_to_be_rated].append(rating_plant)
    elif "Update" in command:
        plant_tobe_updated = second_part.split(" - ")[0]
        if plant_tobe_updated not in plants.keys():
            print("error")
        else:
            new_rarity = int(second_part.split(" - ")[1])
            plants[plant_tobe_updated].pop(0)
            plants[plant_tobe_updated].insert(0, new_rarity)
    elif "Reset" in command:
        plant_to_be_reset = command.split(": ")[1]
        if plant_to_be_reset not in plants.keys():
            print("error")
        else:
            rarity_to_add_back = plants[plant_to_be_reset][0]
            plants[plant_to_be_reset].clear()
            plants[plant_to_be_reset].append(rarity_to_add_back)
            # plants[plant_to_be_reset].insert(1, 0)
    else:
        print("error")

for key, value in plants.items():
    item_to_amend = value[1:]
    remaining_part = value[0]
    if len(item_to_amend) > 1:
        total = sum(item_to_amend)
        new_num = total / len(item_to_amend)
        value.clear()
        value.append(remaining_part)
        value.append(new_num)
    if len(value) == 1:
        value.append(0)

print(f"Plants for the exhibition:")
plants = dict(sorted(plants.items(), key=lambda x: (-x[1][0], -x[1][1])))
for key, value in plants.items():
    print(f"- {key}; Rarity: {int(value[0])}; Rating: {value[1]:.2f}")
