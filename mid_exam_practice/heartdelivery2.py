neighborhood = list(map(int, input().split("@")))

command = input()
start = 0
while not command == "Love!":
    current = command.split()
    length = int(current[1])
    house = start + length
    if house not in range(len(neighborhood)):
        house = 0
    if neighborhood[house] == 0:
        print(f"Place {house} already had Valentine's day.")
    else:
        neighborhood[house] -= 2
        if neighborhood[house] == 0:
            print(f"Place {house} has Valentine's day.")
    start = house

    command = input()

print(f"Cupid's last position was {house}.")
left_houses = [el for el in neighborhood if el != 0]
if len(left_houses) > 0:
    print(f"Cupid has failed {len(left_houses)} places.")
else:
    print("Mission was successful.")
