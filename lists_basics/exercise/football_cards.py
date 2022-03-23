card = input()
lost = False
eliminated = card.split()
filtered = []

for elem in eliminated:  # removes repeating elements
    if elem not in filtered:
        filtered.append(elem)

a_team = 11
b_team = 11

for i in filtered:
    if i[0] == "A":
        a_team -= 1
    if i[0] == "B":
        b_team -= 1
    if a_team < 7 or b_team < 7:
        lost = True
        break

print(f"Team A - {a_team}; Team B - {b_team}")
if lost:
    print("Game was terminated")
