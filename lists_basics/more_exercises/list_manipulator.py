# # works for some conditions; cannot understand how to formulate output
#
# numbers_sequence = input().split()
# empty_list = []
# command = input()
# list_to_use = numbers_sequence.copy()
# while not command == "end":
#     manipulation_command = command
#     current_manipulation_command = manipulation_command.split()
#     action = current_manipulation_command[0]
#     value_of_action = current_manipulation_command[1]
#
#     if action == "exchange":
#         if int(value_of_action) > len(numbers_sequence) or int(value_of_action) < 0:
#             print("Invalid index")
#         else:
#             left_half = numbers_sequence[0:int(value_of_action)+1]
#             right_half = numbers_sequence[int(value_of_action)+1::]
#             right_half += left_half
#             numbers_sequence = right_half
#     elif action == "max":
#         if value_of_action == "even":
#             list_to_use.sort(reverse=True)
#             for elem in list_to_use:
#                 if int(elem) % 2 == 0:
#                     print(numbers_sequence.index(elem))
#                     break
#             else:
#                 print("No matches")
#                 break
#         elif value_of_action == "odd":
#             list_to_use.sort(reverse=True)
#             for elem in list_to_use:
#                 if not int(elem) % 2 == 0:
#                     print(numbers_sequence.index(elem))
#                     break
#             else:
#                 print("No matches")
#                 break
#     elif action == "min":
#         if value_of_action == "even":
#             list_to_use.sort()
#             for elem in list_to_use:
#                 if int(elem) % 2 == 0:
#                     print(numbers_sequence.index(elem))
#                     break
#             else:
#                 print("No matches")
#                 break
#         elif value_of_action == "odd":
#             list_to_use.sort()
#             for elem in list_to_use:
#                 if not int(elem) % 2 == 0:
#                     print(numbers_sequence.index(elem))
#                     break
#             else:
#                 print("No matches")
#                 break
#     elif action == "first":
#         if int(value_of_action) > len(numbers_sequence):
#             print("Invalid count")
#         elif current_manipulation_command[-1] == "even":
#             first_evens = []
#             for ind in range(len(numbers_sequence)):
#                 if int(numbers_sequence[ind]) % 2 == 0:
#                     first_evens.append(int(numbers_sequence[ind]))
#                     if int(value_of_action) == first_evens:
#                         break
#             print(first_evens)
#         elif current_manipulation_command[-1] == "odd":
#             first_odds = []
#             for ind in range(len(numbers_sequence)):
#                 if not int(numbers_sequence[ind]) % 2 == 0:
#                     first_odds.append(int(numbers_sequence[ind]))
#                     if int(value_of_action) == first_odds:
#                         break
#             print(f"[{first_odds}]")
#         else:
#             print(empty_list)
#     elif action == "last":
#         if int(value_of_action) > len(numbers_sequence):
#             print("Invalid count")
#         elif current_manipulation_command[-1] == "even":
#             last_evens = []
#             for ind in range(len(numbers_sequence)-1, -1, -1):
#                 if int(numbers_sequence[ind]) % 2 == 0:
#                     last_evens.append(int(numbers_sequence[ind]))
#                     if int(value_of_action) == last_evens:
#                         break
#             last_evens.reverse()
#             print(last_evens)
#         elif current_manipulation_command[-1] == "odd":
#             last_odds = []
#             for ind in range(len(numbers_sequence)-1, -1, -1):
#                 if not int(numbers_sequence[ind]) % 2 == 0:
#                     last_odds.append(int(numbers_sequence[ind]))
#                     if int(value_of_action) == last_odds:
#                         break
#             last_odds.reverse()
#             print(last_odds)
#         else:
#             print(empty_list)
#     command = input()


# solving using functions
def exchange(nums_list, index):
    first_part = nums_list[index+1:]
    second_part = nums_list[:index+1]
    result = first_part + second_part
    return result


def find_max_num(nums_list, odd_or_even):
    filtered_nums = []
    if odd_or_even == "odd":
        for el in nums_list:
            if not el % 2 == 0:
                filtered_nums.append(el)
    else:
        for el in nums_list:
            if el % 2 == 0:
                filtered_nums.append(el)

    if not filtered_nums:
        return "No matches"
    max_element = max(filtered_nums)
    index = len(filtered_nums) - filtered_nums[::-1].index(filtered_nums) - 1
    return index


def find_min_num(nums_list, odd_or_even):
    filtered_nums = []
    if odd_or_even == "odd":
        for el in nums_list:
            if not el % 2 == 0:
                filtered_nums.append(el)
    else:
        for el in nums_list:
            if el % 2 == 0:
                filtered_nums.append(el)

    if not filtered_nums:
        return "No matches"
    min_element = min(filtered_nums)
    index = len(filtered_nums) - filtered_nums[::-1].index(filtered_nums) - 1
    return index


def find_first(nums_list, odd_or_even, count):
    filtered_nums = []
    if odd_or_even == "odd":
        for el in nums_list:
            if not el % 2 == 0:
                filtered_nums.append(el)
    else:
        for el in nums_list:
            if el % 2 == 0:
                filtered_nums.append(el)
    if len(filtered_nums) < count:
        return "Invalid count"

    return filtered_nums[:count]


def find_last(nums_list, odd_or_even, count):
    filtered_nums = []
    if odd_or_even == "odd":
        for el in nums_list:
            if not el % 2 == 0:
                filtered_nums.append(el)
    else:
        for el in nums_list:
            if el % 2 == 0:
                filtered_nums.append(el)
    if len(filtered_nums) < count:
        return "Invalid count"

    return filtered_nums[:count]

nums_as_string = input().split()
nums = []

for el in nums_as_string:
    nums.append(int(el))

command_data = input()

while not command_data == "end":
    command_data = command_data.split()
    command = command_data[0]
    if command == "exchange":
        i = int(command_data[1])
        nums = exchange(nums, i)
    elif command == "max":
        odd_or_even = command_data[1]
        print(find_max_num(nums, odd_or_even))
    elif command == "min":
        odd_or_even = command_data[1]
        print(find_min_num(nums, odd_or_even))
    elif command == "first":
        odd_or_even = command_data[2]
        count = int(command_data[1])
        print(find_first(nums, odd_or_even, count))
    elif command == "last":
        odd_or_even = command_data[2]
        count = int(command_data[1])
        print(find_last(nums, odd_or_even, count))

    command_data = input()
