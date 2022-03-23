def perfect_number(integer):
    sm = 0
    for i in range(1, integer):
        if integer % i == 0:
            sm += i
    if sm == integer:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


given_integer = int(input())
result = perfect_number(given_integer)
print(result)
