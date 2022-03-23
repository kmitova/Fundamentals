users = {}
old_side = 0
command = input()
while not command == "Lumpawaroo":
    if " | " in command:
        current = command.split(" | ")
        side = current[0]
        user = current[1]
        check = False
        for key, values in users.items():
            if user in values:
                check = True
                break
        if check is False:
            if side not in users:
                users[side] = [user]
            elif side in users and user not in users[side]:
                users[side].append(user)

    elif " -> " in command:
        current = command.split(" -> ")
        user = current[0]
        side = current[1]
        for key, values in users.items():
            if user in values:
                values.remove(user)
                break
        if side not in users:
            users[side] = [user]
            print(f"{user} joins the {side} side!")
        elif side in users and user not in users[side]:
            users[side].append(user)
            print(f"{user} joins the {side} side!")
    command = input()


for key, values in users.items():
    if len(values) > 0:
        print(f"Side: {key}, Members: {len(values)}")
        for v in values:
            print(f"! {v}")
