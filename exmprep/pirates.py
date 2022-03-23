cities = {}

command = input()
while not command == "Sail":
    current = command.split("||")
    city = current[0]
    population = int(current[1])
    gold = int(current[2])
    if city not in cities:
        cities[city] = [population, gold]
    elif city in cities:
        cities[city][0] += population
        cities[city][1] += gold
    command = input()

info = input()
while not info == "End":
    current = info.split("=>")
    action = current[0]
    town = current[1]
    if action == "Plunder":
        people = int(current[2])
        gold = int(current[3])
        cities[town][0] -= people
        cities[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[town][0] <= 0 or cities[town][1] <= 0:
            print(f"{town} has been wiped off the map!")
            del cities[town]
    elif action == "Prosper":
        gold = int(current[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")
    info = input()

if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for key, value in cities.items():
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
