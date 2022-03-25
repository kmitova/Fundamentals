targets = input().split()
targets = list(map(int, targets))
target_value_before = 0
shot_count = 0
while True:
    command = input()
    if command == "End":
        break
    index = int(command)

    if index < len(targets):
        if targets[index] != -1:
            target_value_before = targets[index]
            targets[index] = -1

            shot_count += 1
        for ind in range(len(targets)):
            if targets[ind] > target_value_before and targets[ind] != -1:
                targets[ind] -= target_value_before
            elif targets[ind] <= target_value_before and targets[ind] != -1:
                targets[ind] += target_value_before

targets = list(map(str, targets))
targets = " ".join(targets)
print(f"Shot targets: {shot_count} -> {targets}")
