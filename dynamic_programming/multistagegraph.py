
def multiStageGraph(n, graph, stages):
    costs = [0] * (n+1)
    d = [0] * (n+1)
    path = [0]* (stages+1)
    for i in range(n-1, 1, -1):
        minimum = float('inf')
        for k in range(i, n):

            if graph[i][k] != 0 and graph[i][k] + costs[k] < minimum:
                minimum =  graph[i][k] + costs[k]
                d[i] = k

        costs[k] = minimum

    path[1]= 1
    path[stages] = n
    for p in range(2, stages):
        path[p] = d[path[i-1]]

    return path   