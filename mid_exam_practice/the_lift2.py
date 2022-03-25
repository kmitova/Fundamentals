MAX_CAPACITY_PER_WAGON = 4
passengers = int(input())

current_state_of_lift = list(map(int, input().split()))

for i in range(len(current_state_of_lift)):
    while current_state_of_lift[i] < MAX_CAPACITY_PER_WAGON and passengers > 0:
        current_state_of_lift[i] += 1
        passengers -= 1


filtered_lift = list(set(current_state_of_lift))

max_capacity = len(current_state_of_lift) * MAX_CAPACITY_PER_WAGON

output_list = " ".join(list(map(str, current_state_of_lift)))
if passengers == 0 and sum(current_state_of_lift) < max_capacity:
    print("The lift has empty spots!")

elif passengers > 0:
    print(f"There isn't enough space! {passengers} people in a queue!")


print(output_list)

