from typing import List
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def solve(k, ch):
            sp, ep, ans = 0, 0, 0
            while ep < len(answerKey):
                if answerKey[ep] != ch:
                    k -= 1
                while k < 0:
                    if answerKey[sp] == ch:
                        sp += 1
                    else:
                        sp += 1
                        k += 1
                ans = max(ans, ep-sp+1)
                ep += 1
            return ans
        return max(solve(k, 'T'), solve(k, 'F'))
    
    def maxConsecutiveAnswers_1(self, answerKey: str, target: int) -> int:
        mx = 0
        for ch in "TF":
            j = 0
            k = target
            for i in answerKey:
                if i == ch:
                    k -= 1
                if k < 0:
                    if answerKey[j] == ch:
                        k += 1
                    j += 1
            mx = max(mx, len(answerKey)-j)
        return mx
    
s = Solution()
answerKey = "TTFTTFTT"
k = 1
res = s.maxConsecutiveAnswers_1(answerKey, k)
print(res)