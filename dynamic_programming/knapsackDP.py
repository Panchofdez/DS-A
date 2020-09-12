"""
    • Dynamic programming is useful when you’re trying to optimize
    something given a constraint.
    • You can use dynamic programming when the problem can be
    broken into discrete subproblems.
    • Every dynamic-programming solution involves a grid.
    • he values in the cells are usually what you’re trying to optimize.
    • Each cell is a subproblem, so think about how you can divide your
    problem into subproblems.
    • here’s no single formula for calculating a dynamic-programming
    solution.
    """

def knapsack(size, weights, values):
    #using the tabulation method in dynamic programming (bottom-up approach)
    
    K=[[0 for n in range(size + 1)] for x in range(len(weights))]

    for i in range(len(weights)):
        for j in range(size + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif weights[i] <= j:
                K[i][j] = max(K[i-1][j], values[i] + K[i-1][j-weights[i]])
            else:
                K[i][j] = K[i-1][j]

    print(K)
    

    items = []

    x = len(weights)-1
    y = size
    print("Max total weight we can add to the Knapsack: ", K[x][y])
    #find the items that we can add to the knapsack
    while x >0  and y > 0:
        if K[x][y] == K[x-1][y]:
            x -= 1
        else:
            items.append(x)
            x-= 1
            y = y-weights[x+1]



    print("Items: ", items)       




# W = [0,3,1,2,2,1]
# V = [0,10,3,9,5,6]

# knapsack(6, W, V)


# val = [60, 100, 120] 
# wt = [10, 20, 30] 
# W = 50
# knapsack(W, wt, val)








val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50

#table to store our values so we don't recompute a value 
K = [[-1 for x in range(W + 1)] for y in range(len(val)+ 1)]

def knapsack_2(W, val, weights, n):
    #using the recursive + memoization approach

    #base case
    if n == 0 or W == 0:
        return 0
    
    #If it's not -1 we return the value that we already stored in the table so we avoid doing extra work
    if K[n][W] != -1:
        return K[n][W]

    #if the weight of the nth object is greater than the size of the knapsack we can't include it into the object
    if weights[n-1] > W:
        K[n][W] = knapsack_2(W, val, weights, n-1)
        return K[n][W]
    
    else:
        # return the maximum of two cases: 
        # (1) nth item included 
        # (2) not included 
        K[n][W] =  max(val[n-1] + knapsack_2(W-weights[n-1], val, weights, n-1), knapsack_2(W, val, weights, n-1))        
        return K[n][W]


print(knapsack_2(W, val, wt, len(val)))