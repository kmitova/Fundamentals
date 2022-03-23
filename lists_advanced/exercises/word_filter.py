text = input().split()

filtered = list(filter(lambda x: len(x) % 2 == 0, text))

filtered_as_string = " ".join(filtered)

print(*filtered_as_string.split(), sep='\n')
