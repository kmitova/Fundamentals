numbers = input().split(",")

zeroes = []
zeroes_to_back = []
for number in numbers:
    if int(number) == 0:
        zeroes.append(number)

for number in numbers:
    if not int(number) == 0:
        zeroes_to_back.append(number)

zeroes_to_back.extend(zeroes)

zeroes_to_back = list(map(int, zeroes_to_back))
print(zeroes_to_back)
