version = input().split(".")
version = [int(num) for num in version]

for ind in range(len(version)-1, -1, -1):
    if version[ind] == 9:
        version[ind] = 0
        if version[ind - 1] < 9:
            version[ind - 1] += 1
            break
        elif version[ind-1] == 9:
            version[ind - 1] = 0
            version[ind - 2] += 1
            break
    version[ind] += 1
    break

result = [str(el) for el in version]
print(".".join(result))
