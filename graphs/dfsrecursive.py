#depth first search
#dfs uses a stack but instead of using an actual data structure we will use the call stack to implement the stack

from collections import defaultdict

class Graph(object):
    def __init__(self):
        #storing our graph as an adjacency list
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def DFS(self, start_node):
        visited = [False]*len(self.graph)
        return self.dfs_helper(start_node, visited)
    def dfs_helper(self, node, visited):
        if visited[node] == True:
            return 
        print(node, end=" ")
        visited[node] = True
        neighbours = self.graph[node]
        for next_node in neighbours:
            self.dfs_helper(next_node, visited)


g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print(g.graph)
g.DFS(0)