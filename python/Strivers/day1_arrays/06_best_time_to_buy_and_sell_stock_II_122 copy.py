from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy_price = prices[0]
        profit = 0
        for i in range(1, n):
            if prices[i]-buy_price > profit:
                sell_price = prices[i]
                profit = sell_price - buy_price
            else:
                buy_price = min(buy_price, prices[i])
        return profit
    
sol = Solution()
# Input: 
prices = [7,1,5,3,6,4]  #Output: 7
res = sol.maxProfit(prices)
print(res)