rooms = int(input())
free_chairs_left = True
free_chairs_available = 0
for room in range(1, rooms + 1):
    data = input().split()
    free_chairs = data[0]
    visitors = int(data[1])
    if len(free_chairs) >= visitors:
        free_chairs_available += len(free_chairs) - visitors
        continue
    else:
        free_chairs_left = False
        needed = visitors - len(free_chairs)
        print(f"{needed} more chairs needed in room {room}")

if free_chairs_left:
    print(f"Game On, {free_chairs_available} free chairs left")
