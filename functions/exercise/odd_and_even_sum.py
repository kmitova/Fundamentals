def odd_even_sum(num):
    even_sum = 0
    odd_sum = 0
    for symbol in number:
        digit = int(symbol)

        if digit % 2 == 0:
            even_sum += digit
        elif not digit % 2 == 0:
            odd_sum += digit
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()
result = odd_even_sum(number)
print(result)
