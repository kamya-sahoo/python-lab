attendance = {}

n = int(input("Enter number of students: "))

for i in range(n):

    name = input("\nEnter student name: ")

    total_classes = int(input("Enter total classes: "))

    present = int(input("Enter classes attended: "))

    attendance[name] = {
        "Total Classes": total_classes,
        "Present": present,
        "Absent": total_classes - present
    }

print("\n----- ATTENDANCE REPORT -----")

for name, details in attendance.items():

    total = details["Total Classes"]
    present = details["Present"]

    if total > 0:
        percentage = (present / total) * 100
    else:
        percentage = 0

    print("\nStudent:", name)
    print("Total Classes:", total)
    print("Present:", present)
    print("Absent:", details["Absent"])
    print("Attendance:", round(percentage, 2), "%")

    if percentage >= 75:
        print("Status: Eligible")
    else:
        print("Status: Not Eligible")