string = input()
string_list = [char for char in string]
next = 0
for i in range(len(string_list)-1, -1, -1):
    next = i - 1
    if next in range(len(string_list)):
        if string_list[next] == string_list[i]:
            string_list.pop(next)

print("".join(string_list))
