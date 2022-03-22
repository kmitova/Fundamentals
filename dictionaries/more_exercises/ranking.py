data1 = input()
contests_passwords = {}
while not data1 == "end of contests":
    contest, password = data1.split(":")
    if contest not in contests_passwords:
        contests_passwords[contest] = password
    data1 = input()

users_contests = {}
users_points = {}
data2 = input()
while not data2 == "end of submissions":
    contest, password, username, points = data2.split("=>")
    points = int(points)
    if contest in contests_passwords:
        if contests_passwords[contest] == password:
            if username not in users_contests:
                users_contests[username] = {contest: points}
            elif username in users_contests and contest not in users_contests[username]:
                users_contests[username][contest] = points

            elif username in users_contests and contest in users_contests[username]:
                if points > users_contests[username][contest]:
                    users_contests[username][contest] = points

    data2 = input()

best = ""
max_points = 0
for key, val in users_contests.items():
    total_points = 0
    for v in users_contests[key].values():
        values = users_contests[key].values()
        total_points = sum(values)
        if total_points > max_points:
            max_points = total_points
            best = key


print(f"Best candidate is {best} with total {max_points} points.")
sorted_result = sorted(users_contests.items(), key=lambda kvp: kvp[0])

print("Ranking:")
for item in sorted_result:
    print(item[0])
    sorted_item = sorted(item[1].items(), key=lambda kvp: kvp[1], reverse=True)
    for i in sorted_item:
        print(f"#  {i[0]} -> {i[1]}")


