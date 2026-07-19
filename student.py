# Student Management System

students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")

        student = {
            "name": name,
            "roll": roll
        }

        students.append(student)
        print("✅ Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("❌ No students found.")
        else:
            print("\n===== Student List =====")
            for i, student in enumerate(students, start=1):
                print(f"\nStudent {i}")
                print("Name :", student["name"])
                print("Roll :", student["roll"])

    elif choice == "3":
        print("👋 Thank you! Exiting program...")
        break

    else:
        print("❌ Invalid choice! Please enter 1, 2, or 3.")