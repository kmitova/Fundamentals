#  80/100

pirate_ship = list(map(int, input().split(">")))
war_ship = list(map(int, input().split(">")))
max_health = int(input())
command = input()
stalemate = True
count = 0
while not command == "Retire":
    current = command.split()
    action = current[0]
    if action == "Fire":
        index = int(current[1])
        damage = int(current[2])
        if index in range(len(war_ship)):
            war_ship[index] -= damage
            if war_ship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                pirates_won = True
                exit()
    elif action == "Defend":
        start = int(current[1])
        end = int(current[2])
        damage = int(current[3])
        if start in range(len(pirate_ship)) and end in range(len(pirate_ship)):
            for i in range(start, end+1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    warship_won = True
                    exit()
    elif action == "Repair":
        index = int(current[1])
        health = int(current[2])
        if index in range(len(pirate_ship)):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health:
                pirate_ship[index] = max_health
    elif action == "Status":
        for item in pirate_ship:
            if item < max_health * 0.2:
                count += 1
        print(f"{count} sections need repair.")

    command = input()

print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(war_ship)}")

