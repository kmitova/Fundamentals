targets = list(map(int, input().split("|")))
points = 0
command = input()
needed_index = 0

while not command == "Game over":
    data = command.split()
    current_command = data[0]

    if current_command[0] == "Shoot":
        direction, start_index, length = data[1].split("@")
        start_index = int(start_index)
        length = int(length)
        if start_index in range(0, len(targets)):

            if direction == "Left":
                needed_index = (start_index - length) % len(targets)

            elif direction == "Right":
                needed_index = (start_index + length) % len(targets)

            if targets[needed_index] < 5:
                points += targets[needed_index]
                targets[needed_index] = 0
            else:
                points += 5
                targets[needed_index] -= 5
    elif current_command[0] == "Reverse":
        targets.reverse()

    command = input()

print(" - ".join(map(str, targets)))

print(f"Iskren finished the archery tournament with {points} points!")
