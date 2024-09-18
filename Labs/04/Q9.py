class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display_student_info(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.name)


class Marks(Student):
    def __init__(self, student_id, name, marks_algo, marks_dataScience, marks_calculus):
        super().__init__(student_id, name)
        self.marks_algo = marks_algo
        self.marks_dataScience = marks_dataScience
        self.marks_calculus = marks_calculus

    def display_marks(self):
        print("Marks in Algorithm:", self.marks_algo)
        print("Marks in Data Science:", self.marks_dataScience)
        print("Marks in Calculus:", self.marks_calculus)


class Result(Marks):
    def __init__(self, student_id, name, marks_algo, marks_dataScience, marks_calculus):
        super().__init__(student_id, name, marks_algo, marks_dataScience, marks_calculus)

    def calculate_result(self):
        total_marks = self.marks_algo + self.marks_dataScience + self.marks_calculus
        average_marks = total_marks / 3
        print("Total Marks:", total_marks)
        print("Average Marks:", average_marks)


result = Result("23K-0059", "Areeba Hasnain", 80, 90, 85)

print("Student Information:")
result.display_student_info()

print("\nMarks:")
result.display_marks()

print("\nResult:")
result.calculate_result()