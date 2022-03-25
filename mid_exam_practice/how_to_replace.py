# how to replace


initial_list = input().split("!")
command = input()

current_command = command.split()
current_action = current_command[0]
item = current_command[1]
if current_action == "Correct":
    if item in initial_list:
        new_item = current_command[2]
        index = initial_list.index(item)
        initial_list.insert(index, new_item)
        initial_list.remove(item)
print(initial_list)