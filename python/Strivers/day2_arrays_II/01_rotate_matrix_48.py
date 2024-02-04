from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # rotating to principal diagonal
        for i in range(n):
            for j in range(n):
                if i > j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # rotationg to y axix
        for i in range(n):
            for j in range(n//2):
                matrix[i][j] , matrix[i][n-1-j]= matrix[i][n-1-j], matrix[i][j]
        return matrix
    
sol = Solution()
# Input: 
matrix = [[1,2,3],[4,5,6],[7,8,9]]  
output =  [[7,4,1],[8,5,2],[9,6,3]]
res = sol.rotate(matrix)
assert res == output