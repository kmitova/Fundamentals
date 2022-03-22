command = input()
dictionary = {}

while command != 'end':
    tokens = command.split(' : ')
    course_name = tokens[0]
    student_name = tokens[1]

    if course_name not in dictionary.keys():
        dictionary[course_name] = [student_name]
    else:
        dictionary[course_name].append(student_name)

    command = input()

print(dictionary)
for course_name, registered_students in dictionary.items():
    print(f'{course_name}: {len(registered_students)}')
    for student_name in registered_students:
        print(f'-- {student_name}')