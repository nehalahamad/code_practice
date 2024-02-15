# https://www.youtube.com/watch?v=-lbbPPnToLM&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=26
'''
1 - Defina a class PriorityQueue to implement priority queue deta structure using linked list, provide __init__() method to create a list object (initially empty).
2 - Defina a push() method in PriorityQueue class to insert new data with given priority.
3 - Defina a pop() method in PriorityQueue class, which return the highest priority data stored in the prority queue data structure, Raise exception if priority queue is empty.
4 - Define is_empty() method in PriorityQueue class to check if the priority queue is empty.
5 - In class PriorityQueue, define a method size ot return the number of elements present in the priority queue.
'''
class Node:
    # item with lower priority value are consider to be highest priority
    def __init__(self, item=None, priority=None, next=None) -> None:
        self.item = item
        self.priority = priority
        self.next = next

class PriorityQueue:
    def __init__(self) -> None:
        self.start = None
        self.item_count = 0

    def is_empty(self):
        return self.start is None
    
    def push(self, data, priority):
        n = Node(data, priority)
        # chcking if queue is empty or has only one item
        if (self.start is None) or (priority < self.start.priority):
            n.next = self.start
            self.start = n
        # if queue has more that one item
        else:
            temp = self.start
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.item_count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        data = self.start.item
        self.start = self.start.next
        return data


    def size(self):
        return self.item_count

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push("Amit", 4)
    pq.push("Arjun", 7)
    pq.push("Ashima", 2)
    pq.push("Agrah", 5)
    pq.push("Anant", 8)
    pq.push("Ambika", 1)

    while not pq.is_empty():
        print(pq.pop())