import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file doesnt exists")

#try and except methods
def problem():
    try:
        a=int(input("Enter the first num: "))
        b=int(input("enter the second num: "))
        print("Maximum num: ", max(a,b))
    except ValueError:
        print("Invalid digits not allowed")
problem()