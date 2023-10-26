from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        que = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        while que:
            i, j, step = que.popleft()
            if i==0 or i==len(maze)-1 or j==0 or j==len(maze[0])-1:
                if step > 0:
                    return step
            for di, dj in directions:
                if (0 <= i+di < len(maze)) and (0 <= j+dj < len(maze[0])) and (maze[i+di][j+dj] == '.'):
                    que.append((i+di, j+dj, step+1))
                    maze[i+di][j+dj]='+'
        return -1

            


maze = [
    ["+", "+", ".", "+"],
    [".", ".", ".", "+"],
    ["+", "+", "+", "."]]
entrance = [1,2]
maze =[
    ["+", ".", "+", "+", "+", "+", "+"],
    ["+", ".", "+", ".", ".", ".", "+"],
    ["+", ".", "+", ".", "+", ".", "+"],
    ["+", ".", ".", ".", "+", ".", "+"],
    ["+", "+", "+", "+", "+", ".", "+"]]
entrance = [0,1]

s = Solution()
res = s.nearestExit(maze, entrance)
print(res)