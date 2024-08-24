marks = {
    "subject1": int(input("Enter marks for Subject 1: ")),
    "subject2": int(input("Enter marks for Subject 2: ")),
    "subject3": int(input("Enter marks for Subject 3: "))
}

subject1 = marks["subject1"]
subject2 = marks["subject2"]
subject3 = marks["subject3"]

total_marks = subject1 + subject2 + subject3
average_marks = total_marks / len(marks)
percentage = (total_marks / 300) * 100

print("Marks Dictionary:", marks)
print("Average Marks:", average_marks)
print("Percentage:", percentage, "%")
