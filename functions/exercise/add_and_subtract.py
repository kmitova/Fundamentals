def sum_numbers(num1, num2):
    result = num1 + num2
    return result


def subtract(first_sum, num3):
    return first_sum - num3


first_num = int(input())
second_num = int(input())
third_num = int(input())

sum_of_first_two = sum_numbers(first_num, second_num)

output = subtract(sum_of_first_two, third_num)
print(output)
