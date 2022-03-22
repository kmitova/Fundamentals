
submissions = {}
users = {}

while True:
    line = input()
    if line == "no more time":
        break
    line = line.split(" -> ")
    username = str(line[0])
    contest = str(line[1])
    points = int(line[2])

    if contest not in submissions:
        submissions[contest] = {username: points}
    if username not in submissions[contest]:
        submissions[contest][username] = points
    if username not in users:
        users[username] = {contest: points}
    else:
        users[username][contest] = points
    if submissions[contest][username] < points:
        submissions[contest][username] = points
    if users[username][contest] < points:
        users[username][contest] = points

for key, value in submissions.items():
    print(f"{key}: {len(value)} participants")
    sorted_names = sorted(value.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    n = 0
    for name, grade in sorted_names:
        n += 1
        print(f"{n}. {name} <::> {grade}")

print("Individual standings:")

ind_points = {}

for value in submissions.values():
    for k, v in value.items():
        if k not in ind_points:
            ind_points[k] = v
        else:
            ind_points[k] += v

sorted_points = sorted(ind_points.items(), key=lambda kvp: (-kvp[1], kvp[0]))

i = 0
for k, v in sorted_points:
    i += 1
    print(f"{i}. {k} -> {v}")
