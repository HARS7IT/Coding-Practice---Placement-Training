#stack
# it is a linear data structure.
# it follows LIFO approach.
# stack has only one end, called top end.
# if top == size-1, then the stack is full.
# push function cant be called here.
# if we push full stack, the it will cause stack overflow.
# if top == -1, then we cant call pop function since stack is empty.
# if we pop empty stack, the it willc ause stack underflow.

#Operations on stack:
# 1. Push= It is used to insert the data into the stack.
# 2. Pop= It is used to delete the data from the stack.
# 3. Peak= It returns the topmost element from the stack.

class StackOperations:

    def __init__(self):
        self.stack=[]

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if self.stack == []:
                print("Stack underflow")
        else:
             self.stack.pop()

    def display(self):
        if self.stack == []:
            print("Stack is empty")
        else:
            for top in range(len(self.stack)-1,-1,-1):
                print(self.stack[top])

obj=StackOperations()
while True:
     
    your_choice=int(input("Enter your choice(1,2,3): "))
    if your_choice == 1:
        data= int(input("Enter your data: "))
        obj.push(data)
    elif your_choice ==2:
        obj.pop()
    elif your_choice == 3:
        obj.display()
    else:
        print("Invalid choice")
        break

# applications:
# undo & redo
# transaction history


         
