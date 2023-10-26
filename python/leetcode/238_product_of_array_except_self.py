from typing import List
import itertools

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        # output = [nums[0]]
        output = list(itertools.accumulate(nums, lambda x,y:x*y))
        product = 1
        for i in range(size-1, 0, -1):
            output[i] = output[i-1] * product
            product *= nums[i]
        output[i-1] = product
        return output


s = Solution()
nums = [1,2,3,4] #output = [24,12,8,6]
# nums = [-1,1,0,-3,3] #Output: [0,0,9,0,0]
res = s.productExceptSelf(nums)
print(res)