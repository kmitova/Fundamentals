import re

pattern = r"%([A-Z][a-z]+)%[^\|\$%\.]*<(\w+)>[^\|\$%\.]*\|(\d+)\|[^\|\$%\.\d]*(([0-9]+)(\.\d+)*)\$"
total = 0
current_total = 0
orders = {}
data = input()
while not data == "end of shift":
    matches = re.search(pattern, data)
    if matches:
        name = matches.group(1)
        item = matches.group(2)
        quantity = int(matches.group(3))
        price = float(matches.group(4))
        current_total = int(quantity) * float(price)
        print(f"{name}: {item} - {current_total:.2f}")
        total += current_total
    data = input()

print(f"Total income: {total:.2f}")
