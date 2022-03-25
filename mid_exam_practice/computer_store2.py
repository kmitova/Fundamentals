price_no_tax = 0
while True:
    number = input()
    if number == "special" or number == "regular":
        break
    float_number = float(number)
    if float_number <= 0:
        print("Invalid price!")
    else:
        price_no_tax += float_number

if price_no_tax == 0:
    print("Invalid order!")

else:
    tax = 0.2 * price_no_tax
    price = price_no_tax + tax
    if number == "special":
        price = price - price * 0.1
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_no_tax:.2f}$")
    print(f"Taxes: {tax:.2f}$")
    print("-----------")
    print(f"Total price: {price:.2f}$")
