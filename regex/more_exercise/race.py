import re

pattern = r"([A-Za-z0-9])"
participants = input().split(", ")
results = {}
text = input()
while not text == "end of race":
    distance = 0
    name = ''
    matches = re.findall(pattern, text)
    for match in matches:
        if match.isdigit():
            distance += int(match)
        elif match.isalpha():
            name += match

    if name not in results:
        results[name] = distance
    else:
        results[name] += distance
    text = input()

results2 = {}
for key, value in results.items():
    if key in participants:
        results2[key] = value

sorted_results = sorted(results2.items(), key=lambda x: -x[1])

results_list = []
for item in sorted_results:

    results_list.append(item[0])
    if len(results_list) == 3:
        break


print(f"1st place: {results_list[0]}")
print(f"2nd place: {results_list[1]}")
print(f"3rd place: {results_list[2]}")
