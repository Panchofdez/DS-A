#Floyd Warshall algorithm
#for finding a solution to All-Pairs Shortest Path problem
#dynamic programming method
#Time Complexity of O(V^3)

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for x in range(vertices)] for y in range(vertices)]

    def FloydWarshall(self):

        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    self.graph[i][j] = min(self.graph[i][j], self.graph[i][k] + self.graph[k][j])

        self.printSolution()

    def printSolution(self):
        for i in range(self.V): 
            for j in range(self.V): 
                if(self.graph[i][j] == INF): 
                    print("INF", end= "\t")
                else: 
                    print(self.graph[i][j], end="\t")
                if j == self.V-1: 
                    print("") 


# Let us create the following weighted graph 
""" 
            10 
       (0)------->(3) 
        |         /|\ 
      5 |          | 
        |          | 1 
       \|/         | 
       (1)------->(2) 
            3           """
g = Graph(4)
INF = float("inf")
g.graph = [[0,5,INF,10], 
             [INF,0,3,INF], 
             [INF, INF, 0,   1], 
             [INF, INF, INF, 0] 
        ] 
# Print the solution 
g.FloydWarshall(); 