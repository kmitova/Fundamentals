import re

pattern = r"^@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+$"

count = int(input())
for i in range(count):
    text = input()
    matches = re.findall(pattern, text)
    # if matches:
    #     print(matches)
    if matches:
        for el in matches:
            code = el

            digits = ""
            for char in code:
                if char.isdigit():
                    digits += char
            if digits == "":
                print("Product group: 00")
            else:
                print(f"Product group: {digits}")
    else:
        print("Invalid barcode")

