# results = {}
# submissions = {}
# data = input()
# while not data == "exam finished":
#     current = data.split("-")
#     if len(current) == 3:
#         name = current[0]
#         language = current[1]
#         points = int(current[2])
#         if language not in submissions:
#             submissions[language] = [1]
#         else:
#             submissions[language].append(1)
#         if name not in results:
#             results[name] = {"language": language, "points": points}
#         elif name in results and results[name]["language"] == language:
#             if results[name]["points"] < points:
#                 results[name]["points"] = points
#     else:
#         current = data.split("-")
#         name = current[0]
#         del results[name]
#     data = input()
#
# print("Results:")
# for key, value in results.items():
#     points = results[key]["points"]
#     print(f"{key} | {points}")
#
# print("Submissions:")
# for k, v in submissions.items():
#     length = len(v)
#     print(f"{k} - {length}")


results = {}
submissions = {}
info = input()
while not info == "exam finished":
    current = info.split("-")
    if len(current) == 2:
        name = current[0]
        for key, value in results.items():
            for k, v in value.items():
                if k == name:
                    del results[key][name]
                    break
    else:
        name = current[0]
        language = current[1]
        points = int(current[2])
        if language not in submissions:
            submissions[language] = 1
        else:
            submissions[language] += 1
        if language not in results:
            results[language] = {name: points}
        else:
            if name not in results[language]:
                results[language].update({name: points})
            else:
                if points > results[language][name]:
                    results[language][name] = points
    info = input()

print("Results:")
for key, value in results.items():
    for k, v in value.items():
        print(f"{k} | {v}")

print("Submissions:")
for key, value in submissions.items():
    print(f"{key} - {value}")


























