from typing import List 
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(r, c, i):
            for j in range(9):
                # checking in the row
                if board[r][j] == i:
                    return False
                # checking in the column
                if board[j][c] == i:
                    return False
                # checking in the small square
                if board[3*(r//3)+j//3][3*(c//3)+j%3] == i:
                    return False
            return True

        def solve():
            M, N = len(board), len(board[0])
            for r in range(M):
                for c in  range(N):
                    if board[r][c] == '.':
                        for i in range(1, 10):
                            if is_valid(r, c, str(i)):
                                board[r][c] = str(i)
                                if solve():
                                    return True
                                else:
                                    board[r][c] = '.'
                        return False
            return True

        solve()

s = Solution()
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(board)
for row in board:
    print(row)