next_pair_of_rows = int(input())
info = {}
for n in range(next_pair_of_rows):
    name = input()
    grade = float(input())
    if name not in info:
        info[name] = [grade]
    else:
        info[name].append(grade)

for k, v in info.items():
    avg = sum(v) / len(v)
    if avg >= 4.5:
        print(f"{k} -> {avg:.2f}")
