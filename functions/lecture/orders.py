def total_price(product, quantity):
    price = 0
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1.00
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2.00
    return price*quantity


given_product = input()
given_quantity = int(input())
result = total_price(given_product, given_quantity)
print(f"{result:.2f}")
