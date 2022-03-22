# 70/100

sides = {}

command = input()
while not command == "Lumpawaroo":
    if " | " in command:
        current = command.split(" | ")
        side = current[0]
        user = current[1]
        check = False
        if side not in sides:
            sides[side] = []
        for key, value in sides.items():
            if user in value:
                check = True
        if not check:
            sides[side].append(user)

    else:
        current = command.split(" -> ")
        side = current[1]
        user = current[0]
        if side in sides:
            # if user in sides[side]:
                for key, value in sides.items():
                    if user in value:
                        value.remove(user)
                        # sides[side].append(user)

                    # else:
                sides[side].append(user)

                print(f"{user} joins the {side} side!")
        else:
            sides[side] = [user]
    command = input()


for key, value in sides.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for user in value:
            print(f"! {user}")
