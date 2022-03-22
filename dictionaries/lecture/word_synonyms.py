n = int(input())
count = 2 * n
dict = {}

for i in range(n):
    word = input()
    synonym = input()
    if word not in dict:
        dict[word] = []
    dict[word].append(synonym)

for key in dict:
    print(f"{key} - {', '.join(dict[key])}")
