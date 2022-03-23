def factorial_division(num1, num2):
    less_than_num1 = []
    num1_factorial = 1
    for i in range(1, num1+1):
        less_than_num1.append(i)
    for number in less_than_num1:
        num1_factorial *= number

    less_than_num2 = []
    num2_factorial = 1
    for i in range(1, num2 + 1):
        less_than_num2.append(i)
    for number in less_than_num2:
        num2_factorial *= number

    result = num1_factorial / num2_factorial
    return f"{result:.2f}"


number_1 = int(input())
number_2 = int(input())
output = factorial_division(number_1, number_2)
print(output)
