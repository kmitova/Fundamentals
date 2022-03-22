countries = input().split(", ")
capitals = input().split(", ")
dictionary = {k: v for k, v in zip(countries, capitals)}

for key, val in dictionary.items():
    print(f"{key} -> {val}")
