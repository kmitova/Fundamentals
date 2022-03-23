import re

pattern = r"(=|\/)([A-Z]{1}[A-Za-z]{2,})(\1)"

places = input()
found = []
matches = re.findall(pattern, places)
if matches:
    for match in matches:
        found.append(match[1])

total = 0
for item in found:
    total += len(item)

print(f"Destinations: {', '.join(found)}")
print(f"Travel Points: {total}")

