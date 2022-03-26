import re

txt = "The rain in Spain"
x = re.search(r"^The.*Spain$", txt)
result = x.group(0)  # 0 takes all matches
print(result)
