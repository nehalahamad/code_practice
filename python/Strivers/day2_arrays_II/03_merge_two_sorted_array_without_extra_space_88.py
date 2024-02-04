from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        i = 0
        j = m
        while i < j and j < m+n:
            if nums1[i] <= nums1[j]:
                i += 1
            else:
                temp = nums1[j]
                nums1[i+1:j+1] = nums1[i:j]
                nums1[i] = temp
                i += 1
                j += 1
        return nums1

sol = Solution()
# Input: 
nums1, nums2 = [1,2,3,0,0,0], [2,5,6]
m, n = 3, 3
# Output: [1,2,2,3,5,6]
res = sol.merge(nums1, m, nums2, n)
print(res)