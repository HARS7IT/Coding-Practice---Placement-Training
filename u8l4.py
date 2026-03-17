try:
    x=int(input("Enter x:"))
    y=int(input("Enter y:"))
    if y>10:
        print(x/y)
    else:
        print(x+y)
except ZeroDivisionError:
    print("Please check y value")

except ValueError:
    print("Enter valid number")

except:
    print("Something went wrong")