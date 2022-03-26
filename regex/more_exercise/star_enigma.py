import re

number = int(input())
letters = ["s", "t", "a", "r", "S", "T", "A", "R"]
pattern = r"@([A-Z][a-z]+)[^@\-!:>]*:[^@\-!:>[0-9]*(\d+)![^@\-!:>]*([A|D])![^@\-!:>]*->[^@\-!:>[0-9]*(\d+)"
attacked = []
destroyed = []
for i in range(number):
    found_letters = []
    decrypted_message = ""
    key = 0
    message = input()

    for sym in message:
        if sym in letters:
            found_letters.append(sym)
    key = len(found_letters)
    for char in message:
        decrypted_message += chr(ord(char)-key)
    match = re.search(pattern, decrypted_message)
    if match:
        name = match.group(1)
        population = int(match.group(2))
        attack_type = match.group(3)
        soldiers = int(match.group(4))
        if attack_type == "A":
            attacked.append(name)
        elif attack_type == "D":
            destroyed.append(name)

attacked = sorted(attacked)
destroyed = sorted(destroyed)

print(f"Attacked planets: {len(attacked)}")
if len(attacked) > 0:
    for item in attacked:
        print(f"-> {item}")
print(f"Destroyed planets: {len(destroyed)}")
if len(destroyed) > 0:
    for item in destroyed:
        print(f"-> {item}")
