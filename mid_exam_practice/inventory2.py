items = input().split(", ")
command = input()
while not command == "Craft!":
    current = command.split(" - ")
    action = current[0]
    if action == "Collect":
        item = current[1]
        if item not in items:
            items.append(item)
    elif action == "Drop":
        item = current[1]
        if item in items:
            items.remove(item)
    elif action == "Renew":
        item = current[1]
        if item in items:
            items.remove(item)
            items.append(item)
    elif action == "Combine Items":
        old_and_new = current[1].split(":")
        old_item = old_and_new[0]
        new_item = old_and_new[1]
        if old_item in items:
            old_index = items.index(old_item)
            items.insert(old_index+1, new_item)
    command = input()

print(", ".join(items))
