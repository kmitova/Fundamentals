def characters_between(char1str, char2str):
    char1 = ord(char1str)
    char2 = ord(char2str)
    characters = []
    for char in range(char1+1, char2):
        characters.append(chr(char))
    as_string = " ".join(characters)
    return as_string


character_1 = input()
character_2 = input()
result = characters_between(character_1, character_2)
print(result)
