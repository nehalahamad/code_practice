from typing import List

class Solution:
    def maxProfit_m(self, prices: List[int]) -> int:
        n = len(prices)-1
        m = [[-1, -1]for i in range(n+1)]

        def f(ind, buy):
            if ind > n:
                return 0
            if m[ind][buy] != -1:
                return m[ind][buy]
            
            if buy:
                profit = max( -prices[ind] + f(ind+1, 0),  f(ind+1, 1))
            else:
                profit = max( prices[ind] + f(ind+1, 1),  f(ind+1, 0))
            m[ind][buy] = profit
            return profit
        return f(0, 1)
    
    def maxProfit_dp(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0]for i in range(n)]

        for ind in range(n-2, -1, -1):
            for buy in range(0, 2):
                if buy:
                    profit = max( -prices[ind] + dp[ind+1][0],  dp[ind+1][1]    )
                else:
                    profit = max(  prices[ind] + dp[ind+1][1],  dp[ind+1][0]    )
                dp[ind][buy] = profit
        return dp[0][1]

    def maxProfit_two_txn_m(self, prices: List[int]) -> int:
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
    
    def maxProfit_two_txn_dp(self, prices: List[int]) -> int:
        n = len(prices)
        caps = 3
        buyes = 2
        dp = [[[0 for i in range(caps)] for j in range(2)] for k in range(n)]
        for ind in range(n-2, -1, -1):
            for buy in range(buyes):
                for cap in range(1, caps):
                    if buy == 1:
                        dp[ind][buy][cap] = max( -prices[ind] + dp[ind+1][0][cap],  dp[ind+1][1][cap])
                    else:
                        dp[ind][buy][cap] = max(  prices[ind] + dp[ind+1][1][cap-1],  dp[ind+1][0][cap])
        return dp[0][1][2]
    
    def maxProfit_two_txn_1(self, prices: List[int]) -> int:
        t1_min_price, t2_min_price = float('inf'), float('inf')
        t1_max_profit, t2_max_profit = 0, 0

        for price in prices:
            # Calculate the maximum profit if only one transaction is allowed
            if price < t1_min_price:
                t1_min_price = price

            profit1 = price - t1_min_price
            if profit1 > t1_max_profit:
                t1_max_profit = profit1

            # Use the profit of 1st transaction in 2nd transaction
            effective_price = price - t1_max_profit
            if effective_price < t2_min_price:
                t2_min_price = effective_price
            
            profit2 = price - t2_min_price
            if profit2 > t2_max_profit:
                t2_max_profit = profit2

        # t2_max_profit = The maximum profit after 2 transactions
        return t2_max_profit
    
# ------------------------------------------------------------
s = Solution()
prices = {0:[7,1,5,3,6,4], 1:[1,2,3,0,2], 2:[2,1,2,0,1], 3:[2,1,4,5,2,9,7], 4:[14,9,10,12,4,8,1,16], 5:[3,3,5,0,0,3,1,4]}
res = s.maxProfit_two_txn_dp(prices[5])
print(res)

a = int('6')