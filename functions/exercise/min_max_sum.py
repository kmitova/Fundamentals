def min_max_sum(numbers):
    print(f"The minimum number is {(min(numbers))}")
    print(f"The maximum number is {(max(numbers))}")
    print(f"The sum number is: {(sum(numbers))}")


numbers_sequence = input().split()
ints_numbers_sequence = [int(i) for i in numbers_sequence]
min_max_sum(ints_numbers_sequence)
