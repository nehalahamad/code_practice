# https://www.youtube.com/watch?v=ahiM09ZhBdI&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=19
'''
1 - Define a class Queue to implement queue data structure using list. Define __init__() method to create an empty list object as instance object member of Queue.
2 - Define a method is_empty() to check if the queue is empty in Queue class.
3 - In Queue class, define enqueue() method to add data at the read end of the queue.
4 - In Queue class, define dequeue() method to remove front element from the queue.
5 - In Queue class, define get_front() method to reutrn front element of the queue.
6 - In Queue class, define get_read() method to return rear elemento of the queue.
7 - In Queue class, define size() method to return size of the queue that is the number of items present in the queue.
'''

class Queue:
    def __init__(self) -> None:
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, data) :
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Queue Underflow")

    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue Underflow")
        
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue Underflow")

    def size(self):
        return len(self.items)

# ================================
q = Queue()
try:
    print(q.get_front())
except Exception as e:
    print(e)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print(f"Fron={q.get_front()}, rear={q.get_rear()}")
try:
    q.dequeue()
    print(f"Queue has now: {q.size()} elements")
except IndexError as e:
    print(e)