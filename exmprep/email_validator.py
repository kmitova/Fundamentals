email = input()

command = input()
while not command == "Complete":
    current = command.split()
    action = current[0]
    if action == "Make":
        if current[1] == "Upper":
            email = email.upper()
            print(email)
        elif current[1] == "Lower":
            email = email.lower()
            print(email)
    elif action == "GetDomain":
        count = int(current[1])
        print(email[len(email) - count:])
    elif action == "GetUsername":
        if "@" in email:
            username = ""
            for char in email:
                if not char == "@":
                    username += char
                else:
                    break
            print(username)
        else:
            print(f"The email {email} doesn't contain the @ symbol.")
    elif action == "Replace":
        char = current[1]
        email = email.replace(char, "-")
        print(email)
    elif action == "Encrypt":
        encrypted = ""
        for char in email:
            encrypted += str(ord(char)) + " "
        print(encrypted.rstrip())
    command = input()