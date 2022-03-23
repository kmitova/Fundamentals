message = input()

command = input()
while not command == "Reveal":
    current = command.split(":|:")
    action = current[0]
    if action == "InsertSpace":
        index = int(current[1])
        message = message[:index] + " " + message[index:]
        print(message)

    elif action == "Reverse":
        substring = current[1]
        if substring in message:
            length = len(substring)

            start_index = message.index(substring)

            end_index = start_index + length - 1

            message = message[:start_index] + message[end_index+1:]
            substring_reversed = substring[::-1]
            message += substring_reversed
            print(message)
        else:
            print("error")
    elif action == "ChangeAll":
        substring = current[1]
        replacement = current[2]
        if substring in message:
            message = message.replace(substring, replacement)
            print(message)

    command = input()
print(f"You have a new text message: {message}")
