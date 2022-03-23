lines = int(input())
positives = []
negatives = []
for line in range(lines):
    integer = int(input())
    if integer >= 0:
        positives.append(integer)
    else:
        negatives.append(integer)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)} Sum of negatives: {sum(negatives)}")