budget = float(input())
one_kg_flour_price = float(input())
eggs_price = one_kg_flour_price * 0.75
one_l_milk_price = one_kg_flour_price + one_kg_flour_price * 0.25
milk_needed_price = 0.25 * one_l_milk_price
total_price = one_kg_flour_price + eggs_price + milk_needed_price
cozunacs = 0
eggs = 0


while budget >= total_price:
    cozunacs += 1
    eggs += 3
    if cozunacs % 3 == 0:
        eggs -= cozunacs - 2
    budget = budget - total_price

print(f"You made {cozunacs} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.")