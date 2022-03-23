import re

pattern = r"^!([A-Z{1}][a-z]{2,})!:\[(.{8,})\]"
lines = int(input())
for line in range(lines):
    text = input()
    match = re.findall(pattern, text)
    if match:
        for el in match:
            command = el[0]
            message = el[1]
            encrypted = ""
            for char in message:
                encrypted += str(ord(char)) + " "
            print(f"{command}: {encrypted.rstrip()}")
    else:
        print("The message is invalid")
