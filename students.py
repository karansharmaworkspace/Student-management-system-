class Student:
    all_students = []
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def menu():
        print("\n ========= Student Management System ========")
        print("1. Add Student")
        print("2. Update Marks")
        print("3. Show All Students")
        print("4. Exit")

        choice = int(input("Enter your choice(1-4): "))
        if choice == 1:
            name = input("Enter student name: ")
            roll_number = int(input("Enter student roll number: "))
            grade = float(input("Enter student grade: "))
            student = Student(name, roll_number, grade)
            Student.all_students.append(student)
            print("Student added successfully!")
        elif choice == 2:
            roll_number = int(input("Enter student roll number to update marks: "))
            for student in Student.all_students:
                if student.roll_number == roll_number:
                    new_grade = float(input("Enter new grade: "))
                    student.grade = new_grade
                    print("Marks updated successfully!")
                    break
            else:
                print("Student not found!")
        elif choice == 3:
            if not Student.all_students:
                print("No students found!")
            else:
                print("\nList of Students:")
                for student in Student.all_students:
                    print(f"Name: {student.name}, Roll Number: {student.roll_number}, Grade: {student.grade}")  
        elif choice == 4:
            print("Exiting the program. Goodbye!")
            exit()
        else:
         print("Invalid choice! Please enter a number between 1 and 4.")    

if __name__ == "__main__":
    while True:
        Student.menu() 
        