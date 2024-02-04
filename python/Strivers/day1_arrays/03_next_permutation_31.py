# https://www.youtube.com/watch?v=JDOXKqF60RQ
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = j = len(nums)-1
        
        # finding p such that nums[p] < nums[p+1] 
        while i>0 and nums[i-1] >= nums[i]:
            i -= 1
        p = i-1
        if i == 0:
            nums.reverse()
            return
        # finding j such that  nums[j] <= nums[p]
        while nums[j] <= nums[p]:
            j -= 1
        # swapping nums[j], nums[p]
        nums[p], nums[j] = nums[j], nums[p]
        # reversing
        nums[p+1:] = nums[len(nums)-1:p:-1]

        print(nums)
        return nums

sol = Solution()
# Input: 
# nums = [1,1,5] #Output:[1,5,1]
nums = [2, 1, 5, 4, 3, 0, 0]
res = sol.nextPermutation(nums)
print(res)