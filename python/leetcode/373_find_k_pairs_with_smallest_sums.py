from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        h = []
        for n1 in nums1:
            for n2 in nums2:
                if len(h) < k:
                    heapq.heappush(h, (-n1-n2, [n1, n2]))
                else:
                    top = heapq.heappop(h)
                    if top[0] > -n1-n2:
                        heapq.heappush(h, top)
                        break
                    else:
                        heapq.heappush(h, (-n1-n2, [n1, n2]))
        res = [item[1] for item in h]
        return res
    
s = Solution()
nums1, nums2, k = [1,7,11], [2,4,6], 3
res = s.kSmallestPairs(nums1, nums2, k)
print(res)