#Tuples in a dictionary

locations = {
    (10,20): "Park",
    (30,40): "Library",
    (50,60): "Cafe"
}

print("Location at (30,40):", locations[(30,40)])

#returning multiple values from a function:

def calculate(a,b):
    sum_val=a+b
    diff_val=a-b
    return(sum_val,diff_val)

result = calculate(10,5)
print("Sum is: ",result[0])
print("Difference is: ",result[1])

#Basic set creation

fruits={"apple","banana","cherry","apple"}
print("Fruits set: ",fruits)

fruits.add("orange")
print("After adding orange: ",fruits)

fruits.remove("apple")
print("After removing apple: ",fruits)