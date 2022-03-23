def password_validator(password):
    number_of_chars = 0
    chars_are_valid = False
    only_l_and_d = False
    digits_are_valid = False
    for i in password:
        number_of_chars += 1
    if number_of_chars < 6 or number_of_chars > 10:
        chars_are_valid = False
    else:
        chars_are_valid = True
    for char in password:
        char_as_int = ord(char)
        if char_as_int not in range(48, 122):
            only_l_and_d = False
            break
        else:
            only_l_and_d = True
    digits = []
    for char in password:
        char_as_int = ord(char)
        if char_as_int in range(48, 58):
            digits.append(char)
    if len(digits) < 2:
        digits_are_valid = False
    else:
        digits_are_valid = True
    if not chars_are_valid:
        print("Password must be between 6 and 10 characters")
    if not only_l_and_d:
        print("Password must consist only of letters and digits")
    if not digits_are_valid:
        print("Password must have at least 2 digits")
    if chars_are_valid and digits_are_valid and only_l_and_d:
        print("Password is valid")


given_password = input()
password_validator(given_password)
