# def even_numbers(numbers):
#     only_evens = []
#     for number in numbers:
#         intnumber = int(number)
#         if intnumber % 2 == 0:
#             only_evens.append(intnumber)
#     return only_evens
#
#
# numbers_sequence = input().split()
# result = even_numbers(numbers_sequence)
# print(result)

#  using filter() function, works too
def even_numbers(numbers):
    return numbers % 2 == 0


numbers_sequence = input().split()
ints_numbers_sequence = [int(i) for i in numbers_sequence]
evens = list(filter(even_numbers, ints_numbers_sequence))
print(evens)
