numbers = list(map(int, input().split()))

command = input()

while not command == "End":
    current_command = command.split()
    action = current_command[0]
    if action == "Switch":
        index = int(current_command[1])
        if index in range(len(numbers)):
            numbers[index] = - numbers[index]
    elif action == "Change":
        index = int(current_command[1])
        value = int(current_command[2])
        if index in range(len(numbers)):
            numbers[index] = value
    elif action == "Sum":
        if current_command[1] == "Positive":
            positives = [x for x in numbers if x >= 0]
            print(sum(positives))
        elif current_command[1] == "Negative":
            negatives = [x for x in numbers if x < 0]
            print(sum(negatives))
        elif current_command[1] == "All":
            print(sum(numbers))
    command = input()

output = [x for x in numbers if x >= 0]
output = map(str, output)
print(" ".join(output))
