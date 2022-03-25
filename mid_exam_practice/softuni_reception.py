total_employees = 3

employee_1_ability_per_hour = int(input())
employee_2_ability_per_hour = int(input())
employee_3_ability_per_hour = int(input())

students_count = int(input())

total_ability_per_hour = (employee_1_ability_per_hour + employee_2_ability_per_hour + employee_3_ability_per_hour)

time = 0
rest = 0
requests_answered = 0
current_time = 0
for student in range(1, students_count+1):
    if total_ability_per_hour <= 0:
        time += 1
        total_ability_per_hour = (employee_1_ability_per_hour +
                                employee_2_ability_per_hour
                                + employee_3_ability_per_hour)

    total_ability_per_hour -= 1
    requests_answered += 1

    if time % 3 == 0 and not time == 0 and not time == current_time:
        current_time = time
        rest += 1

if students_count == 0:
    print(f"Time needed: {0 + rest}h.")
else:
    print(f"Time needed: {1+time+rest}h.")
