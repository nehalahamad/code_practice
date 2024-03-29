
class Stack(list):
    def is_empty(self):
        return len(self) == 0
    def push(self, data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is Empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError(" Stack is Empty")
    def size(self):
        return len(self)
    def insert(self, index, data):
        raise AttributeError(" No attribute 'insert'")
    
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("top element is: ", s1.peek())
print("removed element is: ", s1.pop())
print("top element is: ", s1.peek())
s1.insert(2, 55)