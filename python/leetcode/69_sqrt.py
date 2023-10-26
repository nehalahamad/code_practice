class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        l, r = 1, x
        while l < r:
            mid = (l+r)//2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                r = mid
            else:
                l = mid + 1
        return l - 1

s = Solution()
for i in range(4, 80, 8):
    sq = s.mySqrt(i)
    print(i, '==', sq)