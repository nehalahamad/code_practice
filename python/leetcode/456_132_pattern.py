from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_arr = []
        min_ele = nums[0]
        for i in range(len(nums)):
            if nums[i] < min_ele:
                min_arr.append(nums[i])
                min_ele = nums[i]
            else:
                min_arr.append(min_ele)
        stack = []
        for j in range(len(nums)-1, -1, -1):
            while stack and nums[j]<stack[-1]:
                stack.pop()
            

            pass
        

nums = [3,1,4,2]
sol = Solution()
sol.find132pattern(nums)

        


        