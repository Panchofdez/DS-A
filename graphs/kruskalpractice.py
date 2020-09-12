class Graph(object):
    def __init__(self, vertices):
        #num of vertices in graph 
        self.vertices = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u,v,w])
    
    def find_parent(self, parent, i):
        if parent[i] == i:
            return i 
        return self.find_parent(parent, parent[i])

    def union(self,parent, rank, u, v):
        u_parent = self.find_parent(parent,u)
        v_parent = self.find_parent(parent, v)

        if rank[u_parent] > rank[v_parent]:
            parent[v_parent] = u_parent
        elif rank[v_parent] > rank[u_parent]:
            parent[u_parent] = v_parent
        else:
            parent[u_parent] = v_parent
            rank[v_parent] += 1


    def KruskalAlgo(self):
        
      
        #store the resulting minimum spanning tree
        result = []
        #store the length of mst
        e = 0
        #counter as we iterate over the graph
        i = 0 
        print(self.graph)
        self.graph = sorted(self.graph, key=lambda x:x[2])
        print(self.graph)
        parent = []
        rank = []
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
        print(parent)
        print(rank)
        while e < self.vertices - 1:
            u, v, w = self.graph[i]
            i += 1
            x  = self.find_parent(parent, u)
            y = self.find_parent(parent, v)
            
            if x != y:
                e += 1
                result.append([u,v,w])
                print("before",parent)
                self.union(parent, rank, x, y)
                print("after", parent)
        print("Following are the edges in the constructed MST")
        for u,v,weight  in result: 
            #print str(u) + " -- " + str(v) + " == " + str(weight) 
            print ("%d -- %d == %d" % (u,v,weight)) 
g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 
  
g.KruskalAlgo() 