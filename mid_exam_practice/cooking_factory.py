from sys import maxsize

command = input()
sum_quality = 0
average_quality = 0
max_sum_quality = 0
with_same_quality = 0
lists_with_same_quality = []
max_average_quality = 0
lists_with_same_av_quality = []
min_length = maxsize
result = []

while not command == "Bake It!":
    sequence = list(map(int, command.split("#")))
    sum_quality = sum(sequence)
    if sum_quality > max_sum_quality:
        previous_quality = max_sum_quality
        max_sum_quality = sum_quality
        result = sequence
        if previous_quality == max_sum_quality:
            with_same_quality += 1
            lists_with_same_quality.append(sequence)
    command = input()

if len(lists_with_same_quality) > 1:
    for item in lists_with_same_quality:
        average_quality = sum(item) / len(item)
        if average_quality > max_average_quality:
            max_average_quality = average_quality
            lists_with_same_av_quality.append(item)
            result = item

if len(lists_with_same_av_quality) > 1:
    for item in lists_with_same_av_quality:
        if sum(item) < min_length:
            min_length = sum(item)
            result = item

print(f"Best batch quality: {max_sum_quality}")
print(" ".join(map(str, result)))
