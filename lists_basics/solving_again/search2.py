lines = int(input())
word = input()
strings = []
for line in range(lines):
    string = input()
    strings.append(string)

print(strings)

for index in range(len(strings) - 1, -1, -1):
    element = strings[index]
    if word not in element:
        strings.remove(element)

print(strings)

