def rectangle(n):
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print()


def square(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()


def left_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print()


def right_triangle(n):
    for i in range(n):
        for j in range(i,n):
            print(" ",end="")
        for j in range(i+1):
            print("*",end="")
        print()


def center_triangle(n):
      for i in range(n):
        for j in range(i,n):
            print(" ",end="")
        for j in range(i):
            print("*",end="")
        for j in range(i+1):
            print("*",end="")
        print()


def diamond(n):
     for i in range(n-1):
        for j in range(i,n):
            print(" ",end="")
        for j in range(i):
            print("*",end="")
        for j in range(i+1):
            print("*",end="")
        print()
    
     for i in range(n):
        for j in range(i+1):
            print(" ",end="")
        for j in range(i,n-1):
            print("*",end="")
        for j in range(i,n):
            print("*",end="")
        print()

    
def decreasing_triangle(n):
    for i in range(n):
        for j in range(i,n):
            print("*",end="")
        print()


def menu():
    while True:
        print("\n------ STAR PATTERN GENERATOR ------")
        print("1. Rectangle")
        print("2. Square")
        print("3. Left Triangle")
        print("4. Right Triangle")
        print("5. Decreasing Triangle")
        print("6. Center Triangle")
        print("7. Diamond")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            n = int(input("Enter number of rows: "))

        if choice == "1":
            rectangle(n)
        elif choice == "2":
            square(n)
        elif choice == "3":
            left_triangle(n)
        elif choice == "4":
            right_triangle(n)
        elif choice == "5":
            decreasing_triangle(n)
        elif choice == "6":
            center_triangle(n)
        elif choice == "7":
            diamond(n)
        elif choice == "8":
            print("Thank you for using the Star Pattern Generator!")
            break
        else:
            print("Invalid choice! Try again.")

menu()
