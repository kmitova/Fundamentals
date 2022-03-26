import re

pattern = r"((www)\.([A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+))"
text = input()
valid_urls = []

while text:
    matches = re.finditer(pattern, text)
    for match in matches:
        valid_urls.append(match.group(1))
    text = input()

for item in valid_urls:
    print(item)
