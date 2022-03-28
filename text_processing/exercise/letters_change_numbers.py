alphabet = {chr(96 + num): num for num in range(1, 27)}
data = input().split()
sums_list = []
for el in data:
    first_letter = el[0]
    last_letter = el[-1]
    number = int(el[1:-1])
    total_sum = 0
    if first_letter.isupper():
        first_letter = first_letter.lower()
        total_sum += number / alphabet[first_letter]
    elif first_letter.islower():
        total_sum += number * alphabet[first_letter]
    if last_letter.isupper():
        last_letter = last_letter.lower()
        total_sum -= alphabet[last_letter]
    elif last_letter.islower():
        total_sum += alphabet[last_letter]
    sums_list.append(total_sum)

print(f"{sum(sums_list):.2f}")
