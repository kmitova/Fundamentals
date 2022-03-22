data = input().split()

bakery = {}

for index in range(0, len(data), 2):
    current_product = data[index]
    current_quantity = int(data[index+1])
    bakery[current_product] = current_quantity

print(bakery)
