my_details=("Harshit", 21, "Gaming Technology")
harshit_courses = {"CN", "Discrete Maths", "Computer Graphics", "FLA", "SRWC","DLGA"}
harshit_grades = {
    "CN": 90,
    "Discrete Maths": 95,
    "Computer Graphics": 91,
    "FLA": 90,
    "SRWC": 87,
    "DLGA": 89
}
print(f"Student:{my_details[0]}, Age: {my_details[1]}, Major: {my_details[2]}")
print("Courses:", harshit_courses)
print("Grades: ")
for subject, grade in harshit_grades.items():
    print(f"  {subject}:{grade}")