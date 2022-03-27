# starting_word = input()
# aim_mutated_word = input()
#
# result = ""
# previous_str = starting_word
#
# for index in range(len(starting_word)):
#     for i in range(index + 1):
#         result += aim_mutated_word[i]
#     for i in range(index + 1, len(aim_mutated_word)):
#         result += starting_word[i]
#     if not result == previous_str:
#         print(result)
#     previous_str = result
#     result = ""

# another way:

first_word = input()
second_word = input()

for i in range(len(first_word)):
    if first_word[i] != second_word[i]:  # in order not to repeat outputs
        replacement = second_word[i]
        word = first_word[0:i] + replacement + first_word[i+1:]
        first_word = word  # need to use the current condition of the
        # word not to start from the beginning
        print(first_word)
