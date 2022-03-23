wagons = int(input())

train = [0] * wagons

command = input()
while command != "End":
    current_command = command.split()
    action = current_command[0]
    if action == "add":
        number_of_people = int(current_command[1])
        train[-1] += number_of_people

    elif action == "insert":
        index = int(current_command[1])
        number_of_people = int(current_command[2])
        train[index] += number_of_people
    elif action == "leave":
        index = int(current_command[1])
        number_of_people = int(current_command[2])
        train[index] -= int(current_command[2])
    command = input()

print(train)
