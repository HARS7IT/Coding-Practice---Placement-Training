#Queue:

class queueOperations:
    def __init__(self):
        self.queue=[]
    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        if self.queue==[]:
            print("Queue is underflow")
        else:
            self.queue.pop(0)

    def display(self):
        if self.queue==[]:
            print("Queue is empty")
        else:
            for i in range(len(self.queue)):
                print(self.queue[i])

obj=queueOperations()
obj.enqueue(10)
obj.enqueue(20)
obj.display()