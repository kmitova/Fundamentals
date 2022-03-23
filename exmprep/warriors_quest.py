text = input()

command = input()
while not command == "For Azeroth":
    current = command.split()
    action = current[0]
    if action == "GladiatorStance":
        text = text.upper()
        print(text)
    elif action == "DefensiveStance":
        text = text.lower()
        print(text)
    elif action == "Dispel":
        index = int(current[1])
        letter = current[2]
        if index in range(len(text)):
            for ind in range(len(text)):
                if ind == index:
                    text = text.replace(text[ind], letter, 1)
                    break
            print("Success!")
        else:
            print("Dispel too weak.")
    elif action == "Target":
        if current[1] == "Change":
            substring = current[2]
            substring2 = current[3]
            text = text.replace(substring, substring2, 1)
            print(text)
        elif current[1] == "Remove":
            substring = current[2]
            text = text.replace(substring, "")
            print(text)
    else:
        print("Command doesn't exist!")
    command = input()
