from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        profit = 0
        effective_buy_price = prices[0]
        for i in range(1, n):
            profit = max(profit, prices[i]-effective_buy_price-fee)
            effective_buy_price = min(effective_buy_price, prices[i]-profit)
        return profit

# --------------------------------
prices = [1,3,2,8,4,9]
fee = 2
s = Solution()
res = s.maxProfit(prices, fee)
print(res) 