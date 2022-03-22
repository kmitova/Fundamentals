from math import ceil

people = int(input())
capacity = int(input())

full_courses = ceil(people / capacity)
print(full_courses)
