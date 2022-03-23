def sort(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers


numbers_sequence = input().split()
ints_numbers_sequence = [int(i) for i in numbers_sequence]
result = sort(ints_numbers_sequence)
print(result)
