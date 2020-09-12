 #Bellman Ford algorithm 
#can find the shortest path from one node to any other node. Best to be used if Dijksta's algorithm doesn't work because there are negative weights
#time complexity of O(EV) or sometimes in worst case O(V^3)
#Can detect negative cycles
#dynamic programming method

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.edges = []
    
    def addEdge(self, u, v, w):
        self.edges.append([u,v,w])

           
    # utility function used to print the solution  
    def printArr(self, dist):  
        print("Vertex Distance from Source")  
        for i in range(self.V):  
            print("{0}\t\t{1}".format(i, dist[i]))  

    def BellmanFord(self, start):
        #1.set every entry to infinity
        #2.Set start node distance to 0
        #3.Relax every node V-1 times
        distances = [float('inf')]*self.V
        distances[start] = 0

        for i in range(self.V-1):
            for u,v,w in self.edges:
                if distances[v] > distances[u] + w:
                    distances[v] = distances[u] + w

        #if relaxation occurs after V-1 times then there is a negative cycle
        for u,v,w in self.edges:
            if distances[v] > distances[u] + w:
                print("Negative cycle detected")
                return 
        self.printArr(distances)  

                
g = Graph(5)  
g.addEdge(0, 1, -1)  
g.addEdge(0, 2, 4)  
g.addEdge(1, 2, 3)  
g.addEdge(1, 3, 2)  
g.addEdge(1, 4, 2)  
g.addEdge(3, 2, 5)  
g.addEdge(3, 1, 1)  
g.addEdge(4, 3, -3)  
  
# Print the solution  
g.BellmanFord(0)  