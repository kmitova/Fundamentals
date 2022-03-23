words = input().split()
palindrome = input()

found_palindromes = [item for item in words if item == item[::-1]]
print(found_palindromes)

palindrome_found_n_times = words.count(palindrome)

print(f"Found palindrome {palindrome_found_n_times} times")
