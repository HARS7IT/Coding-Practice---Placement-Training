#area.py

def area_calculator():
    print("Area Calculator")
    print("Choose shape: rectangle, circle, triangle")

    shape= input("Enter shape: ").lower()

    if shape == "rectangle":
        length= float(input("Enter length: "))
        width=float(input("Enter width: "))
        print("Area of rectangle: ",length*width)

    elif shape == "circle":
        radius = float(input("Enter radius: "))
        print("Area of circle: ", 3.14159*radius*radius)

    elif shape == "triangle":
        base=float(input("Enter base: "))
        height=float(input("Enter height: "))
        print("Area of triangle: ",0.5*base*height)

    else:
        print("Invalid shape")

area_calculator()