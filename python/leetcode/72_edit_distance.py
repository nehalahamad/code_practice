class Solution:
    def minDistance_r(self, word1: str, word2: str) -> int:
        def f(i, j):
            if i<0: return j+1
            if j<0: return i+1
            return f(i-1, j-1) if word1[i] == word2[j] else 1 + min(f(i-1, j), f(i, j-1), f(i-1, j-1))

        i, j = len(word1)-1, len(word2)-1
        return f(i, j)

    def minDistance_dp(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # base condition
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])
        return dp[-1][-1]


s = Solution()
word1 = "horse"
word2 = "ros"
res = s.minDistance_dp(word1, word2)
print(res)
        