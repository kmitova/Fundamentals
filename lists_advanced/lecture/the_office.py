from statistics import mean

happiness_list = input().split()

happiness_improvement_factor = int(input())

multiplied_happiness_list = list(map(lambda x: int(x)*happiness_improvement_factor, happiness_list))


average = mean(multiplied_happiness_list)


happy_employees = list(filter(lambda x: x >= average, multiplied_happiness_list))


if len(happy_employees) >= len(multiplied_happiness_list)/2:
    print(f"Score: {len(happy_employees)}/{len(multiplied_happiness_list)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(multiplied_happiness_list)}. Employees are not happy!")
