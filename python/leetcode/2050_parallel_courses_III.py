import collections
from typing import List

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        parent_child = collections.defaultdict(list)
        indegree = {i:0 for i in range(1, n+1)}

        for rel in relations:
            parent_child[rel[0]].append(rel[1])
            indegree[rel[1]]+=1

        indegree =  sorted(indegree.items(), key=lambda x:x[1])
        for node, indeg in indegree.items():
            for child in parent_child[node]:
                
            pass
        

s = Solution()
n = 5
relations = [[1,5],[2,5],[3,5],[3,4],[4,5]]
time = [1,2,3,4,5]
rel = s.minimumTime(n, relations, time)
print(rel)