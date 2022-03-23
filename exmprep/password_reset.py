text = input()

command = input()
while not command == "Done":
    current = command.split()
    action = current[0]
    if action == "TakeOdd":
        new_text = ""
        for ind in range(len(text)):
            if not ind % 2 == 0:
                new_text += text[ind]
        text = new_text
        print(text)
    elif action == "Cut":
        index = int(current[1])
        length = int(current[2])
        substr = text[index:index + length]
        if substr in text:
            text = text.replace(substr, "", 1)
        print(text)
    elif action == "Substitute":
        substring = current[1]
        substitute = current[2]
        if substring in text:
            occurrences = text.count(substring)
            for i in range(occurrences):
                text = text.replace(substring, substitute)
            print(text)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {text}")
