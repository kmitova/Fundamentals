def parking():
    users = {}
    lines = int(input())
    for line in range(lines):
        info = input()
        current = info.split()
        username = current[1]
        if len(current) == 2:
            if username not in users:
                print(f"ERROR: user {username} not found")
            else:
                del users[username]
                print(f"{username} unregistered successfully")
        else:
            plate = current[2]
            if username not in users:
                users[username] = plate
                print(f"{username} registered {plate} successfully")
            else:
                print(f"ERROR: already registered with plate number {plate}")

    for user in users:
        print(f"{user} => {users[user]}")


parking()
