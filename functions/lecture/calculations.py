def calculate(operator, num1, num2):
    if operator == "multiply":
        return num1*num2
    elif operator == "divide":
        return num1/num2
    elif operator == "add":
        return num1+num2
    elif operator == "subtract":
        return num1-num2


given_command = input()
first_number = int(input())
second_number = int(input())
result = calculate(given_command, first_number, second_number)
print(int(result))
