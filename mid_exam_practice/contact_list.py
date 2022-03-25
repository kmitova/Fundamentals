contacts = input().split()
time_to_break = False
while True:
    command = input().split()
    action = command[0]

    if action == "Add":
        contact = command[1]
        index = int(command[2])
        if contact not in contacts:
            contacts.append(contact)
        else:
            if index in range(len(contacts)):
                # old_index = contacts.index(contact)
                # contacts.insert(index, contacts.pop(old_index))
                contacts.insert(index, contact)
    elif action == "Remove":
        index = int(command[1])
        if index in range(len(contacts)):
            contacts.pop(index)
    elif action == "Export":
        start_index = int(command[1])
        count = int(command[2])
        if count > len(contacts[start_index:]):
            print(" ".join(contacts[start_index:]))
        else:
            print(" ".join(contacts[start_index: count]))
    elif action == "Print":
        if command[1] == "Normal":
            time_to_break = True
            break
        elif command[1] == "Reversed":
            contacts.reverse()
            time_to_break = True
            break

if time_to_break:
    print(f'Contacts: {" ".join(contacts)}')