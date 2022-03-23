from sys import maxsize


def exchange_places(numbers, ind):
    if ind not in range(len(numbers)):
        print("Invalid index")
    first_half = numbers[:ind+1]
    second_half = numbers[ind+1:]
    numbers = second_half + first_half
    return numbers


def max_odd(numbers):
    odds = [x for x in numbers if x % 2 != 0]
    if len(odds) == 0:
        return "No matches"
    max_odd_number = - maxsize
    max_index = 0
    for i, value in enumerate(numbers):
        if value % 2 != 0 and value >= max_odd_number:
            max_odd_number = value
            max_index = i
    return max_index


def max_even(numbers):
    evens = [x for x in numbers if x % 2 == 0]
    if len(evens) == 0:
        return "No matches"
    max_even_number = -maxsize
    max_index = 0
    for i, value in enumerate(numbers):
        if value % 2 == 0 and value >= max_even_number:
            max_even_number = value
            max_index = i
    return max_index


def min_odd(numbers):
    odds = [x for x in numbers if x % 2 != 0]
    if len(odds) == 0:
        return "No matches"
    min_odd_number = maxsize
    min_index = 0
    for i, value in enumerate(numbers):
        if value % 2 != 0 and value <= min_odd_number:
            min_odd_number = value
            min_index = i
    return min_index


def min_even(numbers):
    evens = [x for x in numbers if x % 2 == 0]
    if len(evens) == 0:
        return "No matches"
    min_even_number = maxsize
    min_index = 0
    for i, value in enumerate(numbers):
        if value % 2 == 0 and value <= min_even_number:
            min_even_number = value
            min_index = i
    return min_index


def first_even(numbers, n):
    result_list = []
    if n > len(numbers):
        return "Invalid count"
    evens = [x for x in numbers if x % 2 == 0]
    if len(evens) == 0:
        empty = []
        return empty
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            result_list.append(numbers[i])
            if len(result_list) == n:
                break
    return result_list


def first_odd(numbers, n):
    result_list = []
    if n > len(numbers):
        return "Invalid count"
    odds = [x for x in numbers if x % 2 != 0]
    if len(odds) == 0:
        empty = []
        return empty
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            result_list.append(numbers[i])
            if len(result_list) == n:
                break
    return result_list


def last_even(numbers, n):
    result_list = []
    if n > len(numbers):
        return "Invalid count"
    evens = [x for x in numbers if x % 2 == 0]
    if len(evens) == 0:
        empty = []
        return empty
    for i in range(len(numbers)-1,-1,-1):
        if numbers[i] % 2 == 0:
            result_list.append(numbers[i])
            if len(result_list) == n:
                break
    result_list.reverse()
    return result_list


def last_odd(numbers, n):
    result_list = []
    if n > len(numbers):
        return "Invalid count"
    odds = [x for x in numbers if x % 2 != 0]
    if len(odds) == 0:
        empty = []
        return empty
    for i in range(len(numbers)-1,-1,-1):
        if numbers[i] % 2 != 0:
            result_list.append(numbers[i])
            if len(result_list) == n:
                break
    result_list.reverse()
    return result_list


a = 5

sequence = list(map(int, input().split()))

command = input()
while not command == "end":
    current_command = command.split()
    action = current_command[0]
    if action == "exchange":
        index = int(current_command[1])
        result = exchange_places(sequence, index)
        sequence = result
    elif action == "max":
        if current_command[1] == "odd":
            result = max_odd(sequence)
            print(result)
        elif current_command[1] == "even":
            result = max_even(sequence)
            print(result)
    elif action == "min":
        if current_command[1] == "odd":
            result = min_odd(sequence)
            print(result)
        elif current_command[1] == "even":
            result = min_even(sequence)
            print(result)

    elif action == "first":
        count = int(current_command[1])
        if current_command[2] == "even":
            result = first_even(sequence, count)
            print(result)
        elif current_command[2] == "odd":
            result = first_odd(sequence, count)
            print(result)

    elif action == "last":
        count = int(current_command[1])
        if current_command[2] == "even":
            result = last_even(sequence, count)
            print(result)
        elif current_command[2] == "odd":
            result = last_odd(sequence, count)
            print(result)

    command = input()

print(sequence)
