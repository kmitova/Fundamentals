import re

pattern = r"^(.+)>(\d+)\|([a-z]+)\|([A-Z]+)\|([^<>]+)<(\1)$"

lines = int(input())
for line in range(lines):
    text = input()
    matches = re.findall(pattern, text)
    password = ""
    if matches:
        for el in matches:
            group1 = el[1]
            group2 = el[2]
            group3 = el[3]
            group4 = el[4]
            password = group1 + group2 + group3 + group4
        print(f"Password: {password}")
    else:
        print("Try another password!")
