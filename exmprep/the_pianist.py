number = int(input())

pieces = {}

for i in range(number):
    data = input()
    current = data.split("|")
    piece = current[0]
    composer = current[1]
    key = current[2]
    pieces[piece] = [composer, key]


command = input()
while not command == "Stop":
    current = command.split("|")
    action = current[0]
    name = current[1]
    if action == "Add":
        composer = current[2]
        key = current[3]
        if name not in pieces:
            pieces[name] = [composer, key]
            print(f"{name} by {composer} in {key} added to the collection!")
        else:
            print(f"{name} is already in the collection!")
    elif action == "Remove":
        if name in pieces:
            del pieces[name]
            print(f"Successfully removed {name}!")
        else:
            print(f"Invalid operation! {name} does not exist in the collection.")
    elif action == "ChangeKey":
        new_key = current[2]
        if name in pieces:
            pieces[name][1] = new_key
            print(f"Changed the key of {name} to {new_key}!")
        else:
            print(f"Invalid operation! {name} does not exist in the collection.")
    command = input()

sorted_pieces = sorted(pieces.items(), key=lambda kvp: (kvp[0], kvp[1][0]))

for key, value in sorted_pieces:
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
