days = int(input())
players = int(input())
energy = float(input())
water_per_day_one_person = float(input())
food_per_day_one_person = float(input())
water_per_day = water_per_day_one_person * players
food_per_day = food_per_day_one_person * players
water = water_per_day * days
food = food_per_day * days
food_reduction = 0
no_energy_left = 0

for day in range(1, days+1):
    energy_lost = float(input())
    energy -= energy_lost

    if energy <= 0:
        no_energy_left = True
        break
    if day % 2 == 0:
        energy += energy * 0.05
        water -= water * 0.3
    if day % 3 == 0:
        energy += energy * 0.1
        food_reduction = food / players
        food -= food_reduction

if no_energy_left:
    print(f"you will run out of energy. you will be left with {food:.2f} food and {water:.2f} water")
else:
    print(f"you are ready for the quest. you will be left with {energy:.2f} energy!")
