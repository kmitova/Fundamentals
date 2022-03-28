banned_words = input().split(", ")
text = input()

for item in banned_words:
    while item in text:
        text = text.replace(item, len(item)*"*")

print(text)


