from typing import List
import collections

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent_to_children = collections.defaultdict(list)
        child_to_parent = {}
        for node in range(n):
            left, right = leftChild[node], rightChild[node]
            if left != -1:
                parent_to_children[node].append(left)
                if left not in child_to_parent:
                    child_to_parent[left] = node
                else:
                    return False
            if right != -1:
                parent_to_children[node].append(right)
                if right not in child_to_parent:
                    child_to_parent[right] = node
                else:
                    return False
        
        # checking whether only on root candidate exist
        root_candidate = None
        for node in range(n):
            if node not in child_to_parent:
                if not root_candidate:
                    root_candidate = node
                else:
                    return False
        # if no root candidate exists, it means there exist cycle
        if root_candidate is None:
            return False
        # checking if tree is not disconnected
        visited = set()
        queue = collections.deque([root_candidate])
        while queue:
            current_node = queue.popleft()
            visited.add(current_node)
            for child in parent_to_children[current_node]:
                queue.append(child)
        return len(visited) == n
    
s = Solution()
n, leftChild, rightChild = 4, [1,-1,3,-1], [2,-1,-1,-1] # output=True
res = s.validateBinaryTreeNodes(n, leftChild, rightChild)
print(res)