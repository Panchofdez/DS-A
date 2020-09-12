#use dfs to find connected components in a graph
from collections import defaultdict

class Graph():
    def __init__(self):
        #storing our graph as an adjacency list
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def connected_components(self):
        visited = [False] *len(self.graph)
        #tracks the number of connected_components
        count = 0 
        #keeps track of which component the node belongs to
        components = []

        for node in self.graph:
            if visited[node] == False:
                count+=1
                dfs(node, components, count)
        return (count, components)

    def dfs(self, node, components, count):
        visited[node] = True
        components[node] = count
        for next_node in self.graph[node]:
            if visited[next_node] == False:
                dfs(next_node,components,count)