import re

pattern = r"^>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)$"

total = 0
bought = []

data = input()
while not data == "Purchase":
    match = re.search(pattern, data)
    if match:
        furniture, price, quantity = match.groups()
        total += float(price) * int(quantity)
        bought.append(furniture)

    data = input()

print("Bought furniture:")
for item in bought:
    print(item)

print(f"Total money spend: {total:.2f}")
