students_info = {}
data = input()
while data[0].isupper():
    current = data.split(":")
    name = current[0]
    id = int(current[1])
    course = current[2]
    students_info[name] = id, course
    data = input()

course_info = data
if len(course_info) > 1:
    course_info = course_info.split("_")
    first = course_info[0]
    for key, value in students_info.items():
        if first in value[1]:
            print(f"{key} - {value[0]}")
else:
    for key, value in students_info.items():
        if course_info in value:
            print(f"{key} - {value[0]}")
