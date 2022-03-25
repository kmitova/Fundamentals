a = 5
elements = input().split()
command = input()
moves = 0
result = 0
won = False
while not command == "end":
    indices = command.split()
    i_1 = int(indices[0])
    i_2 = int(indices[1])
    moves += 1
    if i_1 == i_2 or (i_1 not in range(len(elements)) or i_2 not in range(len(elements))):
        middle = len(elements) // 2
        elements.insert(middle, f"-{moves}a")
        elements.insert(middle + 1, f"-{moves}a")
        print(f"Invalid input! Adding additional elements to the board")
    elif elements[i_1] == elements[i_2]:
        matching_el = elements[i_1]
        elements = [x for x in elements if not x == matching_el]
        print(f"Congrats! You have found matching elements - {matching_el}!")

        if len(elements) == 0:
            print(f"You have won in {moves} turns!")
            won = True
    else:
        print("Try again!")
    if won:
        break
    command = input()


if not won:
    print("Sorry you lose :(")
    for el in elements:
        print(el, end=" ")
