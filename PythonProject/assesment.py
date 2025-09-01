"""
Add students
View Students
Update Students
Delete Students
Exit
"""

students = [
    {"Id": 1, "Name": "Alice", "Age": 20, "Email": "alice@gmail.com"},
    {"Id": 2, "Name": "Bob", "Age": 22, "Email": "bob@gmail.com"},
    {"Id": 3, "Name": "Angel", "Age": 21, "Email": "angel@gmail.com"}
]
def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    email = input("Enter student email: ")
    id = students[-1]["Id"] + 1
    students.append({"Id": id, "Name": name, "Age": age, "Email": email})

def view_students():
    for student in students:
        print(student)

def update_student():
    student_id = int(input("enter student id:"))
    for student in students:
        if student["Id"] == student_id:
            name = input ("Enter new name: ")
            age = input("Enter new age: ")
            email = input("Enter new email: ")
            student["Name"] = name
            student["Age"] = age
            student["Email"] = email

def delete_student():
    student_id = int(input("enter student id: "))
    for student in students:
        if student["Id"] == student_id:
            students.remove(student)
            break

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")         