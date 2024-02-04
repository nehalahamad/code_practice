"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # memoization
        n = len(prices)-1
        m = [[[-1 for i in range(3)] for j in range(2)] for k in range(n+1)]

        def f(ind, buy, cap):
            if ind > n or cap == 0:
                return 0
            if m[ind][buy][cap] != -1:
                return m[ind][buy][cap]
            
            if buy:
                profit = max( -prices[ind] + f(ind+1, 0, cap),  f(ind+1, 1, cap))
            else:
                profit = max( prices[ind] + f(ind+1, 1, cap-1),  f(ind+1, 0, cap))
            m[ind][buy][cap] = profit
            return profit
        return f(0, 1, 2)
    
sol = Solution()
# Input: 
prices = [3,3,5,0,0,3,1,4]  #Output: 6
res = sol.maxProfit(prices)
print(res)