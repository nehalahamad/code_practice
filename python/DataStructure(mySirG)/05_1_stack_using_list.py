# https://www.youtube.com/watch?v=2H8QmXhVvoY&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=13
'''
01 - Define a class Stack to implement stack data structure using list. Define __init__() method to create an empty list object as instance object member of Stack.
02 - Defina a method is_empty() to check if the stack is mpty in Stack class.
03 - In Stack class, define push() method to add data onto to the stack.
04 - In Stack class, define pop() method to top element from the stack.
05 - In Stack class, define peek() method to return top element on the stack.
06 - in Stack class, define size() method to reutrn size of the stack ithat is number of items present in the stack.
'''

class Stack:
    def __init__(self) -> None:
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is Empty")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is Empty")
    def size(self):
        return len(self.items)
    
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("top element is: ", s1.peek())
print("removed element is: ", s1.pop())
print("top element is: ", s1.peek())

