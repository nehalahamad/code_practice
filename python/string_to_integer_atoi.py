class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        res = 0
        if not s:
            return res
        positive = True
        if s[0] == '+':
            positive = True
        elif s[0] == '-':
            positive = False
        elif not s[0].isnumeric():
            return 0
        else:
            res = res * 10 + int(s[0])

        min1, max1 = -2**31, 2**31-1
        for i in range(1, len(s)):
            if s[i].isnumeric():
                res = res * 10 + int(s[i])
                print(res)
                if positive and res >= max1:
                    return max1
                elif not positive and -res <= min1:
                    return min1
            else:
                break
        if positive:
            return res
        else:
            return -res
        
        
s = Solution()
# res = s.myAtoi('-91283472332') #output = -2147483648
# res = s.myAtoi('    -42') #output = -42
res = s.myAtoi("21474836460") #output = 2147483647
print('result: ', res)
# print(2**31-1)