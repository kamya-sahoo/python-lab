
students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("\nEnter student name: ")
    marks = float(input("Enter marks (out of 100): "))

    if marks < 0 or marks > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        continue

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    students[name] = {
        "Marks": marks,
        "Grade": grade
    }

print("\n----- STUDENT REPORT -----")

for name, details in students.items():
    print("\nName:", name)
    print("Marks:", details["Marks"])
    print("Grade:", details["Grade"])
