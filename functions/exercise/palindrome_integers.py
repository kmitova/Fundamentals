def check_and_print_if_palindrome(element):
    if element == element[::-1]:
        return True
    return False


numbers_as_string = input().split(", ")

for num_as_str in numbers_as_string:
    print(check_and_print_if_palindrome(num_as_str))
