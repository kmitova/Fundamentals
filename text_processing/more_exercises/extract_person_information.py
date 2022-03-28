lines = int(input())

for n in range(lines):
    string = input()
    name = ""
    age = ""
    for el in range(len(string)):

        if string[el] == "@":
            next_el = el+1
            while not string[next_el] == "|":
                name += string[next_el]
                next_el += 1
        if string[el] == "#":
            next_el = el+1
            while not string[next_el] == "*":
                age += string[next_el]
                next_el += 1
    print(f"{name} is {age} years old.")
