import re
pattern_health = r"[^\d+\-*\/\.]"
pattern_damage = r"(-*\d+\.*\d*)"
demons = input()
split = r"\s*,\s*|,\s*"
demons = sorted(re.split(split, demons))
results = {}
for demon in demons:
    health = 0
    damage = 0
    stars = 0
    slashes = 0
    matches_health = re.findall(pattern_health, demon)
    matches_damage = re.findall(pattern_damage, demon)
    multiplies_count = demon.count("*")
    divides_count = demon.count("/")
    for ch in matches_health:
        health += ord(ch)

    for ch in matches_damage:
        damage += float(ch)
    for i in range(0, multiplies_count):
        damage *= 2
    for i in range(0, divides_count):
        damage /= 2

    results[demon] = [health, damage]

sorted_results = sorted(results.items(), key=lambda kvp: kvp[0])

for key, value in sorted_results:
    print(f"{key} - {value[0]} health, {value[1]:.2f} damage")