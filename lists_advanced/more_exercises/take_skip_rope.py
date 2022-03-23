initial_string = input()

numbers = [el for el in initial_string if el in "0123456789"]
non_numbers = [el for el in initial_string if el not in "0123456789"]

print(numbers)
print(non_numbers)

evens = [num for num in numbers if numbers.index(num) % 2 == 0]
odds = [num for num in numbers if not numbers.index(num) % 2 == 0]

result = []
skipped = []
reached_for_res = 0
reached_for_skip = 0
for i in evens:
    for j in odds:
        pass
