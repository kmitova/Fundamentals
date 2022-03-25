integers = list(map(int, input().split()))

command = input()
while not command == "end":
    current = command.split()
    action = current[0]
    if action == "swap":
        index_1 = int(current[1])
        index_2 = int(current[2])
        integers[index_1], integers[index_2] = integers[index_2], integers[index_1]
    elif action == "multiply":
        index_1 = int(current[1])
        index_2 = int(current[2])
        integers[index_1] *= integers[index_2]
    elif action == "decrease":
        integers = [el-1 for el in integers]

    command = input()
integers = map(str, integers)
print(", ".join(integers))
