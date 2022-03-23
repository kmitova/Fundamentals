a_team = 11
b_team = 11

red_cards = input().split()

filtered = []
terminated = False
for card in red_cards:
    if card not in filtered:
        filtered.append(card)

for card in filtered:
    if card[0] == "A":
        a_team -= 1
    elif card[0] == "B":
        b_team -= 1
    if a_team < 7 or b_team < 7:
        terminated = True
        break
print(f"Team A - {a_team}; Team B - {b_team}")
if terminated:
    print("Game was terminated")
