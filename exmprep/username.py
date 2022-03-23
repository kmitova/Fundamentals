username = input()
command = input()
while not command == "Sign up":
    current = command.split()
    action = current[0]
    if action == "Case":
        if current[1] == "lower":
            username = username.lower()
            print(username)
        elif current[1] == "upper":
            username = username.upper()
            print(username)
    elif action == "Reverse":
        start = int(current[1])
        end = int(current[2])
        if start in range(len(username)) and end in range(len(username)):
            string = ""
            for ind in range(len(username)):
                if ind in range(start, end+1):
                    string += username[ind]
            print(string[::-1])
    elif action == "Cut":
        substring = current[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}")
    elif action == "Replace":
        char = current[1]
        username = username.replace(char, "*")
        print(username)
    elif action == "Check":
        char = current[1]
        if char in username:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")

    command = input()
