lines = int(input())
total_sum = 0

for line in range(lines):
    letter = input()
    ascii_letter = ord(letter)
    total_sum += ascii_letter

print(f"The sum equals: {total_sum}")
