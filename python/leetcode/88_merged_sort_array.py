from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m+n-1
        
        # while m>0 and n>0:
        #     if nums1[m-1] >= nums2[n-1]:
        #         nums1[last] = nums1[m-1]
        #         m -= 1
        #     else:
        #         nums1[last] = nums2[n-1]
        #         n -= 1
        #     last -= 1
        
        # while n>0:
        #     nums1[last] = nums2[n-1]
        #     n -= 1
        #     last -= 1
        # ---------------------------------------------------

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
        print(nums1)
            
s = Solution()
nums1, m = [1,2,3,0,0,0], 3
nums2, n = [2,5,6], 3
s.merge(nums1, m, nums2, n)