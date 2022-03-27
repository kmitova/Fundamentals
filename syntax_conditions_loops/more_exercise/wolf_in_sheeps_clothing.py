animals = input().split(", ")
animals.reverse()


for i in range(len(animals)):
    if animals[0] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    elif animals[i] == "wolf":
        print(f"Oi! Sheep number {i}! You are about to be eaten by a wolf!")
