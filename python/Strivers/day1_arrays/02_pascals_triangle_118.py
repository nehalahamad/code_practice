from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def two_item_sum(arr):
            return [1] + [ arr[j]+arr[j+1] for j in range(len(arr)-1) ] + [1]

        res = [[1]]
        for i in range(numRows-1):
            res.append(two_item_sum(res[-1]))
        return res
    
sol = Solution()
# Input: 
numRows = 5 #Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
res = sol.generate(numRows)
print(res)