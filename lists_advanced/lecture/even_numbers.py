nums_as_string = input().split(", ")
nums = [int(num) for num in nums_as_string]
# nums_with_map = list(map(lambda num: int(num), nums_as_string)) # using map to convert to ints
# nums_map_ref = list(map(int, nums_as_string)) # another way to convert to ints

filtered_nums = [index for index in range(len(nums)) if nums[index] % 2 == 0]
print(filtered_nums)
# using filter() to print indices of even elements

# filtered_nums_filter = list(map(lambda el: nums.index(el), list(filter(lambda num: num % 2 == 0, nums))))
# print(filtered_nums_filter)