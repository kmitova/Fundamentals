words = input().split()

command = input()

while not command == "Stop":
    current_command = command.split()
    if current_command[0] == "Delete":
        index = int(current_command[1])
        if index+1 in range(len(words)):
            words.pop(index+1)
    elif current_command[0] == "Swap":
        word_1 = current_command[1]
        word_2 = current_command[2]
        if word_1 in words and word_2 in words:
            index_1 = words.index(word_1)
            index_2 = words.index(word_2)
            words[index_1], words[index_2] = words[index_2], words[index_1]
    elif current_command[0] == "Put":
        word = current_command[1]
        index = int(current_command[2])
        if index-1 in range(len(words)):
            words.insert(index-1, word)
    elif current_command[0] == "Sort":
        words.sort(reverse=True)
    elif current_command[0] == "Replace":
        word_1 = current_command[1]
        word_2 = current_command[2]
        if word_2 in words:
            index_2 = words.index(word_2)
            words[index_2] = word_1
    command = input()

print(" ".join(words))
