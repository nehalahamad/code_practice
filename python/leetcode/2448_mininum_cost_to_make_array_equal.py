from typing import List
from itertools import accumulate

class Solution:
    def minCost_1(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        def get_median(num):
            for i in range(n-1, -1, -1):
                if num <= cost_cum_sum[i]:
                    return nums[i]

        nums, cost = zip(*sorted(zip(nums, cost), key=lambda x:x[1]))
        cost_cum_sum = list(accumulate(cost))

        if cost_cum_sum[-1] & 1:
            median = get_median((cost_cum_sum[-1]+1)//2)
            print('odd:  ', median)
        else:
            median = (get_median(cost_cum_sum[-1]//2) + get_median(cost_cum_sum[-1]//2+1))/2
            print('even: ', median)

        min_cost = 0
        for i in range(n):
            min_cost += abs(median-nums[i]) * cost[i]
        return min_cost
    
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def solve(mid):
            c = 0
            for i in range(len(nums)):
                c += abs(nums[i] - mid) * cost[i]
            return c

        l, r = min(nums), max(nums)

        while l <= r:
            mid = (l + r)//2
            if solve(mid) < solve(mid+1):
                idx = mid
                r = mid-1
            else:
                l = mid + 1
        print(idx)
        return solve(idx)
    
    def minCost_2(self, nums: List[int], cost: List[int]) -> int:
        arr = sorted(zip(nums, cost))
        mid = sum(cost) / 2
        count = 0
        for target, co in arr:
            count += co
            if count >= mid:
                return sum(abs(target - n) * c for n, c in arr)

s = Solution()
nums = [1,3,5,2] # 8
cost = [2,3,1,14]
nums = [735103,366367,132236,133334,808160,113001,49051,735598,686615,665317,999793,426087,587000,649989,509946,743518] # 1907611126748
cost = [724182,447415,723725,902336,600863,287644,13836,665183,448859,917248,397790,898215,790754,320604,468575,825614]
res = s.minCost(nums, cost)
print(res)
