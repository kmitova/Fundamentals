numbers_as_string = input().split(" ")
amount_to_remove = int(input())

numbers_as_ints = list(map(int, numbers_as_string))  # from strings to ints

for removal in range(amount_to_remove):
    numbers_as_ints.remove(min(numbers_as_ints))

print(", ".join(str(numbers_as_ints) for numbers_as_ints in numbers_as_ints))
