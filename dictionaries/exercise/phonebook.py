data = input()
dictionary = {}
while "-" in data:
    current = data.split("-")
    name = current[0]
    number = current[1]
    dictionary[name] = number
    data = input()

n = int(data)

for i in range(n):
    name = input()
    if name in dictionary:
        print(f"{name} -> {dictionary[name]}")
    else:
        print(f"Contact {name} does not exist.")
