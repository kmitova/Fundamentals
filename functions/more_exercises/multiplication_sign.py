def multiplication_sign(num1, num2, num3):
    if num1[0] == "0" or num2[0] == "0" or num3[0] == "0":
        return "zero"
    elif num1[0] != "-" and num2[0] != "-" and num3[0] != "-":
        return "positive"
    elif num1[0] != "-" and num2[0] == "-" and num3[0] == "-":
        return "positive"
    elif num1[0] == "-" and num2[0] == "-" and num3[0] != "-":
        return "positive"
    elif num1[0] == "-" and num2[0] != "-" and num3[0] == "-":
        return "positive"
    else:
        return "negative"


n1 = input()
n2 = input()
n3 = input()
result = multiplication_sign(n1, n2, n3)
print(result)

