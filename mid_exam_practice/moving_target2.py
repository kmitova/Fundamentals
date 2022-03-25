# 100/100

sequence = input().split()
targets = (list(map(int, sequence)))

command = input()
while not command == "End":
    current = command.split()
    action = current[0]
    index = int(current[1])
    if action == "Shoot":
        power = int(current[2])
        if index in range(len(targets)):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    elif action == "Add":
        value = int(current[2])
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":

        radius = int(current[2])

        start = index - radius
        end = index + radius

        if start >= 0 and end < len(targets):
            del targets[start: end + 1]
        else:
            print("Strike missed!")
    command = input()

targets = list(map(str, targets))
print("|".join(targets))
