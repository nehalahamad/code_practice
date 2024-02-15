# https://www.youtube.com/watch?v=83MII3xl55c&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=25
'''
1 - Defina a class PriorityQueue to implement priority queue deta structure using list, provide __init__() method to create a list object (initially empty).
2 - Defina a push() method in PriorityQueue class to insert new data with given priority.
3 - Defina a pop() method in PriorityQueue class, which return the highest priority data stored in the prority queue data structure, Raise exception if priority queue is empty.
4 - Define is_empty() method in PriorityQueue class to check if the priority queue is empty.
5 - In class PriorityQueue, define a method size ot return the number of elements present in the priority queue.
'''


class PriorityQueue:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, data, priority):
        index = 0
        while index < len(self.items) and self.items[index][1] <= priority:
            index += 1
        self.items.insert(index, (data, priority))

    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is Empty")
        return self.items.pop(0)

    def size(self):
        return len(self.items)

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