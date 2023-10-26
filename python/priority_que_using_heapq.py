'''Note: heapq is used to implement priority queues and deque is used to implement stack, queue'''
# # heapify
# # heappush
# # heappop
# # heapreplace

# import heapq
# H = [21,1,45,78,3,5]
# heapq.heapify(H)
# print(H)

# heapq.heappush(H,8)
# print(H)

# heapq.heappop(H)
# print(H)

# heapq.heapreplace(H,6)
# print(H)

import heapq
h = [(4, (1,3)), (5, (1,4)), (7, (2,5)), (2, (1,1)), (10, (5,5))]
heapq.heapify(h)
print(h)
m = heapq.heappop(h)
print(m)


