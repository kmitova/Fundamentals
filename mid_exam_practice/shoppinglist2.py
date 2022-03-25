groceries = input().split("!")

command = input()
while not command == "Go Shopping!":
    current = command.split()
    if len(current) == 3:
        action = current[0]
        olditem = current[1]
        newitem = current[2]
        if olditem in groceries:
            index = groceries.index(olditem)
            groceries[index] = newitem
    else:
        action = current[0]
        item = current[1]
        if action == "Urgent":
            if item not in groceries:
                groceries.insert(0, item)
        elif action == "Unnecessary":
            if item in groceries:
                groceries.remove(item)
        elif action == "Rearrange":
            if item in groceries:
                groceries.remove(item)
                groceries.append(item)
    command = input()

print(", ".join(groceries))
