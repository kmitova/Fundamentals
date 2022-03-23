line_1 = input().split()
line_2 = input().split()
line_3 = input().split()

player_1_wins = False
player_2_wins = False
draw = True

for index1 in range(len(line_1)):
    for index2 in range(len(line_2)):
        for index3 in range(len(line_3)):
            if line_1[0] == "1" and line_1[1] == "1" and line_1[2] == "1":
                player_1_wins = True
                break
            elif line_2[0] == "1" and line_2[1] == "1" and line_2[2] == "1":
                player_1_wins = True
                break
            elif line_3[0] == "1" and line_3[1] == "1" and line_3[2] == "1":
                player_1_wins = True
                break
            elif line_1[0] == "1" and line_2[0] == "1" and line_3[0] == "1":
                player_1_wins = True
                break
            elif line_1[1] == "1" and line_2[1] == "1" and line_3[1] == "1":
                player_1_wins = True
                break
            elif line_1[2] == "1" and line_2[2] == "1" and line_3[2] == "1":
                player_1_wins = True
                break
            elif line_1[0] == "1" and line_2[1] == "1" and line_3[2] == "1":
                player_1_wins = True
                break
            elif line_1[2] == "1" and line_2[1] == "1" and line_3[0] == "1":
                player_1_wins = True
                break

            elif line_1[0] == "2" and line_1[1] == "2" and line_1[2] == "2":
                player_2_wins = True
                break
            elif line_2[0] == "2" and line_2[1] == "2" and line_2[2] == "2":
                player_2_wins = True
                break
            elif line_3[0] == "2" and line_3[1] == "2" and line_3[2] == "2":
                player_2_wins = True
                break
            elif line_1[0] == "2" and line_2[0] == "2" and line_3[0] == "2":
                player_2_wins = True
                break
            elif line_1[1] == "2" and line_2[1] == "2" and line_3[1] == "2":
                player_2_wins = True
                break
            elif line_1[2] == "2" and line_2[2] == "2" and line_3[2] == "2":
                player_2_wins = True
                break
            elif line_1[0] == "2" and line_2[1] == "2" and line_3[2] == "2":
                player_2_wins = True
                break
            elif line_1[2] == "2" and line_2[1] == "2" and line_3[0] == "2":
                player_2_wins = True
                break
        if player_1_wins:
            break
        if player_2_wins:
            break
    if player_1_wins:
        draw = False
        break
    if player_2_wins:
        draw = False
        break

if player_1_wins:
    print("First player won")
if player_2_wins:
    print("Second player won")
if draw:
    print("Draw!")
