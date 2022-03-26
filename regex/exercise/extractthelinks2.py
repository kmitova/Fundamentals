import re

pattern = r"(www\.([A-Za-z0-9-]+)\.([a-z]+)((\.[a-z]+)*))"

data = input()
while data:
    matches = re.findall(pattern, data)
    if matches:
        for el in matches:
            print(el[0])
    data = input()
