import re

pattern = r"(#|\$|%|\*|&)([A-Za-z]+)(\1)=(\d+)!!([\s\S]*)"
no_match = False

while True:
    text = input()
    matches = re.findall(pattern, text)
    name = ""
    code = 0
    message = ""
    valid_name = True
    valid_code = True
    decrypted = ""
    if matches:
        # print(matches)
        for el in matches:
            name = el[1]
            code = int(el[3])
            message = el[4]
        # print(name, code, message)
        for char in name:
            if not char.isalpha():
                valid_name = False
                break
        for num in str(code):
            if not num.isdigit():
                valid_code = False
                break
        if valid_name and valid_code:
            if len(message) == code:
                for char in message:
                    decrypted += chr(ord(char) + code)
                print(f"Coordinates found! {name} -> {decrypted}")
                break
            else:
                no_match = True
        else:
            no_match = True
    else:
        no_match = True

    if no_match:
        print("Nothing found!")
