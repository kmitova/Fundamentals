# 100/100

targets_sequence = input().split()
targets_sequence_nums = list(map(int, targets_sequence))


while True:
    command = input()
    if command == "End":
        break
    current_command = command.split()
    action = current_command[0]
    index_of_action = int(current_command[1])
    if action == "Shoot":
        power = int(current_command[2])
        if index_of_action in range(len(targets_sequence_nums)):
            targets_sequence_nums[index_of_action] -= power
            if targets_sequence_nums[index_of_action] <= 0:
                targets_sequence_nums.pop(index_of_action)
        else:
            continue
    elif action == "Add":
        value = int(current_command[2])
        if index_of_action in range(len(targets_sequence_nums)):
            targets_sequence_nums.insert(index_of_action, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        radius = int(current_command[2])
        if index_of_action + radius < len(targets_sequence_nums) - 1\
                and index_of_action - radius >= 0:
            targets_sequence_nums.pop(index_of_action + radius)
            targets_sequence_nums.pop(index_of_action - radius)
            targets_sequence_nums.pop(index_of_action - radius)
        else:
            print("Strike missed!")
            continue

targets_sequence_nums = list(map(str, targets_sequence_nums))
result = "|".join(targets_sequence_nums)
print(result)
