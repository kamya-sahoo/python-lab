while True:

    print("\n----- STUDENT DATA MANAGER -----")
    print("1. Add Student Record")
    print("2. Display Student Records")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = input("Enter Marks: ")

        file = open("students.txt", "a")

        file.write(roll + "," + name + "," + marks + "\n")

        file.close()

        print("Student record added successfully!")

    elif choice == 2:

        try:
            file = open("students.txt", "r")

            print("\n----- STUDENT RECORDS -----")

            records = file.readlines()

            if len(records) == 0:
                print("No student records found!")

            else:
                for record in records:
                    print(record.strip())

            file.close()

        except FileNotFoundError:
            print("Student file does not exist!")

    elif choice == 3:

        print("Exiting Student Data Manager...")
        break

    else:
        print("Invalid choice! Try again.")