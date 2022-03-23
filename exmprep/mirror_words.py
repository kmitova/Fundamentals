import re

pattern = r"(@|#)([A-Za-z]{3,})(\1)(\1)([A-Za-z]{3,})(\1)"
text = input()
words = {}
matches = re.findall(pattern, text)

if matches:
    print(f"{len(matches)} word pairs found!")
    for item in matches:
        if item[1] == item[4][::-1]:
            words[item[1]] = item[4]
else:
    print("No word pairs found!")

if len(words) == 0:
    print("No mirror words!")
else:
    res = ""
    print("The mirror words are:")
    for key, value in words.items():
        res += f"{key} <=> {value}" + ", "
    print(res.rstrip(", "))
