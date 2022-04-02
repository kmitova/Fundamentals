key = input()

info = input()
while not info == "Generate":
    current = info.split(">>>")
    action = current[0]
    if action == "Contains":
        substring = current[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print("Substring not found!")
    elif action == "Flip":
        direction = current[1]
        start = int(current[2])
        end = int(current[3])
        if direction == "Upper":
            key = key.replace(key[start:end], key[start:end].upper())
        else:
            key = key.replace(key[start:end], key[start:end].lower())
        print(key)
    elif action == "Slice":
        start = int(current[1])
        end = int(current[2])
        key = key[:start] + key[end:]
        print(key)

    info = input()

print(f"Your activation key is: {key}")
