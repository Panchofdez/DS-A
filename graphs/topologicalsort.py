#A topological ordering of the nodes in a directed graph where for each directed edge from node A to node B, node  A appears before node B 
#topological orderings are not unique
#topological sort is O(V+E)
#the only type of graph which has a valid topological ordering are Directed Acyclic Graphs (DAG)

from collections import defaultdict


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        """Arbritrarily pick an unvisited node
            Beginning with the selected node, do a Depth-first search exploring only unvisited nodes
            On the recursive callback of DFS add the current node to the topological ordering in reverse order 
        """" 
        N = len(self.graph)
        visited = [False]*N
        ordering = [0]* N #result of the topological sort
        i = N-1#tracks the index to insert into the ordering array

        for node in self.graph:
            if visited[node] == False:
                i = dfs(node, visited, ordering, i)

        return ordering 

    def dfs(self, node, visited, ordering, i):
        visited[node] = True
        neighbours = self.graph[node]
        for neighbour in neighbours:
            if visited[neighbour] == False: 
                i = dfs(neighbour, visited, ordering, i)
        
        ordering[i] = neighbour
        return i - 1
