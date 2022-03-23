heroes = {}

command = input()
while not command == "End":
    current = command.split()
    action = current[0]
    name = current[1]
    if action == "Enroll":
        if name not in heroes:
            heroes[name] = []
        else:
            print(f"{name} is already enrolled.")
    elif action == "Learn":
        spell = current[2]
        if name not in heroes:
            print(f"{name} doesn't exist.")
        else:
            if spell in heroes[name]:
                print(f"{name} has already learnt {spell}")
            else:
                heroes[name].append(spell)
    elif action == "Unlearn":
        spell = current[2]
        if name not in heroes:
            print(f"{name} doesn't exist.")
        else:
            if spell not in heroes[name]:
                print(f"{name} doesn't know {spell}")
            else:
                heroes[name].remove(spell)

    command = input()

sorted_heroes = sorted(heroes.items(), key=lambda x: (-len(x[1]), x[0]))
print("Heroes:")
for name, collection in sorted_heroes:
    print(f"== {name}: {', '.join(collection)}")
