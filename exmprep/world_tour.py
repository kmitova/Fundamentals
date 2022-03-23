# import re
#
# stops = input()
# stops = [el for el in stops]
# # stops_list = re.findall(r"\w+|[^\s\w]+", stops)
# # print(stops_list)
# command = input()
#
# while not command == "Travel":
#     current = command.split(":")
#     action = current[0]
#     if action == "Add Stop":
#         index = int(current[1])
#         string = current[2]
#         if index in range(len(stops)):
#             stops.insert(index, string)
#         print(stops)
#     elif action == "Remove Stop":
#         start = int(current[1])
#         end = int(current[2])
#         if start in range(len(stops)) and end in range(len(stops)):
#             del stops[start:end+1]
#         print(stops)
#
#             # stops_list = stops_list[:start+1] + stops_list[start+1:end+1]
#     elif action == "Switch":
#         old_string = current[1]
#         new_string = current[2]
#         if old_string in stops:
#             os_index = stops.index(old_string)
#
#             for ind in range(len(stops)):
#                 if ind == os_index:
#                     stops[ind] = new_string
#                     # stops.replace(old_string, new_string)
#
#             print(stops)
#     command = input()
#
# print(f"Ready for world tour! Planned stops: {''.join(stops)}")

def add_stop(stops_str, idx, str):
    if idx in range(len(stops_str)):
        return stops_str[:idx] + str + stops_str[idx:]
    return stops_str


def remove_stop(stops_str, start, stop):
    if start in range(len(stops_str)) and stop in range(len(stops_str)):
        return stops_str[:start] + stops_str[stop + 1:]
    return stops_str


def switch(stops_str, old, new):
    return stops_str.replace(old, new)


stops = input()

while True:
    data = input()

    if data == "Travel":
        break

    split_data = data.split(':')
    command = split_data[0]

    if command == "Add Stop":
        index = int(split_data[1])
        string = split_data[2]
        stops = add_stop(stops, index, string)
    elif command == "Remove Stop":
        start_index = int(split_data[1])
        stop_index = int(split_data[2])
        stops = remove_stop(stops, start_index, stop_index)
    elif command == "Switch":
        old_string = split_data[1]
        new_string = split_data[2]
        stops = switch(stops, old_string, new_string)

    print(stops)

print(f"Ready for world tour! Planned stops: {stops}")
