food = (float(input()))*1000
hay = (float(input()))*1000
cover = (float(input()))*1000
guinea_pig_weight = float(input())*1000
days = 0
enough = False
while True:
    if food <= 0 or cover <= 0 or hay <= 0:
        break
    if days == 30:
        enough = True
        break
    days += 1
    food = food - 300
    if days % 2 == 0:
        needed_hay = food * 0.05
        hay = hay - needed_hay
    if days % 3 == 0:
        needed_cover = guinea_pig_weight / 3
        cover = cover - needed_cover


if enough:
    print(f"Everything is fine! Puppy is happy! Food: {food/1000:.2f}, Hay: {hay/1000:.2f}, Cover: {cover/1000:.2f}.")
else:
    print("Merry must go to the pet store!")
