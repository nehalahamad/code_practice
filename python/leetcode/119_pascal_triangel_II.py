from typing import List 
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def two_item_sum(arr):
            res = []
            for j in range(len(arr)-1):
                res.append(arr[j]+arr[j+1])
            return res

        res = [1, 1]
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return res
        else:
            for i in range(rowIndex-1):
                temp_res = [1] + two_item_sum(res) + [1]
                res = temp_res[:]
        return res
    

sol = Solution()
res = sol.getRow(3)
print(res)


        
        

        