# https://www.youtube.com/watch?v=tj67qYGeYHY&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=37&pp=iAQB

'''
1 - write a class Graph to implement adjacency matrix representation of a simple and undirected graph.
2 - In class Graph, define __init__ method to initialise vertex_count and dict adj_list where key is vertex and value is a list of adjacent vertices
3 - In class Graph, define add_edge() method to add an edge in the graph with given weight.
4 - In class Graph, define remove_edge() method to remove and edge from the graph.
5 - In class Graph, define has_edge() method check whether two given vetices are connected by an edge or not
6 - In class Graph, define print_adj_matrix() mehtod to print adjacency list of graph.
'''
class Graph:
    def __init__(self, vno) -> None:
        self.vertext_count = vno
        self.adj_list = {v:[] for v in range(vno)}
    
    # -----------------------------------------------
    def add_edge(self, u, v, weight=1):
        if 0<=u<self.vertext_count and 0<=v<self.vertext_count:
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))
        else:
            print('Invalid Vertext')

    # -----------------------------------------------
    def remove_edge(self, u, v):
        if 0<=u<self.vertext_count and 0<=v<self.vertext_count:
            self.adj_matrix[u] = [(vert, w) for vert, w in self.adj_list if vert!=v]
            self.adj_matrix[v] = [(vert, w) for vert, w in self.adj_list if vert!=u]
        else:
            print('Invalid Vertext')

    # -----------------------------------------------
    def has_edge(self, u, v):
        if 0<=u<self.vertext_count and 0<=v<self.vertext_count:
            return any(vert==v for vert, w in self.adj_list[u])
        else:
            print('Invalid Vertext')

    # -----------------------------------------------
    def print_adj_matrix(self):
        for vert, n in self.adj_list.items():
            print('V', vert, ': ', n)

# =====================================================
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_adj_matrix()

