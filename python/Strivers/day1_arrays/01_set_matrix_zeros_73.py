from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        num_row, num_col = len(matrix), len(matrix[0])
        row_marked, col_marked = set(), set()
        for i in range(num_row):
            for j in range(num_col):
                if matrix[i][j] == 0:
                    row_marked.add(i)
                    col_marked.add(j)

        for i in range(num_row):
            for j in range(num_col):
                if i in row_marked or j in col_marked:
                    matrix[i][j] = 0
        print(matrix)

sol = Solution()
# Input: 
matrix = [[1,1,1],[1,0,1],[1,1,1]]   # Output: [[1,0,1],[0,0,0],[1,0,1]]
sol.setZeroes(matrix)
        