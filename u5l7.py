def maximum(a,b,c):
    if a>b and a>c:
        print("a is greater: ",a)
    elif b>a and b>c:
        print("b is greater: ",b)
    elif c>a and c>b:
        print("c is greater: ",c)
    else:
        print("Any two or more numbers are same")
a=int(input("Enter first number: "))
b=int(input("Enter second number:  "))
c=int(input("Enter third number: "))
maximum(a,b,c)