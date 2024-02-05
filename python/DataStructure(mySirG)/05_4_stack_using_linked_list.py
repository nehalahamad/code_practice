from _01_singly_linked_list import *

class Stack:
    def __init__(self) -> None:
        self.mylist = SLL()
        self.item_count = 0
    
    def is_empty(self):
        return self.mylist.is_empty()
    
    def push(self, data):
        self.mylist.insert_at_start(data)
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            data = self.mylist.start.item
            self.mylist.delete_first()
            self.item_count -= 1
            return data
        else:
            raise IndexError("Stack is Empty")
        
    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item
        else:
            raise IndexError("Stack is Empty")
        
    def size(self):
        return self.item_count
    
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("top element is: ", s1.peek())
print("total element in stack: ", s1.size())
print("removed element is: ", s1.pop())
print("top element is: ", s1.peek())
print("total element in stack: ", s1.size())