digits = ""
letters = ""
other = ""

string = input()

for sym in string:
    if ord(sym) in range(49, 58):
        digits += sym
    elif ord(sym) in range(65, 91):
        letters += sym
    elif ord(sym) in range(97, 132):
        letters += sym
    else:
        other += sym

print(digits)
print(letters)
print(other)

#  can solve with isdigit and isalpha methods as well
