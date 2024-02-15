# https://www.youtube.com/watch?v=ahiM09ZhBdI&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=19
'''
1 - Define a class Queue to implement queue data structure using singly linked list. Define __init__() method to initialize fron and rear reference variable and item_count variable to keep track of number of elements in the queue.
2 - Define a method is_empty() to check if the queue is empty in Queue class.
3 - In Queue class, define enqueue() method to add data at the read end of the queue.
4 - In Queue class, define dequeue() method to remove front element from the queue.
5 - In Queue class, define get_front() method to reutrn front element of the queue.
6 - In Queue class, define get_read() method to return rear elemento of the queue.
7 - In Queue class, define size() method to return size of the queue that is the number of items present in the queue.
'''
class Node:
    def __init__(self, item=None, next=None) -> None:
        self.item = item
        self.next = next

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.item_count = 0
        self.items = []
    
    def is_empty(self):
        return self.front == None

    def enqueue(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count += 1

    def dequeue(self):
        # checking if queue is empty
        if self.is_empty():
            raise IndexError("Queue Underflow")
        # checking if queue has only one element
        elif self.rear == self.front:
            self.front = None
            self.rear = None
        # when queue has more than one element
        else:
            self.front = self.front.next
        self.item_count -= 1


    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Queue Underflow")
        
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("Queue Underflow")

    def size(self):
        return self.item_count

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