
coffees = 0
need_sleep = False

while True:
    command = input()
    if command == "END":
        break
    if not command == "cat" and not command == "CAT" and not command == "dog" \
            and not command == "DOG" and not command == "coding" \
            and not command == "CODING" and not command == "movie" and not command == "MOVIE":
        continue
    else:
        if command.islower():
            coffees += 1
        else:
            coffees += 2
    if coffees > 5:
        need_sleep = True
        break

if need_sleep:
    print("You need extra sleep")
else:
    print(coffees)
