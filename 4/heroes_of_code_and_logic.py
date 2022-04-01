num = int(input())

heroes = {}

for i in range(num):
    info = input().split()
    name = info[0]
    hp = int(info[1])
    mp = int(info[2])
    heroes[name] = [hp, mp]

command = input()
while not command == "End":
    current = command.split(" - ")
    action = current[0]
    name = current[1]
    if action == "CastSpell":
        mp_needed = int(current[2])
        spell = current[3]
        if mp_needed <= heroes[name][1]:
            heroes[name][1] -= mp_needed
            print(f"{name} has successfully cast {spell} and now has {heroes[name][1]} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell}!")
    elif action == "TakeDamage":
        damage = int(current[2])
        attacker = current[3]
        heroes[name][0] -= damage
        if heroes[name][0] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name][0]} HP left!")
        else:
            del heroes[name]
            print(f"{name} has been killed by {attacker}!")

    elif action == "Recharge":
        amount = int(current[2])
        old_mp = heroes[name][1]
        heroes[name][1] += amount
        if heroes[name][1] > 200:
            heroes[name][1] = 200
            diff = 200 - old_mp
            print(f"{name} recharged for {diff} MP!")
        else:
            print(f"{name} recharged for {amount} MP!")

    elif action == "Heal":
        amount = int(current[2])
        old_hp = heroes[name][0]
        heroes[name][0] += amount
        if heroes[name][0] > 100:
            heroes[name][0] = 100
            diff = 100 - old_hp
            print(f"{name} healed for {diff} HP!")
        else:
            print(f"{name} healed for {amount} HP!")

    command = input()

for name, value in heroes.items():
    print(f"{name}")
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")

