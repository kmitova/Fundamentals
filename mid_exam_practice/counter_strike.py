energy = int(input())
not_enough_energy = False
battle_count = 0

while True:
    command = input()
    if command == "End of battle":
        break
    distance = int(command)
    if energy < distance:
        not_enough_energy = True
        break
    energy -= distance
    battle_count += 1
    if battle_count % 3 == 0:
        energy += battle_count


if not_enough_energy:
    print(f"Not enough energy! Game ends with {battle_count} won battles and {energy} energy")

else:
    print(f"Won battles: {battle_count}. Energy left: {energy}")

