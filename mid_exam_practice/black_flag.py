days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

total_plunder = 0

for day in range(1, days+1):
    total_plunder += daily_plunder
    if day % 3 == 0:
        additional_plunder = daily_plunder / 2
        total_plunder += additional_plunder
    if day % 5 == 0:
        loss = total_plunder * 0.3
        total_plunder -= loss

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    diff = total_plunder / expected_plunder
    percent_diff = diff * 100
    print(f"Collected only {percent_diff:.2f}% of the plunder.")
