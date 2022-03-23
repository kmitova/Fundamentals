capacity = int(input())
command = input()
messages = {}

while not command == "Statistics":
    current = command.split("=")
    action = current[0]
    if action == "Add":
        username = current[1]
        sent = int(current[2])
        received = int(current[3])
        if username not in messages:
            messages[username] = [sent, received]

    elif action == "Message":
        sender = current[1]
        receiver = current[2]
        if sender in messages and receiver in messages:
            messages[sender][0] += 1
            if messages[sender][0] >= capacity:
                del messages[sender]
                print(f"{sender} reached the capacity!")
            messages[receiver][1] += 1
            if messages[receiver][1] >= capacity:
                del messages[receiver]
                print(f"{receiver} reached the capacity!")
    elif action == "Empty":
        username = current[1]
        if username == "All":
            del messages
        else:
            if username in messages:
                del messages[username]
    command = input()

sorted_messages = sorted(messages.items(), key=lambda x: (-x[1][1], x[0]))

print(f"Users count: {len(messages)}")
for name, value in sorted_messages:
    print(f"{name} - {sum(value)}")
