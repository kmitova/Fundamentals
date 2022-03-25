health = 100
bitcoins = 0
rooms = input().split("|")
current_room = 0
died = False
for item in rooms:
    current_room += 1
    current = item.split()
    command = current[0]
    number = int(current[1])
    if command == "potion":
        if health + number <= 100:
            health += number

        else:
            number = 100 - health
            health += number
        print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        monster = current[0]
        health -= number
        if health <= 0:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {current_room}")
            died = True
            break
        else:
            print(f"You slayed {monster}.")

if not died:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")




