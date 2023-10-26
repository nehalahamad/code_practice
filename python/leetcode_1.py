class Solution_1:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
            else:
                substr = ''
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()

                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(int(k) * substr)
        return ''.join(stack)


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ''
        cur_num = 0
        for c in s:
            if c.isnumeric():
                cur_num = cur_num * 10 + int(c)
            elif c == '[':
                stack.append(cur_str)
                stack.append(cur_num)
                cur_str = ''
                cur_num = 0
            elif c == ']':
                count = stack.pop()
                pre_str = stack.pop()
                cur_str = pre_str + cur_str * count
            else:
                cur_str += c
        return cur_str








sol = Solution_1()
# s = "3[a]2[bc]"  #--> aaabcbc
# s = "2[3[bc]]3[a]" #--> bcbcbcbcbcbcaaa
s = "3[a2[c]]"

r = sol.decodeString(s)
print(r)