message = input()

info = input()
while not info == "Reveal":
    current = info.split(":|:")
    action = current[0]
    if action == "InsertSpace":
        index = int(current[1])
        message = message[:index] + " " + message[index:]
        print(message)
    elif action == "Reverse":
        substring = current[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message = message + substring[::-1]
            print(message)
        else:
            print("error")
    elif action == "ChangeAll":
        substring = current[1]
        replace = current[2]
        message = message.replace(substring, replace)
        print(message)
    info = input()

print(f"You have a new text message: {message}")
