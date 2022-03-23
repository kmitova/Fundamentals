import re

pattern = r"(::|\*\*)([A-Z]{1}[a-z]{2,})(\1)"
text = input()

threshold = 1

for char in text:
    if char.isdigit():
        char = int(char)
        threshold = char * threshold

print(f"Cool threshold: {threshold}")
all_emojis = []
cool_emojis = []

matches = re.findall(pattern, text)
if matches:
    for el in matches:
        total = 0
        emoji = "".join(el)
        all_emojis.append(emoji)
        for char in el[1]:
            total += ord(char)
        if total >= threshold:
            cool_emojis.append(emoji)

print(f"{len(all_emojis)} emojis found in the text. The cool ones are:")
for item in cool_emojis:
    print(item)
