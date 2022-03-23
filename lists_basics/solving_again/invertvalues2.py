numbers = input().split()
opposites = []
for number in numbers:
    intnumber = int(number)
    intnumber = - intnumber
    opposites.append(intnumber)

print(opposites)
