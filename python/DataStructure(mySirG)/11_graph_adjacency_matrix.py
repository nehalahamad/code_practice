# https://youtu.be/kJnOSCdmJWw?list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs
'''
1 - write a class Graph to implement adjacency matrix representation of a simple and undirected graph.
2 - In class Graph, define __init__ method to initialise vertex_count and adj_matrix (list of list)
3 - In class Graph, define add_edge() method to add an edge in the graph with given weight.
4 - In class Graph, define remove_edge() method to remove and edge from the graph.
5 - In class Graph, define has_edge() method check whether two given vetices are connected by an edge or not
6 - In class Graph, define print_adj_matrix() mehtod to print adjacency matrix.
'''
class Graph:
    def __init__(self, vno) -> None:
        self.vertext_count = vno
        self.adj_matrix = [[0]*vno for _ in range(vno)]
    
    # -----------------------------------------------
    def add_edge(self, u, v, weight=1):
        if 0<=u<self.vertext_count and 0<=v<self.vertext_count:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
        else:
            print('Invalid Vertext')

    # -----------------------------------------------
    def remove_edge(self, u, v):
        if 0<=u<self.vertext_count and 0<=v<self.vertext_count:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
        else:
            print('Invalid Vertext')

    # -----------------------------------------------
    def has_edge(self, u, v):
        if 0<=u<self.vertext_count and 0<=v<self.vertext_count:
            return self.adj_matrix[u][v] != 0
        else:
            print('Invalid Vertext')

    # -----------------------------------------------
    def print_adj_matrix(self):
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))

# =====================================================
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_adj_matrix()

