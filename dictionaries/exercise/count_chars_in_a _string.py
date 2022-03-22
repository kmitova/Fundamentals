string = input()

string_list = [el for el in string]
string_dict = {}

for item in string_list:
    if not item == " ":
        if item not in string_dict:
            string_dict[item] = 1
        else:
            string_dict[item] += 1


for key, val in string_dict.items():
    print(f"{key} -> {val}")
