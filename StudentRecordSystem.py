# Define a class for Student
class Student:
    def __init__(self,name):
        self.name = name
        self.grades = []

    def add_garde(self, grade):
        self.grades.append(grade)

    def get_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

# Define a class for Student

class Teacher:
    def __init__(self):
        self.students= []

    def add_student(self,student_name):
        student = Student(student_name)
        self.students.append(student)
        print(f"✅ Student '{student_name}' added.")

    def assign_grade(self, student_name, grade):
        for student in self.students:
            if student.name == student_name:
                student.add_garde(grade)
                print(f"✅ Grade {grade} add to {student_name}.")
                return
            print(f"⚠️ Student '{student_name}' not found.")
    def show_report(self):
        print("\n📊 Student Report:")
        for student in self.students:
            avg = student.get_average()
            print(f"- {student.name}: Grades = {student.grades}, Average = {avg:.2f}")


#main program
teacher= Teacher()

while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Assign Grade")
    print("3. Show Report")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input(" Enter student name :  ")
        teacher.add_student(name)

    elif choice =="2":
        name = input(" Enter student name :  ")
        try:
            grade = float(input("enter grade (0-100): "))
            teacher.assign_grade(name, grade)
        except ValueError:
            print("⚠️ Invalid grade. Please enter a number.")

    elif choice =="3":
        teacher.show_report()

    elif choice == "4":
        print("👋 Exiting program.")
        break

    else:
        print("❗ Invalid option. Try again.")






