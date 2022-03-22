# # not sorted and tested in judge!
#
# data = input()
# dwarfs = {}
# while not data == "Once upon a time":
#     current = data.split(" <:> ")
#     name = current[0]
#     color = current[1]
#     physics = int(current[2])
#     if color not in dwarfs:
#         dwarfs[color] = {name: physics}
#     elif color in dwarfs:
#         if name != dwarfs[color]:
#             dwarfs[color][name] = physics
#         else:
#             if physics > dwarfs[color][name]:
#                 dwarfs[color][name] = physics
#
#     data = input()
# # print(dwarfs)
# # sorted_dwarfs = sorted(dwarfs.items(), key=lambda kvp: -kvp[1])
# # sorted_colors = sorted(dwarfs.items(), key=lambda kvp: -len(kvp[1]))
# # print(sorted_colors)
# sorted_dwarfs_list = []
# sorted_dwarfs_dict = {}
# # for color, dwarf in sorted_colors.items():
# #     sorted_dwarfs = sorted(dwarf.items(), key=lambda kvp: -kvp[1])
# #     # print(color, sorted_dwarfs)
#
#
# # print(sorted_dwarfs)
# # print(sorted_colors)
# colors = {}
# sorted_dwarfs = sorted(dwarfs.items(), key=lambda x: (x[1][0], colors[x[1][1]]), reverse=True)
# for key, value in sorted_dwarfs:
#     tokens = key.split(":")
#     print(f"({toens[1]}) {tokens[0]} <-> {value[0]}")
#

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

# sorted_dwarfs = sorted(dwarfs.items(), key=lambda x: (x[1][0], colors[x[1][1]]), reverse=True)
# for key, value in sorted_dwarfs:
#     tokens = key.split(":")
#     print(f"({tokens[1]}) {tokens[0]} <-> {value[0]}")

dwarfs = {}
colors = {}
command = input()

while not command == "Once upon a time":
    current = command.split(" <:> ")
    name = current[0]
    color = current[1]
    physics = int(current[2])
    if color not in dwarfs:
        dwarfs[color] = {name: physics}
        colors[color] = 1
    elif color in dwarfs:
        if name not in dwarfs[color]:
            dwarfs[color][name] = physics
            colors[color] += 1
        else:
            if physics > dwarfs[color][name]:
                dwarfs[color][name] = physics

    # if name not in dwarfs:
    #     dwarfs[name] = {color: physics}
    # elif name in dwarfs:
    #
    #     if color not in dwarfs[name]:
    #         dwarfs[name] = {color: physics}
    #     else:
    #         if physics > dwarfs[name][color]:
    #             dwarfs[name][color] = physics
    command = input()

print(dwarfs)
print(colors)
# print(len(dwarfs))

sorted_dwarfs = sorted(dwarfs.values(), key=lambda kvp: kvp[1])

print(sorted_dwarfs)

for color, dwarf in sorted_dwarfs:
    print(color, dwarf)



