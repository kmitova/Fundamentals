string = input()

command = input()
while not command == "End":
    current = command.split()
    action = current[0]
    if action == "Translate":
        char = current[1]
        replacement = current[2]
        string = string.replace(char, replacement)
        print(string)
    elif action == "Includes":
        substring = current[1]
        if substring in string:
            print("True")
        else:
            print("False")
    elif action == "Start":
        substring = current[1]
        length = len(substring)
        if string[:length] == substring:
            print("True")
        else:
            print("False")
    elif action == "Lowercase":
        string = string.lower()
        print(string)
    elif action == "FindIndex":
        char = current[1]
        for ind in range(len(string) -1, -1, -1):
            if string[ind] == char:
                print(ind)
                break
    elif action == "Remove":
        start = int(current[1])
        count = int(current[2])
        string = string.replace(string[start:start+count], "")
        print(string)
    command = input()
