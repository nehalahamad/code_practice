# https://www.youtube.com/watch?v=qiMIQpVqRsU&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=33
# https://www.youtube.com/watch?v=ccRaMA_H32U&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=34
'''
1 - Defina a class Node with instance variables left, item and right. The variables left and right are used to refer left and right child node. The item variables is used to hold data item.
2 - Define a calss BST to implement Binary Search Tree data structure. Make __init__() method to create root instance variables ot hold the reference of root node.
3 - In class BST, define a insert method to store new data item in the binar search tree.
4 - In class BSt, define a search method to find a given item in the binary search tree and return the node reference. Ite reutrns Node if search failed.
5 - In class BST, define a method to implement inorder traversal.
6 - In class BST, define a method to implement preorder traversal.
5 - In class BST, define a method to implement postorder traversal.

6 - In class BST, defina a method to find minimum value item node.
7 - In class BST, define a mehtod to find maximum value item node.
8 - In class BST, define a method to delete a node from binary search teee.
9 - In class BST, define a method size to return the number of elements present in the BST.
'''

class Node:
    def __init__(self, item=None, left=None, right=None) -> None:
        self.left = left
        self.item = item
        self.right = right

class BST:
    def __init__(self) -> None:
        self.root = None
    # ---------------------------------------
    def insert(self, data):
        self.root = self._rinsert(self.root, data)
    def _rinsert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self._rinsert(root.left, data)
        elif data > root.item:
            root.right = self._rinsert(root.right, data)
        return root
    
    # ---------------------------------------
    def search(self, data):
        return self._rsearch(self.root, data)
    def _rsearch(self, root, data):
        if root is None or root.item == data:
            return root
        if data < root.item:
            return self._rsearch(root.left, data)
        else:
            return self._rsearch(root.right, data)
        
    # ---------------------------------------
    def inorder(self):
        result = []
        self._rinorder(self.root, result)
        return result
    def _rinorder(self, root, result):
        if root:
            self._rinorder(root.left, result)
            result.append(root.item)
            self._rinorder(root.right, result)

    # ---------------------------------------
    def preorder(self):
        result = []
        self._rpreorder(self.root, result)
        return result
    def _rpreorder(self, root, result):
        if root:
            result.append(root.item)
            self._rpreorder(root.left, result)
            self._rpreorder(root.right, result)

    # ---------------------------------------
    def postorder(self):
        result = []
        self._rpostorder(self.root, result)
        return result
    def _rpostorder(self, root, result):
        if root:
            self._rpostorder(root.left, result)
            self._rpostorder(root.right, result)
            result.append(root.item)

    # ---------------------------------------
    def min_value(self, temp):
        current = temp
        while current.left is not None:
            current = current.left
        return current.item
    
    # ---------------------------------------
    def max_value(self, temp):
        current = temp
        while current is not None:
            current = current.right
        return current.item
    
    # ---------------------------------------
    def delete(self, data):
        self.root = self._rdelete(self.root, data)
    def _rdelete(self, root, data):
        if root is None:
            return root
        if data < root.item:
            root.left = self._rdelete(root.left, data)
        elif data > root.item:
            root.right = self._rdelete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item = self.min_value(root.right)
            self._rdelete(root.right, root.item)
        return root

    # ---------------------------------------
    def size(self):
        return len(self.inorder())

# ===============================================================
if __name__ == "__main__":
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(80)
    bst.insert(10)
    bst.insert(40)
    bst.insert(60)
    bst.insert(100)
    bst.insert(70)
    bst.insert(90)
    bst.insert(65)
    bst.insert(75)
    bst.insert(72)
    print(bst.inorder())
    # print(bst.search(100))
    # print(bst.search(101))
    print("size of tree is: ", bst.size())
    bst.delete(40)
    print("size of tree is: ", bst.size())

