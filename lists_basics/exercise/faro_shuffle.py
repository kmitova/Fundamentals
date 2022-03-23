# deck = input().split()
# shuffles = int(input())
#
# length = len(deck)
# mid = int(length / 2)
#
# for i in range(0, shuffles):
#     result = []
#     for j in range(0, mid):
#         result.append(deck[j])
#         result.append(deck[mid])
#         mid += 1
#     deck = result
#     mid = int(length / 2)
#
# print(result)

# another solution

deck = input().split()
shuffles = int(input())
left_half = []
right_half = []

for shuffle in range(shuffles):
    current_deck = []
    half = int(len(deck)/2)
    left_half = deck[0:half]
    right_half = deck[half::]
    for index in range(len(left_half)):  # could use right half too, does not matter
        current_deck.append(left_half[index])
        current_deck.append(right_half[index])
    deck = current_deck

print(deck)
