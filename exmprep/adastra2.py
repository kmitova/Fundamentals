import re

pattern = r"(#|\|)([A-Za-z]+( *[A-Za-z]+)*)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d{1,})(\1)"
data = input()
calories = 0
# items = {}
items = []
matches = re.finditer(pattern, data)
if matches:
    for match in matches:
        if not 0 <= int(match.group(7)) > 10000:

            calories += int(match.group(7))
            # items[match.group(2)] = [match.group(4), match.group(6)]
            items.append(match.group(2))
            items.append(match.group(5))
            items.append(match.group(7))
days = calories // 2000
# print(items)
print(f"You have food to last you for: {days} days!")
# for item, info in items.items():
#     print(f"Item: {item}, Best before: {info[0]}, Nutrition: {info[1]}")
if len(items) > 0:
    for ind in range(0, len(items), 3):
        print(f"Item: {items[ind]}, Best before: {items[ind+1]}, Nutrition: {items[ind+2]}")

