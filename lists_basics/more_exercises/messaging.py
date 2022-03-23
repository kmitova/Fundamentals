#  100/100 but don't know how to make i go the beginning of sum of digits is greater than last index

numbers_sequence = input().split()
string = input()
message = []
sums_of_ind_digits = []
for number in numbers_sequence:
    individual_numbers = number.split()
    for ind_number in individual_numbers:
        sum_of_ind_number = 0
        for ind_digit in ind_number:
            sum_of_ind_number += int(ind_digit)
        sums_of_ind_digits.append(sum_of_ind_number)

ind_chars = []
for char in string:
    ind_chars.append(char)
go_back = False
last_char_index = len(ind_chars)
for index_of_char in range(len(ind_chars)):
    for sum_of_digits in sums_of_ind_digits:
        # if sum_of_digits > last_char_index:
        #     go_back = True
        #     continue
        if index_of_char == int(sum_of_digits):
            message.append(ind_chars[index_of_char])
            ind_chars.remove(ind_chars[index_of_char])
    # if sum_of_digits > len(ind_chars):
    #     index_of_char = 0
    # if go_back:
    #     continue

final_message = ("".join(message))
print(final_message)

