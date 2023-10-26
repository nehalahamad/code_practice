from typing import List 

class Solution:
    def removeDuplicates_1(self, nums: List[int]) -> int:
        i = 0
        count = 1
        for j in range(1, len(nums)):
            if nums[i] == nums[j]:
                if count < 2:
                    i += 1
                    nums[i] = nums[j]
                    count += 1
            else:
                i += 1
                nums[i] = nums[j]
                count = 1
        return i + 1
    
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        for j in range(2, len(nums)):
            if nums[i-2] != nums[j]:
                nums[i] = nums[j]
                i+=1
        return i

        
    
s = Solution()
nums = [0,0,1,1,1,1,2,3,3]
res = s.removeDuplicates(nums)
print(res)


# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if len(nums) <= 2:
#             return len(nums)

#         left = 2

#         for right in range(2, len(nums)):
#             if nums[right] != nums[left - 2]:
#                 nums[left] = nums[right]
#                 left += 1
        
#         return left