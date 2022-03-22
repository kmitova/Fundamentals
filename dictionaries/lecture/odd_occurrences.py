words = input().split()
words = list(map(lambda x: x.lower(), words))
dict = {}

for word in words:
    if word not in dict:
        dict[word] = 0
    dict[word] += 1


for key, value in dict.items():
    if not value % 2 == 0:
        print(key, end=" ")
