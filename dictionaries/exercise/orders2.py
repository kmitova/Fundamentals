def orders_program():
    orders = {}
    command = input()
    while not command == "buy":
        current = command.split()
        item = current[0]
        quantity = int(current[2])
        price = float(current[1])
        if item not in orders:
            orders[item] = [quantity, price]
        else:
            orders[item][0] += quantity
            orders[item][1] = price
        command = input()

    for item, info in orders.items():

        print(f"{item} -> {info[0]* info[1]:.2f}")


orders_program()
