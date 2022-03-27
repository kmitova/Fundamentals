string = input()
string_as_list = []
for el in string:
    string_as_list.append(el)

capitals = []
for el in string_as_list:
    if el.isupper():
        capitals.append(el)


indexes = []
for i in range(len(string_as_list)):
    for j in capitals:
        if string_as_list[i] == j:
            indexes.append(i)
filtered = []
for ind in indexes:
    if ind not in filtered:
        filtered.append(ind)

print(filtered)
