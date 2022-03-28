text = input().split()
emoticon = ""
for word in text:
    for index in range(len(word)):
        if word[index] == ":":
            if len(word) > 1:
                emoticon = word[index] + word[index+1]
                print(emoticon)
