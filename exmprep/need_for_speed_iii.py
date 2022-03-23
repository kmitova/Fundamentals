num = int(input())

cars = {}

for i in range(num):
    info = input()
    current = info.split("|")
    car = current[0]
    mileage = int(current[1])
    fuel = int(current[2])
    cars[car] = [mileage, fuel]

command = input()
while not command == "Stop":
    current = command.split(" : ")
    car = current[1]
    action = current[0]
    if action == "Drive":
        distance = int(current[2])
        fuel = int(current[3])
        if cars[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car][0] += distance
            cars[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            del cars[car]
    elif action == "Refuel":
        fuel = int(current[2])
        old = cars[car][1]
        cars[car][1] += fuel
        if cars[car][1] > 75:
            diff = 75 - old
            cars[car][1] = 75
            print(f"{car} refueled with {diff} liters")
        else:
            print(f"{car} refueled with {fuel} liters")
    elif action == "Revert":
        kilometers = int(current[2])
        cars[car][0] -= kilometers
        if cars[car][0] >= 10000:
            print(f"{car} mileage decreased by {kilometers} kilometers")
        else:
            cars[car][0] = 10000

    command = input()

sorted_cars = sorted(cars.items(), key=lambda kvp: (-kvp[1][0], kvp[0]))

for key, value in sorted_cars:
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")
