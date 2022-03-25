total_price = 0
price = 0
while True:
    command = input()
    if command == "regular" or command == "special":
        break
    price = float(command)
    if price <= 0:
        print("Invalid price!")
        continue
    total_price += price

if total_price == 0:
    print("Invalid order!")
else:
    taxes = total_price * 0.2
    price_with_taxes = total_price + taxes

    if command == "special":
        price_with_taxes = price_with_taxes - price_with_taxes * 0.1

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {price_with_taxes:.2f}$")

