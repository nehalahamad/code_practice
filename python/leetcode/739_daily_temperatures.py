from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        # for i, temp in enumerate(temperatures):
        #     while stack and temp > stack[-1][1]:
        #         st_ind, st_temp = stack.pop()
        #         res[st_ind] = i - st_ind
        #     stack.append([i, temp])
        # return res
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                print(stack[-1])
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res
    
s = Solution()
temperatures = [73,74,75,71,69,72,76,73]
res = s.dailyTemperatures(temperatures)
print(res)