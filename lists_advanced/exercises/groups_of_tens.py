numbers = input().split(", ")
numbers = list(map(int, numbers))

boundary = 10

while len(numbers) > 0:
    result = list(filter(lambda x: x <= boundary, numbers))
    numbers = list(filter(lambda x: x > boundary, numbers))
    print(f"Group of {boundary}'s: {result}")
    boundary += 10
