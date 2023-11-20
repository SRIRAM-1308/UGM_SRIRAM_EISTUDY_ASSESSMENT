class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.assignments = []

    def add_student(self, student):
        self.students.append(student)
        return f"Student {student.name} has been enrolled in {self.name}."

    def list_students(self):
        for student in self.students:
            print(student)

    def schedule_assignment(self, assignment):
        self.assignments.append(assignment)
        return f"Assignment for {self.name} has been scheduled."

class Student:
    def __init__(self, name):
        self.name = name
        self.assignments = {}

    def submit_assignment(self, classroom, assignment, submission):
        if assignment in classroom.assignments:
            self.assignments[assignment] = submission
            return f"Assignment submitted by Student {self.name} in {classroom.name}."

class VirtualClassroomManager:
    def __init__(self):
        self.classrooms = []

    def add_classroom(self, classroom):
        self.classrooms.append(classroom)
        return f"Classroom {classroom.name} has been created."

    def list_classrooms(self):
        for classroom in self.classrooms:
            print(classroom.name)

    def remove_classroom(self, classroom):
        self.classrooms.remove(classroom)

def main():
    manager = VirtualClassroomManager()
    while True:
        command = input("Enter command (add_classroom, add_student, schedule_assignment, submit_assignment, exit): ")
        if command == "add_classroom":
            name = input("Enter classroom name: ")
            classroom = Classroom(name)
            print(manager.add_classroom(classroom))
        elif command == "add_student":
            student_name = input("Enter student name: ")
            classroom_name = input("Enter classroom name: ")
            student = Student(student_name)
            classroom = next((c for c in manager.classrooms if c.name == classroom_name), None)
            if classroom:
                print(classroom.add_student(student))
            else:
                print("Classroom not found.")
        elif command == "schedule_assignment":
            assignment = input("Enter assignment details: ")
            classroom_name = input("Enter classroom name: ")
            classroom = next((c for c in manager.classrooms if c.name == classroom_name), None)
            if classroom:
                print(classroom.schedule_assignment(assignment))
            else:
                print("Classroom not found.")
        elif command == "submit_assignment":
            student_name = input("Enter student name: ")
            classroom_name = input("Enter classroom name: ")
            assignment = input("Enter assignment details: ")
            submission = input("Enter submission details: ")
            student = Student(student_name)
            classroom = next((c for c in manager.classrooms if c.name == classroom_name), None)
            if classroom:
                print(student.submit_assignment(classroom, assignment, submission))
            else:
                print("Classroom not found.")
        elif command == "exit":
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
