import re

string = input()

pattern = r"(#|@)([A-Za-z]{3,})(\1)(\1)([A-Za-z]{3,})(\1)"

matches = re.finditer(pattern, string)
words = []
pairs = 0
found = False
if matches:

    for match in matches:
        found = True
        word1 = match.group(2)
        word2 = match.group(5)
        pairs += 1
        if word2 == word1[::-1]:
            words.append(word1)
            words.append(word2)

if not found:
    print("No word pairs found!")

if pairs > 0:
    print(f"{pairs} word pairs found!")

if len(words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    result = ""
    for i in range(0, len(words), 2):
        result += f"{words[i]} <=> {words[i+1]}, "
    print(result.rstrip(", "))

