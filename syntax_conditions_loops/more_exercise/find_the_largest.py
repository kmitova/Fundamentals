number_as_string = input()

numbers = []


for number in number_as_string:
    numbers.append(number)

numbers.sort()
numbers.reverse()
print("".join(numbers))

