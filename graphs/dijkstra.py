#Dijkstra algorithm
#best for finding the single-source shortest path in weighted graphs with no negative weights
#greedy method
"""While we have nodes to process
    Grab the node that is closest to the start
    Update the costs for its neighbors
    If any of the neighbors costs were updated, update the parents too
    Mark this node as processed"""


#setting up the graph as a hash table/dict
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"]={}
graph["a"]["fin"]=1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"]={}

print("graph", graph)

#dict to track the costs for each node in the graph
costs = {}
infinity = float("inf")
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

print("costs", costs)
#dict to track the parent of each node

parents={}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

print("parents", parents)
#Keep track of nodes processed
processed = []

#function to find the lowest cost for the remaining nodes that haven't been processed 
def lowest_cost_node(costs):
    lowest_cost_node = None
    lowest_cost = float("inf")
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = lowest_cost_node(costs)
while node is not None:
    print("node", node)
    cost = costs[node]
    neighbors = graph[node]
    print("cost", cost)
    print("neighbors", neighbors)
    for n in neighbors.keys():
        print("n", n)
        new_cost = cost + neighbors[n]
        print("new_cost", new_cost)
        print("costs[n]", costs[n])
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
        print(costs)
        print(parents)
    processed.append(node)
    node = lowest_cost_node(costs)

print("parents", parents)
