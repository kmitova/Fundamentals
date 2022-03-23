number_sequence = input().split()
half = int(len(number_sequence) / 2)
left_side = number_sequence[0:half]
right_side = number_sequence[half+1::]
right_side.reverse()

left_time = 0
right_time = 0

for element in left_side:
    num = int(element)
    if num == 0:
        left_time = left_time * 0.8
    left_time += num

for element in right_side:
    num = int(element)
    if num == 0:
        right_time = right_time * 0.8
    right_time += num

if left_time < right_time:
    print(f"The winner is left with total time: {left_time:.1f}")
else:
    print(f"The winner is right with total time: {right_time:.1f}")
