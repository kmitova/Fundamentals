data = input()
dictionary = {}
while not data == "End":
    company, id = data.split(" -> ")
    if company not in dictionary:
        dictionary[company] = [id]

    dictionary[company].append(id)

    data = input()

for k, v in dictionary.items():
    filtered = []
    for i in v:
        if i not in filtered:
            filtered.append(i)
    dictionary[k] = filtered


for k, v in dictionary.items():
    print(f"{k}")
    for item in v:
        print(f"-- {item}")
