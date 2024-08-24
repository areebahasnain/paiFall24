marks = {
    "Physics": int(input("Enter marks for Physics: ")),
    "Chemistry": int(input("Enter marks for Chemistry: ")),
    "Maths": int(input("Enter marks for Maths: "))
}

total_marks = marks["Physics"] + marks["Chemistry"] + marks["Maths"]
average_marks = total_marks / len(marks)

highest_marks_subject = ""
highest_marks = 0

for subject, mark in marks.items():
    if mark > highest_marks:
        highest_marks = mark
        highest_marks_subject = subject

print("Average Marks:", average_marks)
print("Highest Marks in:", highest_marks_subject)