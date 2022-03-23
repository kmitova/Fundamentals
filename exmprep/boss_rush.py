import re

pattern = r"|([A-Z]{4,})|:#([A-Za-z]+\s*[A-Za-z]+)#"

lines = int(input())

for line in range(lines):

    results = []
    text = input()
    matches = re.findall(pattern, text)
    if matches:
        print(matches)
        for match in matches:
            for el in match:
                if not el == "":
                    results.append(el)

        if len(results) == 2:
            print(f"{results[0]}, The {results[1]}")
            print(f">>> Strength: {len(results[0])}")
            print(f">>> Armour: {len(results[1])}")
        else:
            print("Access denied!")

