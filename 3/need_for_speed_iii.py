n = int(input())

cars = {}

for i in range(n):
    info = input().split("|")
    car = info[0]
    mileage = int(info[1])
    fuel = int(info[2])
    cars[car] = [mileage, fuel]

command = input()
while not command == "Stop":
    current = command.split(" : ")
    action = current[0]
    car = current[1]
    if action == "Drive":
        distance = int(current[2])
        fuel = int(current[3])
        if fuel > cars[car][1]:
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
        old_fuel = cars[car][1]
        cars[car][1] += fuel
        if cars[car][1] > 75:
            cars[car][1] = 75
            diff = 75 - old_fuel
            print(f"{car} refueled with {diff} liters")
        else:
            print(f"{car} refueled with {fuel} liters")
    elif action == "Revert":
        kms = int(current[2])
        cars[car][0] -= kms
        if cars[car][0] < 10000:
            cars[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kms} kilometers")

    command = input()

for key, value in cars.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")
