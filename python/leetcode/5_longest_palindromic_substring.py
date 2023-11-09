class Solution:
    def longestPalindrome(self, s: str) -> str:
        m, n = len(s), len(s)
        x, y = s, s[::-1]
        table = [['' for i in range(n+1)] for j in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if y[i-1] == x[j-1]:
                    table[i][j] = x[j-1] + table[i-1][j-1]
                # else:
                    # table[i][j] = 0
        longest_substring = max([max(x, key=lambda x:len(x)) for x in table], key=lambda x:len(x))
        for r in table:
            print(r)
        return longest_substring

    
# -------------------------------
sol = Solution()
# s = "babad" #output "bab"
# s = 'cbb' # output 'bb'
# s = "eabcb" #output 'bcb
s = "aacabdkacaa" #output "aca"
res = sol.longestPalindrome(s)
print(res)