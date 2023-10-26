from typing import List
from icecream import ic
from collections import defaultdict


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        res = defaultdict(int)
        for a in arr:
            temp = 1
            for b in arr:
                if b>a: break
                temp += (res[b]*res[a/b])
            res[a] = temp
        return sum(res.values())%(10**9+7)


s = Solution()
arr = [2,4] #result=3
# arr = [2,4,5,10] #result=7
# arr = [18,3,6,2] # 12  after sort [2,3,6,18]
res = s.numFactoredBinaryTrees(arr)
ic(res)       


        