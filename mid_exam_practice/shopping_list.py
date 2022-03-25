shopping_list = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break
    current_command = command.split()
    current_action = current_command[0]
    item = current_command[1]
    if current_action == "Urgent":
        if item in shopping_list:
            continue
        else:
            shopping_list.insert(0, item)
    elif current_action == "Unnecessary":
        if item not in shopping_list:
            continue
        else:
            shopping_list.remove(item)
    elif current_action == "Correct":

        if item in shopping_list:
            new_item = current_command[2]
            index = shopping_list.index(item)
            shopping_list.insert(index, new_item)
            shopping_list.remove(item)
        else:
            continue
    elif current_action == "Rearrange":
        if item in shopping_list:
            shopping_list.remove(item)
            shopping_list.append(item)
        else:
            continue

print(", ".join(shopping_list))
