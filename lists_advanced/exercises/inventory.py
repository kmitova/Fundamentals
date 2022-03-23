items = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break
    command = command.split(" - ")
    action = command[0]
    if action == "Collect":
        item = command[1]
        if item not in items:
            items.append(item)
        else:
            continue
    elif action == "Drop":
        item = command[1]
        if item in items:
            items.remove(item)
    elif action == "Combine Items":
        old_item, new_item = command[1].split(":")
        old_and_new = command[1].split(":")

        if old_item in items:
            old_item_index = items.index(old_item)
            items.insert(old_item_index + 1, new_item)
        else:
            continue
    elif action == "Renew":
        item = command[1]
        if item in items:
            items.remove(item)
            items.append(item)


items = ", ".join(items)
print(items)

# def item_already_exists(item, items_list):
#     if item in items_list:
#         return True
#     return False
#
#
# list_of_items = input().split(", ")
# command = input()
#
# while not command == "Craft!":
#     data = command.split(" - ")
#     action = data[0]
#     item = data[1]
#     if action == "Collect":
#         if not item_already_exists(item, list_of_items):
#             list_of_items.append(item)
#     elif action == "Drop":
#         if item_already_exists(item, list_of_items):
#             list_of_items.remove(item)
#     elif action == "Combine Items":
#         old_item, new_item = data[1].split(":")
#         if item_already_exists(old_item, list_of_items):
#             old_item_index = list_of_items.index(old_item)
#             list_of_items.insert(old_item_index + 1, new_item)
#     elif action == "Renew":
#         if item_already_exists(item, list_of_items):
#             list_of_items.remove(item)
#             list_of_items.append(item)
#     command = input()
#
# print(", ".join(list_of_items))
