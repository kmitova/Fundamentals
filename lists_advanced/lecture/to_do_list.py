todo_list = [0] * 10

command = input()
while command != "End":
    importance, note = command.split("-")
    importance = int(importance) - 1
    todo_list[importance] = note
    command = input()

filtered = [item for item in todo_list if not item == 0]
print(filtered)
