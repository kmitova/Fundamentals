message = input()

command = input()
while not command == "Decode":
    current = command.split("|")
    action = current[0]
    if action == "Move":
        number = int(current[1])
        to_move = message[:number]
        message = message[number:]
        message += to_move
    elif action == "Insert":
        index = int(current[1])
        value = current[2]
        message = message[:index] + value + message[index:]
    elif action == "ChangeAll":
        substring = current[1]
        replacement = current[2]
        message = message.replace(substring, replacement)
    command = input()

print(f"The decrypted message is: {message}")
