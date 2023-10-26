# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_len = 0
    def longestZigZag(self, root) -> int:
        def solve(root, l, r):
            if root is None: return

            self.max_len = max(self.max_len, l, r)

            solve(root.left, r+1, 0)
            solve(root.right, 0, l+1)
            return

        solve(root, 0, 0)
        return self.max_len