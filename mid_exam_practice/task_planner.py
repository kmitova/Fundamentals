times_of_tasks = list(map(int, input().split()))

command = input()

while not command == "End":
    current_command = command.split()
    action = current_command[0]
    if action == "Complete":
        index = int(current_command[1])
        if index in range(len(times_of_tasks)):
            times_of_tasks[index] = 0
    elif action == "Change":
        index = int(current_command[1])
        new_time = int(current_command[2])
        if index in range(len(times_of_tasks)):
            times_of_tasks[index] = new_time
    elif action == "Drop":
        index = int(current_command[1])
        if index in range(len(times_of_tasks)):
            times_of_tasks[index] = -1
    elif action == "Count":
        if current_command[1] == "Completed":
            completed = [el for el in times_of_tasks if el == 0]
            print(len(completed))
        elif current_command[1] == "Incomplete":
            incomplete = [el for el in times_of_tasks if el > 0]
            print(len(incomplete))
        elif current_command[1] == "Dropped":
            dropped = [el for el in times_of_tasks if el < 0]
            print(len(dropped))
    command = input()

incomplete_tasks = [el for el in times_of_tasks if el > 0]
incomplete_tasks = map(str, incomplete_tasks)
print(" ".join(incomplete_tasks))
