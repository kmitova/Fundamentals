students = int(input())
lectures = int(input())
add_bonus = int(input())
max_attendances = 0
bonus = 0
max_bonus = 0
for student in range(students):
    attendances = int(input())
    bonus = attendances / lectures * (5 + add_bonus)
    if bonus > max_bonus:
        max_bonus = bonus
        max_attendances = attendances

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {max_attendances} lectures.")