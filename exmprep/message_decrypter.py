import re

pattern = r"^(\$|%)([A-Z]{1}[a-z]{2,})(\1): \[(\d+)]\|\[(\d+)]\|\[(\d+)]\|$"
lines = int(input())

for line in range(lines):
    text = input()
    tag = ""
    num1 = 0
    num2 = 0
    num3 = 0
    matches = re.findall(pattern, text)
    if matches:
        for element in matches:
            tag = element[1]
            num1 = int(element[3])
            num2 = int(element[4])
            num3 = int(element[5])
        print(f"{tag}:{chr(num1)}{chr(num2)}{chr(num3)}")
    else:
        print("Valid message not found!")
