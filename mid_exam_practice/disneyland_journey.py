journey_cost = float(input())
months = int(input())
saved = 0
bonus = 0
for month in range(1, months+1):
    if month % 2 != 0 and month != 1:
        saved -= saved * 0.16
    if month % 4 == 0:
        bonus += saved * 0.25
    saved += journey_cost * 0.25


saved += bonus

if saved >= journey_cost:
    diff = saved - journey_cost
    print(f"you can go to disneyland and have {diff:.2f} lv for souvenirs")
else:
    diff = journey_cost - saved
    print(f"sorry, you need {diff:.2f} lv more")
