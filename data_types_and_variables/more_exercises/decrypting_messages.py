key = int(input())
lines = int(input())
lst = []

for line in range(lines):
    char = input()
    add = key + ord(char)
    lst.append(add)

for elem in lst:
    print(chr(elem), end="")


