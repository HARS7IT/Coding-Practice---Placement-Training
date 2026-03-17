def name():
    print("my name is Harshit")
    print("Department: CSE")
    print("College: SRM")
    print("City: Chennai")
name()
name()


def sum_num(x,y):#parameter with return value
    return(x+y)

a=int(input("Enter first num: "))
b=int(input("Enter second num: "))
result=sum_num(a,b)
print("Sum of two number: ",result)

def add_d(a=10,b=20):
    return(a+b)
add_d()
add_d(10)

