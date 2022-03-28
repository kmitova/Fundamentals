keys = list(map(str, input().split()))
messages = []

text = input()
while not text == "find":
    message = []
    text_list = [el for el in text]
    start = 0
    while len(text_list) > 0:
        for ind in range(start, len(keys)):
            key = keys[ind]
            break
        for char in text_list:
            new_symbol = ord(char) - int(keys[ind])
            message.append(chr(new_symbol))
            text_list.remove(char)
            break
        start += 1

        if start >= len(keys):
            start = 0
    message = "".join(message)
    messages.append(message)
    text = input()

new_messages = []
for message in messages:
    new_message = message.replace("&", "`", 1)
    new_messages.append(new_message)

types = []
coordinates_list = []
for message in new_messages:
    index_of_ampersand2 = 0
    index_of_ampersand1 = 0
    count = 0
    for ind in range(len(message)):
        typee = ""
        coordinates = ""

        if message[ind] == "`":

            next_el = ind+1
            while not message[next_el] == "&":
                typee += message[next_el]
                next_el += 1
            types.append(typee)

        if message[ind] == "<":

            next_el = ind + 1
            while not message[next_el] == ">":
                coordinates += message[next_el]
                next_el += 1
            coordinates_list.append(coordinates)

for material in types:
    for nums in coordinates_list:
        print(f"Found {material} at {nums}")
        coordinates_list.remove(nums)
        break
