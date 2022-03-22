data = input().split()
available = {}
to_search_for = input().split()

for index in range(0, len(data), 2):
    current_product = data[index]
    current_quantity = int(data[index + 1])
    available[current_product] = current_quantity

for item in to_search_for:
    if item in available.keys():
        print(f"We have {available[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
