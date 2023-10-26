from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, len(citations)
        while l<r:
            mid = (l+r)//2
            if citations[mid] >= n-mid:
                r = mid
            else:
                l = mid+1
        print(l, r, mid)
        return n-r
    
s = Solution()
citations = [0,1,3,5,6]
citations = [1,2,100]
# citations = [0]
res = s.hIndex(citations)
print(res)