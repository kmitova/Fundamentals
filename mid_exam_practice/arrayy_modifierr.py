numbers = list(map(int, input().split()))

command = input()
while not command == "end":
    current_command = command.split()
    action = current_command[0]

    if action == "swap":
        index1 = int(current_command[1])
        index2 = int(current_command[2])
        numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
    elif action == "multiply":
        index1 = int(current_command[1])
        index2 = int(current_command[2])
        numbers[index1] = numbers[index1] * numbers[index2]
    elif action == "decrease":
        numbers = [el-1 for el in numbers]

    command = input()

print(", ".join(list(map(str, numbers))))
