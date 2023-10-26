from typing import List

class Solution:
    def longestArithSeqLength_r(self, nums: List[int]) -> int:
        def solve(index, diff):
            if index < 0:
                return 0
            ans = 0
            for j in range(index-1, -1, -1):
                if nums[index] - nums[j] == diff:
                    ans = max(ans, 1+solve(j, diff))
            return ans

        n = len(nums)
        if n <= 2:
            return n
        
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                ans = max(ans, 2+solve(i, nums[j]-nums[i]))
        return ans
                
    def longestArithSeqLength_dp(self, nums: List[int]) -> int:
        from collections import defaultdict
        n = len(nums)
        if n <= 2:
            return n
        ans = 0
        dp = defaultdict(dict) # dp = {0:{},  1:{},  2:{}, ...}
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                cnt = 2
                # check if answer is already present
                if diff in dp[j]:
                    cnt = dp[j][diff] + 1
                dp[i][diff] = cnt
                ans = max(ans, dp[i][diff])
        print('-'*50)
        print(dp)
        return ans

# ---------------------------------------------------------------------------------
s = Solution()
nums = [[3,6,9,12], [9,4,7,2,10], [20,1,15,3,10,5,8]] # 4,3,4
for item in nums:
    res = s.longestArithSeqLength_dp(item)
    print(res)