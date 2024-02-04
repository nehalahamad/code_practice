from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_arr_sum = nums[0]
        maximum = nums[0]
        for item in nums[1:]:
            max_sub_arr_sum = max(max_sub_arr_sum + item, item)
            maximum = max(maximum, max_sub_arr_sum) 

        return maximum
    
sol = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] #Output = 6
res = sol.maxSubArray(nums)
print(res)  