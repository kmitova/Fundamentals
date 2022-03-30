import re

string = input()
pattern = r"(\||#)([A-Z a-z]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d{1,4})(\1)"

matches = re.finditer(pattern, string)
calories_total = 0
food = []
if matches:
    for match in matches:
        item = match.group(2)
        date = match.group(4)
        calories = int(match.group(6))
        food.append(item)
        food.append(date)
        food.append(calories)
        calories_total += calories

days = int(calories_total / 2000)
print(f"You have food to last you for: {days} days!")

if len(food) > 0:
    for i in range(0, len(food), 3):
        print(f"Item: {food[i]}, Best before: {food[i+1]}, Nutrition: {food[i+2]}")
