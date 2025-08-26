# Student Management System

student_db = {}

# Add Student
def add_student():
    print("=== Add Student ===")
    student_id = input("Enter Student ID: ")
    if student_id in student_db:
        print("Student ID already exists!\n")
    else:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        student_db[student_id] = {"name": name, "age": age, "gender": gender}
        print("Student added successfully!\n")

# Delete Student
def delete_student():
    print("=== Delete Student ===")
    student_id = input("Enter Student ID: ")
    if student_id in student_db:
        del student_db[student_id]
        print("Student deleted successfully!\n")
    else:
        print("Student ID not found!\n")

# Update Student
def update_student():
    print("=== Update Student ===")
    student_id = input("Enter Student ID: ")
    if student_id in student_db:
        print("What do you want to update?")
        print("1. Name")
        print("2. Age")
        print("3. Gender")
        choice = input("Enter choice (1-3): ")
        
        if choice == "1":
            new_name = input("Enter new name: ")
            student_db[student_id]["name"] = new_name
        elif choice == "2":
            new_age = int(input("Enter new age: "))
            student_db[student_id]["age"] = new_age
        elif choice == "3":
            new_gender = input("Enter new gender: ")
            student_db[student_id]["gender"] = new_gender
        else:
            print("Invalid choice!")
            return
        
        print("Student updated successfully!\n")
    else:
        print("Student ID not found!\n")

# Display One Student
def display_one_student():
    print("=== Display One Student ===")
    student_id = input("Enter Student ID: ")
    if student_id in student_db:
        details = student_db[student_id]
        print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}, Gender: {details['gender']}\n")
    else:
        print("Student ID not found!\n")

# Display All Students
def display_all_students():
    print("=== All Student Records ===")
    if not student_db:
        print("No student records available.\n")
    else:
        for student_id, details in student_db.items():
            print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}, Gender: {details['gender']}")
        print()

# Search Student by Name
def search_student_by_name():
    print("=== Search Student by Name ===")
    name = input("Enter Name: ")
    found = False
    for student_id, details in student_db.items():
        if details["name"].lower() == name.lower():
            print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}, Gender: {details['gender']}")
            found = True
    if not found:
        print("No student found with that name.\n")
    print()

# Count Students
def count_students():
    print("=== Count Students ===")
    print(f"Total number of students: {len(student_db)}\n")

# Filter by Age
def filter_by_age():
    print("=== Filter by Age ===")
    age_limit = int(input("Enter age limit: "))
    found = False
    for student_id, details in student_db.items():
        if details["age"] > age_limit:
            print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}, Gender: {details['gender']}")
            found = True
    if not found:
        print("No students older than given age.\n")
    print()

# Main Menu
def start():
    while True:
        print("=== Student Management System ===")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. Display One Student")
        print("5. Display All Students")
        print("6. Search Student by Name")
        print("7. Count Students")
        print("8. Filter by Age")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            display_one_student()
        elif choice == "5":
            display_all_students()
        elif choice == "6":
            search_student_by_name()
        elif choice == "7":
            count_students()
        elif choice == "8":
            filter_by_age()
        elif choice == "9":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

# Run the program
start()
