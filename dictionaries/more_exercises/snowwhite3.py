# dwarfs = {}
#
# command = input()
# while not command == "Once upon a time":
#     current = command.split(" <:> ")
#     name = current[0]
#     color = current[1]
#     physics = int(current[2])
#     if color not in dwarfs:
#         dwarfs[color] = [name, physics]
#     else:
#         if name not in dwarfs[color]:
#             dwarfs[color].append(name)
#             dwarfs[color].append(physics)
#         else:
#             name_index = dwarfs[color].index(name)
#             old_physics = dwarfs[color][name_index+1]
#             if int(physics) > int(old_physics):
#                 dwarfs[color][name_index+1] = physics
#
#     command = input()
#
#
# for key, value in dwarfs.items():
#     for ind in range(0, len(value), 2):
#
#         print(f"({key}) {value[ind]} <-> {value[ind+1]}")

# items = input()
# dwarfs = {}
# colors = {}
# while items != "Once upon a time":
#     tokens = items.split(" <:> ")
#     name = tokens[0]
#     color = tokens[1]
#     physics = int(tokens[2])
#     id = name + ":" + color
#     if id not in dwarfs:
#         if color not in colors:
#             colors[color] = 1
#         else:
#             colors[color] += 1
#         dwarfs[id] = [0, color]
#     dwarfs[id][0] = max([dwarfs[id][0], physics])
#     items = input()
#
# sorted_dwrafs = dict(sorted(dwarfs.items(), key=lambda x: (x[1][0], colors[x[1][1]]), reverse=True))
# for key, value in sorted_dwrafs.items():
#     tokens = key.split(":")
#     print(f"({tokens[1]}) {tokens[0]} <-> {value[0]}")


dwarfs = {}
command = input()
while not command == "Once upon a time":
    current = command.split(" <:> ")
    name = current[0]
    color = current[1]
    physics = int(current[2])
    if color not in dwarfs:
        dwarfs[color] = {name: physics}
    elif color in dwarfs:
        if name in dwarfs[color]:
            if physics > dwarfs[color][name]:
                dwarfs[color][name] = physics
        else:
            dwarfs[color].update({name: physics})
    command = input()

print(dwarfs)
for key, value in dwarfs.items():
    for k, v in value.items():
        print(f"({key}) {k} <-> {v}")
