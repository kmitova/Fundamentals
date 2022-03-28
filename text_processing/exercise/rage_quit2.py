data = input().upper()
index = 0
message = ""
final_message = ""
current_string = ""
while index < len(data):

    if not data[index].isdigit():
        current_string += data[index]
        index += 1
    else:
        current_num = ""
        while data[index].isdigit():
            current_num += data[index]
            index += 1
            if index == len(data):
                break
        current_num = int(current_num)
        message = (current_num * current_string)
        final_message += message
        current_string = ""
unique = []

for el in final_message:
    if el not in unique:
        unique.append(el)
print(f"Unique symbols used: {len(unique)}")
print(final_message)

