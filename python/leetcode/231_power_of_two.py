class Solution:
    def isPowerOfTwo_1(self, n: int) -> bool:
        def is_even(num):
            return bool(num & 1)

        sign = 1
        if n < 0:
            n = -n
            sign = -1
        count_of_ones = 0
        count = -1
        while n:
            if n & 1:
                count_of_ones += 1
            n >>= 1
            count += 1
        
        if sign == 1:
            return True if count_of_ones == 1 else False
        else:
            return True if count_of_ones == 1 and is_even(count) else False 

    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
            
        count_of_ones = 0
        while n:
            if n & 1:
                count_of_ones += 1
            n >>= 1
        return True if count_of_ones == 1 else False

s = Solution()
n = 4
res = s.isPowerOfTwo(n)
print(res)