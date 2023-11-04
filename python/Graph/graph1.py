# 0---1 \
# | / |  2
# 4---3 /
# Graph is represented by ADJACENCY MATRIX and ADJACENCY LIST

# Q1: write a fucntion to add an edge to a graph represented as an adjacency list
# Q2: write a function to remve and edge from a graph represented as a adjacency list
from collections import deque

class Graph():
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
    def __repr__(self):  #representation (repr)
        return "\n".join(["{}: {}".format(n, neighbors) for n, neighbors in enumerate(self.data)])
    # def __str__(self):
        # return self.__repr__()

def bft(graph, root):
    queue = deque()
    discovered = [False] * len(graph.data)

    queue.append(root)

    while queue:
        current = queue.popleft()
        if not discovered[current]:
            print(current)
            discovered[current] = True
            queue.extend(graph.data[current])

    return queue


# =====================================================
num_nodes = 5
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]

graph = Graph(num_nodes, edges)

q = bft(graph, 2)