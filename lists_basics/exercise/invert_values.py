string = input()

string_list = string.split(" ")

new_list = []
for element in string_list:
    number_element = int(element)
    number_element = -number_element
    new_list.append(number_element)
print(new_list)
