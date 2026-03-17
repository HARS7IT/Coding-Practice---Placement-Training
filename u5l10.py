def myfunc(n):
    return lambda a:a*n
a=int(input("Enter the number to be doubled: "))
mydoubler=myfunc(2)
print(mydoubler(a))

numbers=[1,2,3,4,5]
doubled=list(map(lambda x:x*2, numbers))
print(doubled)

students=[("Emil",25),("toabius",22),("linius",28)]