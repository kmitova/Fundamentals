def tribonacci(signature, n):
    output = []

    for number_of_times in range(1, n-2):
        add = 0
        for last_three in signature[-3:]:
            add += last_three
        signature.append(add)
    for nthelement in signature[:n]:
        output.append(nthelement)
    return output


number = int(input())
result = tribonacci([1, 1, 2], number)
result_as_string = [str(int) for int in result]
result_as_string_done = " ".join(result_as_string)
print(result_as_string_done)
