from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def max_heapify(i, heap_size):
            nonlocal stones
            l, r = 2*i+1, 2*i+2
            largest = i
            if l <= heap_size and stones[largest] < stones[l]:
                largest = l
            if r <= heap_size and stones[largest] < stones[r]:
                largest = r
            if largest != i:
                stones[i], stones[largest] = stones[largest], stones[i]
                max_heapify(largest, heap_size)

        def build_max_heap(heap_size):
            for i in range((heap_size-1)//2, -1, -1):
                max_heapify(i, heap_size)
        # ----------------------------------------------------------------
        heap_size = len(stones)-1
        build_max_heap(heap_size)

        while len(stones) > 1:
            y = stones[0]
            stones[0] = stones[-1]
            stones.pop()
            heap_size -= 1
            max_heapify(0, heap_size)

            x = stones[0]


            if x < y:
                stones[0] = y-x
                max_heapify(0, heap_size)
            else:
                stones[0] = stones[-1]
                stones.pop()
                heap_size -= 1
                max_heapify(0, heap_size)
        return stones[0] if stones else 0
# ---------------------------------------------------------
s = Solution()
stones = ([1, 3], [2,2], [2,7,4,1,8,1], [10,4,2,10])[1]
print(stones)
res = s.lastStoneWeight(stones)
print(res)
