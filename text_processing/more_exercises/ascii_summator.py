code_sym1 = ord(input())
code_sym2 = ord(input())
text = input()
total_sum = 0
for el in text:
    if ord(el) in range(code_sym1+1, code_sym2):
        total_sum += ord(el)

print(total_sum)
