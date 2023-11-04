class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def print(self):
        if self.head is None:
            print('Linkedlist is empty')
            return
        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.next
        print(listr)
    
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)
        
    def insert_values(self, data_list):
        for item in data_list:
            self.insert_at_end(item)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at(self, index):
        if index < 0  or index >= self.get_length():
            raise Exception('Invalid Index')
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                return
            itr = itr.next
            count += 1
        
    def insert_at(self, index, data):
        if index < 0  or index >= self.get_length():
            raise Exception('Invalid Index')
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
                
            itr = itr.next
            count += 1
            
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            raise Exception('Empty Linkedlist')
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next
        if itr is None:
            print(f'value {data_after}, does not exist')
    
    def remove_by_value(self, data):
        if self.head is None:
            raise Exception('Empty Linkedlist')
        if self.head.data == data:
            self.head = None
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def oddEvenList(self):
        head = self.head
        if head is None or head.next is None or head.next.next is None:
            return head
        
        end = head
        count = 0
        while end.next:
            count += 1
            end = end.next
        count += 1

        ptr = head
        for i in range(count//2):
            end.next = ptr.next
            ptr.next = ptr.next.next
            end.next.next = None
            ptr = ptr.next
            end = end.next
        return head  
#     ----------------
    def reverse_1(self):
        pre = None
        cur = self.head
        nex = cur.next
        while nex:
            cur.next = pre
            pre = cur
            cur = nex
            nex = nex.next
        cur.next = pre
        self.head = cur
    
    def reverse(self):
        pre, cur = None, self.head
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        self.head = pre
        

    
        
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values([1,2,3,4,5])
    ll.reverse()
    ll.print()