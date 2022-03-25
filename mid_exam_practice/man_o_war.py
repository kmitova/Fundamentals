pirate_ship_status = list(map(int, input().split(">")))
war_ship_status = list(map(int, input().split(">")))
stalemate = True
max_health = int(input())

command = input()

while not command == "Retire":
    current_command = command.split()
    if current_command[0] == "Fire":
        idx = int(current_command[1])
        damage = int(current_command[2])
        if idx >= 0 and idx < len(war_ship_status):
            war_ship_status[idx] -= damage
            if war_ship_status[idx] <= 0:
                print("You won! The enemy ship has sunken.")
                stalemate = False
                break
    elif current_command[0] == "Defend":
        start_idx = int(current_command[1])
        end_idx = int(current_command[2])
        damage = int(current_command[3])
        if start_idx >= 0 and end_idx >= 0 and start_idx < len(pirate_ship_status) and end_idx < len(pirate_ship_status):
            for index in range(start_idx, end_idx + 1):
                pirate_ship_status[index] -= damage
                if pirate_ship_status[index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    stalemate = False
                    break
    elif current_command[0] == "Repair":
        idx = int(current_command[1])
        health = int(current_command[2])
        if idx >= 0 and idx < len(pirate_ship_status):
            pirate_ship_status[idx] += health
            if pirate_ship_status[idx] > max_health:
                diff = pirate_ship_status[idx] - max_health
                pirate_ship_status[idx] -= diff
    elif current_command[0] == "Status":
        need_repair_soon = [x for x in pirate_ship_status if x < max_health * 0.2]
        count = len(need_repair_soon)
        print(f"{count} sections need repair.")
    command = input()

if stalemate:
    sum_pirate = sum(pirate_ship_status)
    sum_war = sum(war_ship_status)
    print(f"Pirate ship status: {sum_pirate}")
    print(f"Warship status: {sum_war}")
