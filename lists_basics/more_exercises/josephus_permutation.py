numbers_sequence = input().split()
k = int(input())
result = []
counter = 0
index = 0

while(len(numbers_sequence)) > 0:
    counter += 1

    if counter % k == 0:
        result.append(numbers_sequence.pop(index))
    else:
        index += 1
    if index >= len(numbers_sequence):
        index = 0

print(str(result).replace(' ', '').replace('\'', ''))

