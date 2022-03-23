users = {}

command = input()
while not command == "Statistics":
    current = command.split("->")
    action = current[0]
    if action == "Add":
        username = current[1]
        if username in users:
            print(f"{username} is already registered!")
        else:
            users[username] = []
    elif action == "Send":
        username = current[1]
        email = current[2]
        users[username].append(email)
    elif action == "Delete":
        username = current[1]
        if username in users:
            del users[username]
        else:
            print(f"{username} not found!")
    command = input()


print(f"Users count: {len(users)}")
sorted_users = sorted(users.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

for key, value in sorted_users:
    print(f"{key}")
    for item in value:
        print(f"- {item}")
