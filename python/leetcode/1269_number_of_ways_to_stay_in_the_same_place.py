from functools import lru_cache
class Solution1:
    def numWays(self, steps: int, arrLen: int) -> int:
        @lru_cache
        def dfs(steps, idx):
            if idx > steps:
                return 0
            if idx >= arrLen or idx < 0:
                return 0
            if steps == 0:
                if idx == 0:
                    return 1
                return 0
            return (dfs(steps-1, idx-1) + dfs(steps-1, idx) + dfs(steps-1, idx+1)) % (10**9+7)
        return dfs(steps, 0)

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # taking minimum of arrLen or half of the steps
        length = min(steps//2+1, arrLen)
        nums_arr_dp = [0 for _ in range(length)] #[1, 0, 0, 0, ... 0(nums)]
        nums_arr_dp[0] = 1
        for i in range(1, steps+1):
            newnums_arr_dp = nums_arr_dp[:]
            for j in range(min(i+1, length)):
                newnums_arr_dp[j] = ( nums_arr_dp[j] + (nums_arr_dp[j-1] if j-1 >=0 else 0) + (nums_arr_dp[j+1] if j+1 < length else 0) ) % (10**9+7)
            nums_arr_dp = newnums_arr_dp
        return nums_arr_dp[0]


sol = Solution()
# steps, arrLen = 499, 300
steps, arrLen = 3, 2 # output=4
res = sol.numWays(steps, arrLen)
print(res)