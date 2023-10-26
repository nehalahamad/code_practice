import heapq
from typing import List
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        left, right = 0, n-1
        heap_que = []
        res = 0

        while left <= right and left < candidates:
            heapq.heappush(heap_que, (costs[left], left))
            left += 1
            if left < right:
                heapq.heappush(heap_que, (costs[right], right))
                right -= 1

        for i in range(k):
            candidate = heapq.heappop(heap_que)
            res += candidate[0]
            if candidate[1] < left and left <= right:
                heapq.heappush(heap_que, (costs[left], left))
                left += 1
            elif candidate[1] > right and left <= right:
                heapq.heappush(heap_que, (costs[right], right))
                right -= 1
        return res

s = Solution()
costs = [18,64,12,21,21,78,36,58,88,58,99,26,92,91,53,10,24,25,20,92,73,63,51,65,87,6,17,32,14,42,46,65,43,9,75] #length=35
k = 13
candidates = 23
res = s.totalCost(costs, k, candidates)
print(res) #223
