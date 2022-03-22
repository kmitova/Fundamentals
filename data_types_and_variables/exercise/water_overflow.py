capacity = 255
liters = 0

lines = int(input())

for line in range(lines):
    quantity = int(input())
    liters = liters + quantity
    if liters > capacity:
        print("Insufficient capacity!")
        liters = liters - quantity
        continue

print(liters)
