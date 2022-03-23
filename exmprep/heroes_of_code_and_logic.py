lines = int(input())

heroes = {}

for n in range(lines):
    data = input()
    current = data.split()
    name = current[0]
    hp = int(current[1])
    mp = int(current[2])
    heroes[name] = [hp, mp]

command = input()

while not command == "End":
    current = command.split(" - ")
    action = current[0]
    name = current[1]
    if action == "CastSpell":
        mp_needed = int(current[2])
        spell_name = current[3]
        if heroes[name][1] >= mp_needed:
            available = heroes[name][1]
            left = available - mp_needed
            heroes[name][1] = left
            print(f"{name} has successfully cast {spell_name} and now has {left} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")
    elif action == "TakeDamage":
        damage = int(current[2])
        attacker = current[3]
        heroes[name][0] -= damage
        left = heroes[name][0]
        if heroes[name][0] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {left} HP left!")
        else:
            print(f"{name} has been killed by {attacker}!")
            del heroes[name]
    elif action == "Recharge":
        amount = int(current[2])
        old_mp = heroes[name][1]
        heroes[name][1] += amount
        if heroes[name][1] > 200:
            diff = 200 - old_mp
            heroes[name][1] = 200
            print(f"{name} recharged for {diff} MP!")
        else:
            print(f"{name} recharged for {amount} MP!")
    elif action == "Heal":
        amount = int(current[2])
        old_hp = heroes[name][0]
        heroes[name][0] += amount
        if heroes[name][0] > 100:
            diff = 100 - old_hp
            heroes[name][0] = 100
            print(f"{name} healed for {diff} HP!")
        else:
            print(f"{name} healed for {amount} HP!")
    command = input()

for key, value in heroes.items():
    print(key)
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")
