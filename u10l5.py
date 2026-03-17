from collections import deque

# ------------------ STUDENT CLASS ------------------
class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.grade = None

    def assign_grade(self, grade):
        self.grade = grade

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Grade: {self.grade}")


# ------------------ QUEUE MANAGEMENT ------------------
class GradeQueue:
    def __init__(self):
        self.queue = deque()   # Queue of students

    # Add student to queue
    def add_student(self, student):
        self.queue.append(student)
        print(f"{student.name} added to grade entry queue.")

    # Enter grade (FIFO)
    def enter_grade(self, grade):
        if not self.queue:
            print("No students waiting.")
            return

        student = self.queue.popleft()
        student.assign_grade(grade)
        print(f"Grade entered for {student.name}: {grade}")
        return student

    # Display waiting students
    def display_queue(self):
        if not self.queue:
            print("Queue is empty.")
        else:
            print("\nStudents waiting for grade entry:")
            for student in self.queue:
                print(f"{student.roll_no} - {student.name}")


# ------------------ MAIN PROGRAM ------------------
grade_queue = GradeQueue()

# Creating students
s1 = Student(101, "Aman")
s2 = Student(102, "Riya")
s3 = Student(103, "Kunal")

# Add students to queue
grade_queue.add_student(s1)
grade_queue.add_student(s2)
grade_queue.add_student(s3)

# Display queue
grade_queue.display_queue()

# Enter grades
grade_queue.enter_grade("A")
grade_queue.enter_grade("B")

# Display updated students
print("\nUpdated Student Records:")
s1.display()
s2.display()
s3.display()

# Display remaining queue
grade_queue.display_queue()
