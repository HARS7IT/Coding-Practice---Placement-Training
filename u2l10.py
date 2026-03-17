score= int(input("Enter your marks(0-100): "))
attendance= int(input("Enter your attendance(0-100): "))
submitted = True

if score>=80:
    if attendance>=60:
        if submitted:
            print("Pass with good marks")
        else:
            print("Pass without submission")
    else:
        print("Pass without attendance")
else:
    print("Failed")