data = input()
dictionary = {}
while not data == "buy":
    current = data.split()
    name = current[0]
    price = float(current[1])
    quantity = int(current[2])
    if name not in dictionary:
        dictionary[name] = {"price": price, "quantity": quantity}
    else:
        dictionary[name]["price"] = price
        dictionary[name]["quantity"] += quantity

    data = input()

for key, value in dictionary.items():
    result = value["price"] * value["quantity"]
    print(f"{key} -> {result:.2f}")
