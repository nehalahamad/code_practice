# https://www.youtube.com/watch?v=Xi451I6nC28&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=22
'''
01 - Define a class Deque to implement deque data strcture using list, Define __init__() method to create an empty list object as instance object member of Deque.
02 - Define a method is_empty() to check if the deque is empty in Deque class.
03 - in Deque class, define insert_front() method to add data at the fron endo of the deque.
04 - in Deque class, define insert_rear()
05 - in Deque class, define delete_front()
06 - in Deque class, define delete_rear()
07 - in Deque class, define get_front()
08 - in Deque class, define get_rear()
09 - in Deque class, define size()
'''

class Deque:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def insert_front(self, data):
        self.items.insert(0, data)

    def insert_rear(self, data):
        self.items.append(data)

    def delete_front(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Deque Underflow")

    def delete_rear(self):
        if not self.is_empty():
            self.items.pop()
        else:
            raise IndexError("Deque Underflow")
        
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Deque Underflow")
        
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Deque Underflow")

    def size(self):
        return len(self.items)

# ===========================================
dq = Deque()
dq.insert_front(10)
dq.insert_front(20)
dq.insert_rear(40)
dq.insert_front(30)
dq.insert_rear(50)
print(dq.get_front(), dq.get_rear())
