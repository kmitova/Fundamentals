# usernames = input().split(", ")
# valid = []
# is_valid = True
# for name in usernames:
#     if len(name) in range(3, 17):
#         if " " not in name:
#             valid.append(name)
#
#
# final = []
# for item in valid:
#     is_valid = False
#     for char in item:
#         if char.isalnum() or char == "-" or char == "_":
#             is_valid = True
#         else:
#             is_valid = False
#             break
#     if is_valid:
#         final.append(item)
#
#
# for item in final:
#     print(item)

# another way:

def length_username(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def type_of_symbols(username):
    for char in username:
        if not(char.isalnum() or char == "-" or char == "_"):
            return False
    return True


def redundant_spaces(username):
    for char in username:
        if char == " ":
            return False
    return True


def username_is_valid(username):
    if length_username(username) and type_of_symbols(username) and redundant_spaces(username):
        return True


usernames = input().split(", ")

for name in usernames:
    if username_is_valid(name):
        print(name)
