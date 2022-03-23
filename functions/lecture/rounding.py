def rounding(numbers):
    rounded_numbers = []
    for number in numbers:
        number_rounded = round(float(number))
        rounded_numbers.append(number_rounded)
    return rounded_numbers


given_numbers = input().split()
result = rounding(given_numbers)
print(result)
