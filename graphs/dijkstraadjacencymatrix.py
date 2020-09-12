#Dijkstra algorithm
#finds the shortest path to all the other nodes in the graph
#a greedy method/optimization problem 
"""While we have nodes to process
    Grab the node that is closest to the start or has the minimum distance value
    Update the costs for its neighbors
    If any of the neighbors costs were updated, update the parents too
    Mark this node as visited"""


class Graph():

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for col in range(vertices)] for row in range(vertices)]

    def printSolution(self, dist): 
        print("Vertex \tDistance from Source")
        for node in range(self.vertices): 
            print(node, "\t", dist[node])
    def find_lowest_cost_node(self, distances, visited):
        lowest_cost = float("inf")
        lowest_cost_node = 0

        for node in range(self.vertices):
            if visited[node] == False and distances[node] < lowest_cost:
                lowest_cost = distances[node]
                lowest_cost_node = node
        return lowest_cost_node

    def dijkstra(self, start):
        visited = [False] * self.vertices
        distances = [float("inf")] * self.vertices

        distances[start] = 0

        for node in range(self.vertices):
            u = self.find_lowest_cost_node(distances, visited)
            visited[u] = True
            for v in range(self.vertices):
                if self.graph[u][v] > 0 and visited[v] == False and distances[v] > self.graph[u][v] + distances[u]:
                    distances[v] =   self.graph[u][v] + distances[u]
        self.printSolution(distances)


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]; 
  
g.dijkstra(0); 