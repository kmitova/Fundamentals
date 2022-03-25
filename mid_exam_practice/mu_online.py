health = 100
bitcoins = 0
rooms = input().split("|")
lose = False
reached_room = 0
for room in rooms:
    reached_room += 1
    current_room = room.split()
    if current_room[0] == "potion":
        healing = int(current_room[1])
        health += healing
        if health > 100:
            diff = health - 100
            health -= diff
            healing = healing - diff
            print(f"You healed for {healing} hp.")
            print(f"Current health: {health} hp.")
        else:
            print(f"You healed for {healing} hp.")
            print(f"Current health: {health} hp.")

    elif current_room[0] == "chest":
        bitcoins_found = int(current_room[1])
        print(f"You found {bitcoins_found} bitcoins.")
        bitcoins += bitcoins_found
    else:
        monster = current_room[0]
        attack = int(current_room[1])
        health -= attack
        if health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {reached_room}")
            lose = True
            break

if not lose:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
