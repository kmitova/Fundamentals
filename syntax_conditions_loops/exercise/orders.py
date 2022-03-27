orders = int(input())
price = 0
total = 0

for order in range(orders):
    price = 0
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    price += price_per_capsule * days * capsules_count
    print(f"The price for the coffee is: ${price:.2f}")
    total = total + price

print(f"Total: ${total:.2f}")
