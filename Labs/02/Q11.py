def add_grade(student_name, grade):
    if student_name in students_grades:
        students_grades[student_name].append(grade)
    else:
        print(f"Student {student_name} not found.")

def calculate_average(student_name):
    if student_name in students_grades:
        grades = students_grades[student_name]
        average = sum(grades) / len(grades)
        print(f"Average grade for {student_name}: {average:.2f}")
    else:
        print(f"Student {student_name} not found.")

def add_student(student_name):
    if student_name not in students_grades:
        students_grades[student_name] = []
        print(f"Student {student_name} added.")
    else:
        print(f"Student {student_name} already exists.")

def remove_student(student_name):
    if student_name in students_grades:
        del students_grades[student_name]
        print(f"Student {student_name} removed.")
    else:
        print(f"Student {student_name} not found.")

students_grades = {
    'Areeba': [85, 92, 88],
    'Emman': [78, 81, 85],
    'Hamza': [90, 87, 95]
} 

add_grade('Areeba', 95)
calculate_average('Areeba')

add_student('Ali')
add_grade('Ali', 88)
calculate_average('Ali')

remove_student('Emman')
print(students_grades)
