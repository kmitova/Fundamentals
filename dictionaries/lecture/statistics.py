data = input()
dict = {}

while not data == "statistics":
    current = data.split(":")
    product = current[0]
    quantity = int(current[1])
    if product not in dict:
        dict[product] = quantity

    else:
        dict[product] += quantity
    data = input()


print("Products in stock:")
for key, value in dict.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(dict.keys())}")
print(f"Total Quantity: {sum(dict.values())}")
