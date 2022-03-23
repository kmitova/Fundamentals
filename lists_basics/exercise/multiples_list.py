factor = int(input())
count = int(input())

multiples = []

for elem in range(1, count+1):
    multiple = elem*factor
    multiples.append(multiple)

print(multiples)
