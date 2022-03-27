# works in all cases:

year = int(input()) + 1

while len(set(str(year))) != len(str(year)):
    year += 1

print(year)

# year = int(input())
# reached = False
#
# while True:
#     year += 1
#     year_str = str(year)
#     for i in year_str:
#         for j in year_str:
#             for k in year_str:
#                 for m in year_str:
#                     if not i == j and not i == k and not i == m:
#                         if not j == k and not j == m:
#                             if not k == m:
#                                 print(f"{i}{j}{k}{m}")
#                                 reached = True
#                                 break
#                     if reached:
#                         break
#                 if reached:
#                     break
#             if reached:
#                 break
#         if reached:
#             break
#     if reached:
#         break




