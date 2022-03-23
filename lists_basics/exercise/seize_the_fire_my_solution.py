fire_cells = input().split("#")
water = int(input())
effort = 0
put_fires = []
fire = 0
for cell in fire_cells:
    values = cell.split(" = ")
    type_fire = values[0]
    range_fire = int(values[1])
    if water < range_fire:
        continue
    if type_fire == "High" and 81 <= range_fire <= 125:
        water -= range_fire

    elif type_fire == "Medium" and 51 <= range_fire <= 80:
        water -= range_fire
    elif type_fire == "Low" and 1 <= range_fire <= 50:
        water -= range_fire
    else:
        continue
    put_fires.append(range_fire)
    effort += range_fire * 0.25
    fire += range_fire

print("Cells:")
for item in put_fires:
    print(f" - {item}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {fire}")

