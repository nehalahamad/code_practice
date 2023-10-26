from typing import List 

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        i = -1
        for j in range(len(nums)):
            if nums[j] != 0:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                
        return nums
s = Solution()
nums = [312,312,436,892,0,0,528,0,686,516,0,0,0,0,0,445,445,445,445,445,445,984,984,984,0,0,0,0,168,0,0,647,41,203,203,241,241,0,628,628,0,875,875,0,0,0,803,803,54,54,852,0,0,0,958,195,590,300,126,0,0,523,523]
res = s.applyOperations(nums)
print(res)