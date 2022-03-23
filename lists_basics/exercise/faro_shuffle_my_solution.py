string = input().split()
length = len(string)
shuffles = int(input())
half_1 = string[:length//2]
half_2 = string[length//2:]

zipped = []
unzipped = []
flat_unzipped = []
for i in range(shuffles):
    zipped = zip(half_1, half_2)
    unzipped = [item for item in list(zipped)]
    flat_unzipped = [item for sublist in unzipped for item in sublist]
    unzipped.clear()
    half_1 = flat_unzipped[:length // 2]
    half_2 = flat_unzipped[length // 2:]
    if i < shuffles - 1:
        flat_unzipped.clear()

print(flat_unzipped)
