from collections import deque

class deque_functions:

    def __init__(self):
        self.list= deque()

    def append_right(self, data):
        self.list.append(data)

    def append_left(self, data):
        self.list.appendleft(data)

    def display(self):
        print(self.list)

obj=deque_functions()
obj.append_right(4)
obj.append_left(5)
obj.display()

