items_with_prices = input().split("|")
budget = float(input())
initial_budget = budget
prices = []
for item in items_with_prices:
    current_item = item.split("->")
    item_type = current_item[0]
    item_price = float(current_item[1])

    if item_type == "Clothes":
        if item_price > 50:
            continue
    elif item_type == "Shoes":
        if item_price > 35:
            continue
    elif item_type == "Accessories":
        if item_price > 20.5:
            continue
    if item_price > budget:
        continue
    budget -= item_price
    prices.append(item_price)

new_prices = []

for elem in prices:
    num_elem = float(elem)
    num_elem += num_elem * 0.4
    new_prices.append(num_elem)
    print(f"{num_elem:.2f}", end=" ")

profit = sum(new_prices) - sum(prices)
print()
print(f"Profit: {profit:.2f}")

needed = budget + sum(new_prices)
if needed >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
