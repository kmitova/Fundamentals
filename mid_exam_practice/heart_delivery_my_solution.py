neighborhood = list(map(int, input().split("@")))
house = 0
command = input()
house_index = 0
previous_house = 0

while not command == "Love!":
    current_house = command.split()
    jump_length = int(current_house[1])
    house += jump_length
    if house not in range(len(neighborhood)):
        house = 0
    if neighborhood[house] <= 0:
        print(f"Place {house} already had Valentine's day.")
    else:
        neighborhood[house] -= 2
        if neighborhood[house] <= 0:
            print(f"Place {house} has Valentine's day.")
    command = input()

print(f"Cupid's last position was {house}.")

not_zeroes = [x for x in neighborhood if x > 0]

if len(not_zeroes) > 0:
    print(f"Cupid has failed {len(not_zeroes)} places.")
else:
    print("Mission was successful.")
