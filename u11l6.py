matrix=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

print("Element at [1][2]: ", matrix [1][2])
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix [{i}][{j}] = {matrix[i][j]}")

students={
    "Alice":{
        "age": 21,
        "courses": {"Maths", "Physics","Maths"},
        "marks": [85,90,78]
    },
    "Bob":{
        "age": 22,
        "courses": {"Chemistry", "Biology"},
        "marks": [75,80,90]
    }
}

for name,info in students.items():
    print(f"\nStudent: {name}")
    print("Age:", info["age"])
    print("Courses:", info["courses"])
    print("Marks:", info["marks"])
    




