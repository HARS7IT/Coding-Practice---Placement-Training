#Recursion
def countdown(n):
    if n<=0:
        print("Done!")
    else:
        print(n)
        countdown(n-1)
countdown(6)

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(7))