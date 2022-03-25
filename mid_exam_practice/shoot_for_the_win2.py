targets = list(map(int, input().split()))
shot_count = 0
command = input()
value_before = 0
while not command == "End":
    index = int(command)
    if index in range(len(targets)):
        if targets[index] != -1:
            value_before = targets[index]
            shot_count += 1
            targets[index] = -1

        for ind in range(len(targets)):
            if targets[ind] > value_before and targets[ind] != -1:
                targets[ind] -= value_before
            elif targets[ind] <= value_before and targets[ind] != -1:
                targets[ind] += value_before

    command = input()

print(f'Shot targets: {shot_count} -> {" ".join(map(str, targets))}')

