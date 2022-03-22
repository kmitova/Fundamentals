party_size = int(input())
days = int(input())
earned = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        party_size = party_size - 2
    if day % 15 == 0:
        party_size += 5
    earned = earned + 50
    earned = earned - 2 * party_size
    if day % 3 == 0:
        earned -= 3 * party_size
    if day % 5 == 0:
        earned += 20 * party_size
    if day % 3 == 0 and day % 5 == 0:
        earned -= 2 * party_size

coins_each = int(earned / party_size)

print(f"{party_size} companions received {coins_each} coins each.")
