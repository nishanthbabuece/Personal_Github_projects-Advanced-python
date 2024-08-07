# practical applications, sorting, filtering, and mapping data

students = [
    {'name': 'Alice', 'grade': 'A'},
    {'name': 'Bob', 'grade': 'B'},
    {'name': 'Charlie', 'grade': 'C'}
]

sorted_students = sorted(students, key=lambda student: student['grade'])
print(sorted_students)