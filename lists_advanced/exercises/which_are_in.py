string_1 = input().split(", ")
string_2 = input().split(", ")

to_check = "".join(string_2)
#  without list comprehension
# final_list = []
# for item in string_1:
#     if item in to_check:
#         final_list.append(item)
#
# print(final_list)

final_list = [item for item in string_1 if item in to_check]
print(final_list)