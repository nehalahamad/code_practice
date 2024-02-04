# https://www.youtube.com/watch?v=OkH3I6XvkoI&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=9
"""
01 - Define a class Node to describe a node of a circular linked list.
02 - Define a class CLL to inplement Circular Linked List with __init__() method to create and initialise last reference variable.
03 - Define a mthod is_empty() to check if the linked list is empty in CLL class.
04 - In class CLL, define a method insert_at_start() to inserrt an element at the starting of the list.
05 - In class CLL, define a method insert_at_last() to inserrt an element at the ednd of the list.
06 - In class CLL, define a method search() to find the node with specified element value.
07 - In class CLL, define a method insert_after() to insert a node after given node of the list.
08 - In class CLL, define a method to print all the element of the list.

09 - In class CLL, implement iterator for CLL to access all the elements of the list in a
10 - delete_first()
11 - delete_last()
12 - delete_item()
"""
class Node:
    def __init__(self, item=None, next=None) -> None:
        self.item = item
        self.next = next

class CLL:
    def __init__(self, last=None) -> None:
        self.last = last

    def is_empty(self):
        return self.last == None
    
    def insert_at_start(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
    
    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n
    def search(self, data):
        if self.is_empty():
            return None
        temp = self.last.next
        while temp != self.last:
            if temp.item == data:
                return temp
            temp = temp.next
        if temp.item == data:
            return temp
        return None
    
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n
            # checking if  temp is the last node 
            if temp == self.last:
                self.last = n

    def print_list(self):
        if self.is_empty():
            return
        temp = self.last.next
        while temp != self.last:
            print(temp.item, end=' ')
            temp = temp.next
        print(temp.item)
    
    def delete_first(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next

    def delete_last(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next == self.last:
                    temp = temp.next    
                temp.next = self.last.next
                self.last = temp

    def delete_item(self, data):
        if not self.is_empty():
            # check if there is only one node in the CLL and that needs to be deleted
            if self.last.next == self.last:
                if self.last.item == data:
                    self.last = None
            else:
                # check if first node (after last node first node comes) needs to beleted
                if self.last.next.item == data:
                    self.delete_first()
                else:
                    temp = self.last.next
                    while temp != self.last:
                        # check if last node needs to be deleted
                        if temp.next == self.last:
                            if self.last.item == data:
                                self.delete_last()
                        if temp.next.item == data:
                            temp.next = temp.next.next
                            break
                        temp = temp.next

    def __iter__(self):
        if self.last == None:
            return CLLIterator(None)
        return CLLIterator(self.last.next)

class CLLIterator:
        def __init__(self, start) -> None:
            self.current = start
            self.start = start
            self.count = 0
        def __iter__(self):
            return self
        def __next__(self):
            if self.current == None:
                raise StopIteration
            if self.current == self.start and self.count == 1:
                raise StopIteration
            else:
                self.count = 1
            data = self.current.item
            self.current = self.current.next
            return data

# =========================================
cll = CLL()
cll.insert_at_start(10)
cll.insert_at_start(20)
cll.insert_at_last(30)
cll.insert_at_last(40)
cll.insert_after(cll.search(10), 50)

for x in cll:
    print(x, end=' ')
# cll.print_list()
