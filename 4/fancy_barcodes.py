import re

pattern = r"^@#+([A-Z]{1}[A-Za-z0-9]{4,}[A-Z]{1})@#+$"
num = int(input())

for n in range(num):
    string = input()
    matches = re.findall(pattern, string)
    if matches:
        for match in matches:
            digits = ""
            for i in match:
                if i.isdigit():
                    digits += i
            if digits == "":
                print("Product group: 00")
            else:
                print(f"Product group: {digits}")
    else:
        print("Invalid barcode")
