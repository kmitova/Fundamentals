def absolute_values(given_sequence):
    abs_numbers_sequence = []
    for value in given_sequence:
        abs_numbers_sequence.append(abs(float(value)))
    return abs_numbers_sequence


numbers_sequence = input().split()

result = absolute_values(numbers_sequence)
print(result)

# with print instead of return:

# def absolute_values(given_sequence):
#     abs_numbers_sequence = []
#     for value in given_sequence:
#         abs_numbers_sequence.append(abs(float(value)))
#     print(abs_numbers_sequence)
#
#
# numbers_sequence = input().split()
#
# absolute_values(numbers_sequence)