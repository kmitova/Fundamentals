import re

pattern = r"\+359( |-)2(\1)\d{3}(\1)\d{4}\b"
numbers = input()
matches = re.finditer(pattern, numbers)

res = ""
for match in matches:
    match_str = match.group(0)
    res += match_str + ", "

print(res.rstrip(", "))
