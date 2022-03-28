strings = input().split()
str1 = strings[0]
str2 = strings[1]
difference = abs(len(str1) - len(str2))
total_sum = 0

if len(str1) > len(str2):
    for index in range(0, len(str2)):
        total_sum += ord(str1[index]) * ord(str2[index])
    for index in range(len(str1) - difference, len(str1)):
        total_sum += ord(str1[index])
elif len(str2) > len(str1):
    for index in range(0, len(str1)):
        total_sum += ord(str1[index]) * ord(str2[index])
    for index in range(len(str2) - difference, len(str2)):
        total_sum += ord(str2[index])
else:
    for index in range(0, len(str1)):
        total_sum += ord(str1[index]) * ord(str2[index])

print(total_sum)

