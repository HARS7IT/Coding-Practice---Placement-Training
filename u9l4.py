# Queue:
# Queue is a linear data structure.
# Queue follows FIFO approach
# Queue has two ends: rear and front
# Insertion is possible from rear end and deletion is possible from front end.
# Initially rear and front == -1, if rear == -1 or front == -1, it means queue is empty.
# if queue is empty, we cant call dequeue operation.
# Enqueue function can be called although.
# if rear == size-1, then queue is full.
# Enqueue func. cant be called when queue is full since it will cause queue overflow.
# Implementing double ended queue(deque):

from collections import deque
queue=deque([])
queue.append(10)
queue.appendleft(20)
print(queue)
