from collections import defaultdict, Counter, namedtuple, deque

# namedtuple for student structure
import json
import os
Student = namedtuple("Student", ["id", "name"])

class StudentActivitySystem:

    def __init__(self):
        self.students = {}                      # student_id -> Student
        self.activities = defaultdict(list)     # student_id -> activities
        self.activity_count = Counter()         # activity -> frequency
        self.recent_activities = deque(maxlen=5)  # last 5 activities

    def add_student(self, sid, name):
        self.students[sid] = Student(sid, name)
        print(f"Student added: {name}")

    def log_activity(self, sid, activity):
        if sid not in self.students:
            print("Student not found!")
            return

        self.activities[sid].append(activity)
        self.activity_count[activity] += 1
        self.recent_activities.append((sid, activity))

        print(f"Activity logged: {activity}")

    def show_student_activity(self, sid):
        print(f"\nActivities of {self.students[sid].name}:")
        print(self.activities[sid])

    def most_common_activity(self):
        print("\nMost common activity:")
        print(self.activity_count.most_common(1))

    def show_recent_activities(self):
        print("\nRecent Activities:")
        for sid, act in self.recent_activities:
            print(self.students[sid].name, "->", act)


# ---------------- MAIN ---------------- #

app = StudentActivitySystem()

app.add_student(1, "Harshit")
app.add_student(2, "Aman")

app.log_activity(1, "Login")
app.log_activity(2, "Login")
app.log_activity(1, "Quiz")
app.log_activity(1, "Logout")
app.log_activity(2, "Quiz")
app.log_activity(1, "Login")

app.show_student_activity(1)
app.most_common_activity()
app.show_recent_activities()


