from typing import List 


class Solution1:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        total_time = sum(time)

        cost_time = list(zip(cost, time))
        cost_time = sorted(cost_time, key=lambda x:x[0]/x[1])
        print(cost_time)

        min_ammount = 0
        while(cost_time):
            c, t = cost_time.pop(0)
            min_ammount += c
            while cost_time and t:
                cost_time.pop()
                t -= 1
        print('======', min_ammount)


class Solution2:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        def solve(cost, time, curr, wall_remaining):
            if curr >= len(cost):
                return sum(cost)
            if wall_remaining <= 0:
                return 0
            if dp[curr][wall_remaining] != -1:
                return dp[curr][wall_remaining]

            takes = cost[curr] + solve(cost, time, curr+1, wall_remaining-time[curr]-1)
            dont_takes = solve(cost, time, curr+1, wall_remaining)
            dp[curr][wall_remaining] = min(takes, dont_takes)
            return dp[curr][wall_remaining]

        # dp = [[-1 for _ in range(len(cost)+1)] for _ in range(len(cost)+1)]
        dp = [[-1 for _ in range(900)] for _ in range(900)]

        return solve(cost, time, 0, len(cost))

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        money = [sum(cost) for i in range(n+1)]
        money[0] = 0
        for i in range(n):
            for j in range(n, 0, -1):
                #          min( not_taken, taken )
                money[j] = min( money[j], money[max(j-time[i]-1, 0)]+cost[i] )
        return money[n]




s = Solution()
# cost, time = [1,2,3,2], [1,2,3,2] # output=3
cost, time = [2,3,4,2], [1,1,1,1] # output=4
# cost, time = [42,8,28,35,21,13,21,35], [2,1,1,1,2,1,1,2] # output = 63
ans = s.paintWalls(cost, time)
print(ans)