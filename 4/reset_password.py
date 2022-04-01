string = input()

data = input()
while not data == "Done":
    current = data.split()
    action = current[0]
    if action == "TakeOdd":
        new = ""
        for i in range(len(string)):
            if i % 2 != 0:
                new += string[i]
        string = new
        print(new)
    elif action == "Cut":
        index = int(current[1])
        length = int(current[2])
        substring = string[index: index+length]
        string = string.replace(substring, "", 1)
        print(string)
    elif action == "Substitute":
        substring = current[1]
        substitute = current[2]
        if substring in string:
            string = string.replace(substring, substitute)
            print(string)
        else:
            print("Nothing to replace!")

    data = input()

print(f"Your password is: {string}")
