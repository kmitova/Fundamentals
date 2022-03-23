results = {}
submissions = {}
command = input()
while not command == "exam finished":
    current = command.split("-")
    if len(current) == 2:
        username = current[0]
        name = current[0]
        del results[name]
    else:
        name = current[0]
        language = current[1]
        points = int(current[2])
        if name not in results:
            results[name] = {"language": [language], "points": [points]}
        elif name in results and language not in results[name]["language"]:
            results[name]["language"].append(language)
            results[name]["points"].append(points)
        elif language in results[name]["language"]:
            language_index = results[name]["language"].index(language)
            points_index = language_index
            if results[name]["points"[points_index]] < points:
                results[name]["points"[points_index]] = points
        if language in submissions:
            submissions[language] += 1
        else:
            submissions[language] = 1
    command = input()

print(results)
print(submissions)