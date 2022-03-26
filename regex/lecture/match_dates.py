import re

pattern = r"(\d{2})(\.|-|\/)([A-Z][a-z]{2})(\2)(\d{4})"

text = input()
matches = re.finditer(pattern, text)

for match in matches:
    day = match.group(1)
    month = match.group(3)
    year = match.group(5)
    print(f"Day: {day}, Month: {month}, Year: {year}")
