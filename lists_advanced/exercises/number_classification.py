numbers = input().split(", ")
numbers = list(map(int, numbers))
positives = [num for num in numbers if num >= 0]
negatives = [num for num in numbers if num < 0]
even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if not num % 2 == 0]

positives = list(map(str, positives))
negatives = list(map(str, negatives))
even = list(map(str, even))
odd = list(map(str, odd))

positives_string = ", ".join(positives)
negatives_string = ", ".join(negatives)
even_string = ", ".join(even)
odd_string = ", ".join(odd)


print(f"Positive: {positives_string}")
print(f"Negative: {negatives_string}")
print(f"Even: {even_string}")
print(f"Odd: {odd_string}")
