data = input()
lines = 0
dictionary = {}

while not data == "stop":
    lines += 1
    if not lines % 2 == 0:
        resource = data
        if resource not in dictionary:
            dictionary[resource] = 0
    else:
        quantity = int(data)
        if dictionary[previous_resource] == 0:
            dictionary[previous_resource] = quantity
        else:
            dictionary[previous_resource] += quantity
    previous_resource = resource
    data = input()

for key, val in dictionary.items():
    print(f"{key} -> {val}")
