from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def two_item_sum(arr):
            return [1] + [ arr[j]+arr[j+1] for j in range(len(arr)-1) ] + [1]

        res = [[1]]
        for i in range(numRows-1):
            res.append(two_item_sum(res[-1]))
        return res


s = Solution()
res = s.generate(5)
print(res)
        