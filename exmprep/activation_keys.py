key = input()
raw_key = key

command = input()
while not command == "Generate":
    current = command.split(">>>")
    action = current[0]
    if action == "Contains":
        substring = current[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print("Substring not found!")
    elif action == "Flip":
        start = int(current[2])
        end = int(current[3])
        if current[1] == "Lower":
            key = key[:start] + key[start:end].lower() + key[end:]
        elif current[1] == "Upper":
            key = key[:start] + key[start:end].upper() + key[end:]
        print(key)
    elif action == "Slice":
        start = int(current[1])
        end = int(current[2])
        key = key[:start] + key[end:]
        print(key)
    command = input()

print(f"Your activation key is: {key}")
