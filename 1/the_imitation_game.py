message = input()

data = input()
while not data == "Decode":
    current = data.split("|")
    action = current[0]
    if action == "Move":
        number = int(current[1])
        to_move = message[:number]
        message = message[number:] + to_move
    elif action == "Insert":
        index = int(current[1])
        value = current[2]
        message = message[:index] + value + message[index:]
    elif action == "ChangeAll":
        substring = current[1]
        replacement = current[2]
        message = message.replace(substring, replacement)
    data = input()

print(f"The decrypted message is: {message}")
