pieces = int(input())

music = {}

for item in range(pieces):
    data = input()
    current = data.split("|")
    piece = current[0]
    composer = current[1]
    key = current[2]
    music[piece] = [composer, key]

command = input()
while not command == "Stop":
    current = command.split("|")
    action = current[0]
    piece = current[1]
    if action == "Add":
        composer = current[2]
        key = current[3]
        if piece in music:
            print(f"{piece} is already in the collection!")
        else:
            music[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif action == "Remove":
        if piece in music:
            del music[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif action == "ChangeKey":
        new_key = current[2]
        if piece in music:
            music[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()

for key, value in music.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
