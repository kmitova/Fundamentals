gifts = input().split()

command = input()
while not command == "No Money":
    current_command = command.split()
    action = current_command[0]
    if action == "OutOfStock":
        gift = current_command[1]
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = "None"
    elif action == "Required":
        gift = current_command[1]
        index = int(current_command[2])
        if index in range(len(gifts)):
            gifts[index] = gift
    elif action == "JustInCase":
        gift = current_command[1]
        gifts[-1] = gift
    command = input()

items = [el for el in gifts if not el == "None"]
print(*items)
