from collections import defaultdict

class Graph(object):
    def __init__(self):
        #we represent our graph as an adjacency list
        self.graph  = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self,start_node, end_node):
        #depth first search traversal to find if there is a path from start to end node
        #dfs implements a stack (LIFO)
        stack = []
        visited = [False]*len(self.graph)

        stack.append(start_node)
        visited[start_node] = True

        while stack:
            node = stack.pop(-1)

            print(node, end=" ")
            if node == end_node:
                return True
            for v in self.graph[node]:
                if visited[v] == False:
                    stack.append(v)
                    visited[v] = True
        return False

g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print(g.graph)
print(g.DFS(0, 3))