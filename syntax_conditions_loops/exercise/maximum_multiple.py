# divisor = int(input())
# bound = int(input())
#
# for n in range(bound, divisor - 1, -1):
#     if n % divisor == 0:
#         if n <= bound:
#             if n > 0:
#                 print(n)
#                 break

# another way:

divisor = int(input())
bound = int(input())

result = int(bound / divisor) * divisor
print(result)
