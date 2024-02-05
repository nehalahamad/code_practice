# https://www.youtube.com/watch?v=AebTLupMMdw&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=7
'''
01 - Define a class Node to describe a node of a doubly linked list.
02 - Defina a class DLL to implement Doubly Linked List with __init__() method to create and initialise start reference variable.

03 - Define a method is_empty() to check if the linked list is empty in DLL class.
04 - in class DLL, defina a method insert_at_start() to insert an element at the starting of the list.
05 - in class DLL, defina a method insert_at_last() to insert an element at the end of the list.
06 - in class DLL, defina a method search() to find the node with specified element value.
07 - in class DLL, defina a method insert_after() to insert new node after a given node of the list.
08 - In class DLL, defina a method to print all the elements fo the list.
09 - In class DLL, implement iterator for DLL to access all the elements of the list in sequence.
10 - In class DLL, implement delete_first()
11 - In class DLL, implement delete_last()
12 - In class DLL, implement delete_item()
'''
class Node:
    def __init__(self, prev=None, item=None, next=None) -> None:
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start=None) -> None:
        self.start = start

    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        n = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n
    
    def insert_at_last(self, data):
        temp = self.start
        if self.start != None:
            while temp.next != None:
                temp = temp.next
            n = Node(temp, data, None)
            if temp == None:
                self.start = n
            else:
                temp.next = n
    
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n

    def print_list(self):
        temp = self.start
        while temp:
            print(temp.item, end=' ')
            temp = temp.next

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

    def delete_last(self):
        if self.start is None:
            return None
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None
        
    def delete_item(self, data):
        if self.start is None:
            return
        else:
            temp = self.start
            while temp.next is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break
                temp = temp.next
    def __iter__(self):
        return DLLIterator(self.start)
    
class DLLIterator:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data

# ======================================
mylist = DLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_after(mylist.search(10), 15)
for x in mylist:
    print(x, end=" ")
