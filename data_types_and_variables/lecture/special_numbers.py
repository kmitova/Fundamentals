# number = int(input())
#
# for n in range(1, number + 1):
#     sum_of_digits = 0
#     digits = n
#     while digits > 0:
#         sum_of_digits += digits % 10
#         digits = int(digits / 10)
#     if (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11):
#         print(f"{n} -> True")
#     else:
#         print(f"{n} -> False")

# another better solution:

n = int(input())

for num in range(1, n+1):
    num_as_string = str(num)
    sum_digits = 0
    for num_str in num_as_string:
        sum_digits = sum_digits + int(num_str)
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")

