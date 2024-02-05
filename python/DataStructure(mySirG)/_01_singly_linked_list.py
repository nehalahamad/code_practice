# https://www.youtube.com/watch?v=ZJW4eQcywYY&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=5
'''
01 - Define a class Node to describe a node of singly linked list.
02 - Define a class SLL to implement Singly Linked List with __init__() method to create and initialise start reference variable.
03 - Defina a method is_empty() to check if the linked list is empty in SLL class.
04 - In class SLL, define a method insert_at_start() to insert an element at the starting of the list.
05 - In class SLL, define a method insert_at_last() to insert an element at the end of the list.
06 - In class SLL, define a method search() to find the node with specified element value.
07 - In class SLL, define a method inset_after() to insert a new node after a given node to the list.
08 - In class SLL, define a method print_list()to print all the elements of the list

09 - In class SLL, implement iterator for SLL to access all the elements fo the list in a sequence.
10 - In class SLL, define a method delete_first() to delelte first element from the list.
11 - In class SLL, define a method delete_last() to delete last element from the list.
12 - In class SLL, define a method delete_item() to delete given element from the list.

'''
class Node:
    def __init__(self, item=None, next=None) -> None:
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None) -> None:
        self.start = start
    
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

    def insert_at_last(self, data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
        print()
    
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next:
                temp = temp.next
            temp.next = None
    
    def delete_item(self, data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start
            if temp.item == data:
                self.start = None
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
                
    def __iter__(self):
        return SLLIterator(self.start)

class SLLIterator:
    def __init__(self, start) -> None:
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data

if __name__ == "__main__":
    mylist = SLL()
    mylist.insert_at_start(20)
    mylist.insert_at_start(10)
    mylist.insert_at_last(30)
    mylist.insert_after(mylist.search(20), 25)
    mylist.print_list()
    mylist.delete_item(20)
    mylist.print_list()

    for x in mylist:
        print(x, end=' ')