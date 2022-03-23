# without lambda
# def repeat_string(string, count):
#     return string * count
#
#
# given_string = input()
# given_count = int(input())
# result = repeat_string(given_string, given_count)
# print(result)

# with lambda
given_string = input()
given_count = int(input())

result = lambda string, count: string * count
print(result(given_string, given_count))
