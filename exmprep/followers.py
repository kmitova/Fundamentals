# command = input()
# followers = {}
# while not command == "Log out":
#     current = command.split(": ")
#     action = current[0]
#     name = current[1]
#     if action == "New follower":
#         if name not in followers:
#             followers[name] = {"likes": 0, "comments": 0}
#     elif action == "Like":
#         count = int(current[2])
#         if name not in followers:
#             followers[name] = {"likes": 0, "comments": 0}
#         else:
#             followers[name]["likes"] += count
#
#     elif action == "Comment":
#         if name not in followers:
#             followers[name] = {"likes": 0, "comments": 0}
#         else:
#             followers[name]["likes"] += 1
#     elif action == "Blocked":
#         if name in followers:
#             del followers[name]
#         else:
#             print(f"{name} doesn't exist.")
#     command = input()
#
# sorted_followers = sorted(followers.items(), key=lambda kvp: (-kvp[1][0], kvp[0]))
# print(sorted_followers)





command = input()
followers = {}
while not command == "Log out":
    current = command.split(": ")
    action = current[0]
    name = current[1]
    if action == "New follower":
        if name not in followers:
            followers[name] = [0, 0]
    elif action == "Like":
        count = int(current[2])
        if name not in followers:
            followers[name] = [0, 0]

        followers[name][0] += count

    elif action == "Comment":
        if name not in followers:
            followers[name] = [0, 0]

        followers[name][1] += 1
    elif action == "Blocked":
        if name in followers:
            del followers[name]
        else:
            print(f"{name} doesn't exist.")
    command = input()

sorted_followers = sorted(followers.items(), key=lambda kvp: (-kvp[1][0], kvp[0]))

print(f"{len(followers)} followers")
for name, value in sorted_followers:
    print(f"{name}: {sum(value)}")