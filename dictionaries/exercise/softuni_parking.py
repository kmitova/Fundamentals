n = int(input())
cars = {}

for i in range(n):
    command = input().split()
    username = command[1]
    if command[0] == "register":
        if username not in cars:
            cars[username] = command[2]
            print(f"{username} registered {cars[username]} successfully")
        else:
            print(f"ERROR: already registered with plate number {cars[username]}")
    elif command[0] == "unregister":
        if username not in cars:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            cars.pop(username)

for key, val in cars.items():
    print(f"{key} => {val}")

