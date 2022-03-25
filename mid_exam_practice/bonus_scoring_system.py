from math import ceil

number_of_students = int(input())

total_n_of_lectures = int(input())

additional_bonus = int(input())
max_attendance = 0
max_bonus = 0
total_bonus = 0
for student in range(number_of_students):
    attendance_of_student = int(input())
    total_bonus = (attendance_of_student / total_n_of_lectures) * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_attendance = attendance_of_student

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {max_attendance} lectures.")
