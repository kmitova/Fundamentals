import re

string = input()

pattern = r"(=|\/)([A-Z]{1}[A-Za-z]{2,})(\1)"

matches = re.finditer(pattern, string)
destinations = []
points = 0
if matches:
    for match in matches:
        place = match.group(2)
        destinations.append(place)
        points += len(place)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {points}")
