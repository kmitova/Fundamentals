meals = {}
unliked = 0
command = input()
while not command == "Stop":
    current = command.split("-")
    action = current[0]
    guest = current[1]
    meal = current[2]
    if action == "Like":
        if guest not in meals:
            meals[guest] = [meal]
        elif meal not in meals[guest]:
            meals[guest].append(meal)
    elif action == "Unlike":
        if guest in meals:
            if meal in meals[guest]:
                meals[guest].remove(meal)
                print(f"{guest} doesn't like the {meal}.")
                unliked += 1
            else:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            print(f"{guest} is not at the party.")
    command = input()

sorted_meals = sorted(meals.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
for name, value in sorted_meals:
    print(f"{name}: {', '.join(value)}")

print(f"Unliked meals: {unliked}")
