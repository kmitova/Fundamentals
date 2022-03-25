nums = list(map(int, input().split()))

average = sum(nums) / len(nums)

nums = [i for i in nums if i > average]
if len(nums) == 0:
    print("No")
    exit()

nums.sort(reverse=True)

to_print = []

for i in nums:
    to_print.append(i)
    if len(to_print) == 5:
        break

print(" ".join(map(str, to_print)))
