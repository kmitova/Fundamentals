text = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']

no_vowels = [el for el in text if el not in vowels]
final_string = "".join(no_vowels)
print(final_string)
