energy = 100
coins = 100
events = input().split("|")
energy_gained = 0

failed = False
for event in events:
    current_event = event.split("-")
    event_type = current_event[0]
    number = int(current_event[-1])

    if event_type == "rest":
        if (energy + number) > 100:
            print("You gained 0 energy.")
        else:
            print(f"You gained {number} energy.")
            energy += number
        print(f"Current energy: {energy}.")
    elif event_type == "order":
        if energy < 30:
            energy += 50
            print("You had to rest!")
            continue
        energy -= 30
        coins += number
        print(f"You earned {number} coins.")
    else:
        ingredient = event_type
        if coins > number:
            coins -= number
            print(f"You bought {ingredient}.")
        else:
            failed = True
            print(f"Closed! Cannot afford {ingredient}.")
            break

if not failed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

