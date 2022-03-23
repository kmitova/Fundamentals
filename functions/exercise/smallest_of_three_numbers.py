def smallest_number(num1, num2, num3):
    numbers_list = [num1, num2, num3]
    return min(numbers_list)


first_num = int(input())
second_num = int(input())
third_num = int(input())

smallest = smallest_number(first_num, second_num, third_num)
print(smallest)
