#Breadth First Search
#uses a queue FIFO
#Searches through nodes in a graph level by level or layer by layer
#finds out if there is a path from node A to B and finds the shortest path
#only finds works in unweighted graphs 
#best algorithm for finding the single-source shortest path in unweighted graphs
#Time Complexity O(V+E)
#can handle large graphs

from collections import defaultdict


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)


    def BFS(self, start_node):
        #Breadth first traversal through a graph
        visited = [False]* len(self.graph)
        queue = []
        visited[start_node] = True
        queue.append(start_node)

        while queue:
            node = queue.pop(0)
            print(node, end=" ")
            for i in self.graph[node]:
                if visited[i] == False:
                    queue.append(i)
                 
                    visited[i] = True


g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

g.BFS(0)