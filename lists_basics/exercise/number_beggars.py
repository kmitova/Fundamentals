# coins = [int(num) for num in input().split(", ")]
# beggars = int(input())
# count = 0
# beggars_list = [0] * beggars
# for coin in coins:
#     beggars_list[count] += coin
#     count += 1
#     if count >= beggars:
#         count = 0
# print(beggars_list)

# another solution

list_of_numbers_as_string = input().split(", ")
beggars = int(input())
sums_of_each_beggar = []
start_index = 0

for beggar in range(beggars):
    current_sum = 0
    for index in range(start_index, len(list_of_numbers_as_string), beggars):
        current_sum += int(list_of_numbers_as_string[index])
    sums_of_each_beggar.append(current_sum)
    start_index += 1

print(sums_of_each_beggar)
