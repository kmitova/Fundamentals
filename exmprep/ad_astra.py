import re
from math import floor

pattern = r"(\||#)([A-Za-z]+(\s[A-Za-z]*)*)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d{1,10000})(\1)"
text = input()

food = []
total_cals = []
matches = re.findall(pattern, text)
if matches:
    for el in matches:
        item = el[1]
        food.append(item)
        date = el[4]
        food.append(date)
        calories = el[6]
        food.append(calories)
        total_cals.append(int(calories))

food_for_days = floor(sum(total_cals) / 2000)
print(f"You have food to last you for: {food_for_days} days!")
if len(food) > 0:
    for ind in range(0, len(food), 3):
        print(f"Item: {food[ind]}, Best before: {food[ind+1]}, Nutrition: {food[ind+2]}")

