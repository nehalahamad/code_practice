class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        grid = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    grid[i][j] = grid[i-1][j-1] + 1
                else:
                    grid[i][j] = max(grid[i][j-1], grid[i-1][j])
        # for t in grid:
        #     print(t)
        return grid[m][n]

text1 = "bsbininm"
text2 = "jmjkbkjkv"
s = Solution()
res = s.longestCommonSubsequence(text1, text2)
print(res)