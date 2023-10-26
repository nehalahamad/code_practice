from typing import List
from collections import defaultdict, deque

class Solution:
    def shortestPathAllKeys_1(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        key_count = 0
        start_position = (0, 0)
        que = deque([])
        for i in range(m):
            for j in range(n):
                if 'a' <= grid[i][j] <= 'f':
                    key_count += 1
                elif grid[i][j] == '@':
                    start_position = (i, j)
        visited = set()
        keys = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0} # 'A':0 -- is locked,     'A':1 -- is unlocked
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        que.append([start_position[0], start_position[1], key_count, 0, keys, visited])
        while que:
            size = len(que)
            for _ in range(size):
                i, j, key_count, steps, keys, visited = que.popleft()
                cur = grid[i][j]
                visited.add((i, j, key_count))
                if key_count == 0:
                    return steps - 1
                else:
                    if 'A'<=cur<='F' and keys[cur]==0 or cur=='#':
                        continue
                    if 'a'<=cur<='f':
                        if not keys[cur.upper()]:
                            keys[cur.upper()] = 1
                            key_count -= 1

                    for di, dj in directions:
                        x, y = i+di, j+dj
                        if 0<=x<m and 0<=y<n and (x, y, key_count) not in visited:
                            que.append([x, y, key_count, steps+1, keys.copy(), visited.copy()])
        return -1
    
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        que = deque([])
        num_of_keys = 0
        keys = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5}
        locks = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    que.append((i, j, 0, 0))
                elif grid[i][j] in keys:
                    num_of_keys += 1

        visited = set()
        while que:
            size = len(que)
            for _ in range(size):
                i, j, found, steps = que.popleft()
                curr = grid[i][j]
                if curr in locks and not (found >> locks[curr]) & 1 or curr == '#':
                    continue

                if curr in keys:
                    found |= 1 << keys[curr]
                    print(curr, bin(found))

                    if found == (1 << num_of_keys) - 1:
                        return steps

                for x, y in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                    if 0<=x<m and 0<=y<n and (x, y, found) not in visited:
                        visited.add((x, y, found))
                        que.append((x, y, found, steps+1))
        
        return -1
# ------------------------------------------------
s = Solution()
grid = ["@.a..","###.#","b.A.B"]  #8
# grid = ["@..aA","..B#.","....b"]   #6
grid = ["@...a",".###A","b.BCc"]  #10
res = s.shortestPathAllKeys(grid)
print(res)
#   "@   .   a   .   .",        # @   .   .   a   A      @   .   .   .   a
#   "#   #   #   .   #",        # .   .   B   #   .      .   #   #   #   A
#   "b   .   A   .   B"         # .   .   .   .   b      b   .   B   C   c



