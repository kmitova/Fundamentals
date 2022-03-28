text = input()
encrypted = ""

for char in text:
    new_symbol = ord(char) + 3
    encrypted += chr(new_symbol)

print(encrypted)
