path = input().split("\\")
info = path[-1]

info = info.split(".")
name = info[0]
extension = info[1]

print(f"File name: {name}")
print(f"File extension: {extension}")
