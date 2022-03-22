lines = int(input())

dragons = {}

for line in range(lines):
    data = input()
    current = data.split()
    color = current[0]
    name = current[1]
    damage = current[2]
    health = current[3]
    armor = current[4]
    if armor == "null":
        armor = 10
    else:
        armor = int(current[4])
    if health == "null":
        health = 250
    else:
        health = int(current[3])
    if damage == "null":
        damage = 45
    else:
        damage = int(current[2])
    if color not in dragons:
        dragons[color] = {name: [damage, health, armor]}
    else:
        if name != dragons[color]:
            dragons[color][name] = [damage, health, armor]

for key, value in dragons.items():
    avg_damage = []
    avg_health = []
    avg_armor = []
    for k, v in value.items():
        avg_damage.append(v[0])
        avg_health.append(v[1])
        avg_armor.append(v[2])
    print(f"{key}::({sum(avg_damage) / len(avg_damage):.2f}/{sum(avg_health) / len(avg_health):.2f}/{sum(avg_armor) / len(avg_armor):.2f})")

    sorted_v = sorted(value.items(), key=lambda kvp: kvp[0])
    for name, nums in sorted_v:
        print(f"-{name} -> damage: {nums[0]}, health: {nums[1]}, armor: {nums[2]}")
