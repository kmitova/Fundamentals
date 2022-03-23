message = input().split()
result = []
letter_code = []

for word in message:
    for ind in range(len(word)):
        if word[ind] in "0123456789":
            letter_code.append(word[ind])
    letter_code_num = "".join(letter_code)
    no_nums = list(filter(lambda x: x not in "0123456789", word))
    word_list = []
    for item in no_nums:
        word_list.append(item)
    word_list.insert(0, chr(int(letter_code_num)))
    word_list[1], word_list[-1] = word_list[-1], word_list[1]
    result.extend(word_list)
    result.append(" ")
    letter_code.clear()

result = "".join(result)
print(result)
