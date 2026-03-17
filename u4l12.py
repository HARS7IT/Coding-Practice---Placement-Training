#combining

student=("Bob", 22, "Mechanical Engineering")

bob_courses = {"Mechanics","Thermodynamics","Math"}

bob_grades = {
    "Mechanics": 90,
    "Thermodynamics": 85,
    "Math": 80
}

print(f"Student:{student[0]}, Age: {student[1]}, Major: {student[2]}")
print("Courses:", bob_courses)
print("Grades: ")
for subject, grade in bob_grades.items():
    print(f"  {subject}:{grade}")


