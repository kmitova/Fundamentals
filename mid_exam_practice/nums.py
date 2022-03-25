integers = list(map(int, input().split()))
average = sum(integers) / len(integers)

bigger = sorted([num for num in integers if num > average])
bigger.sort(reverse=True)

top_5 = []
length = 0

if not bigger:
    print("No")

else:
    for el in bigger:
        top_5.append(el)
        length += 1
        if length >= 5:
            break

    print(" ".join(list(map(str, top_5))))
