"""
    Given a sequence of matrices, find the most efficient way to multiply these matrices together. 
    The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications.
    This problem has an obtimal substructure and has overlapping sub-problems therefore we can use a dynamic programming method
"""
#Using the tabulation/ bottom up approach
def matrixCM(dimensions, numMatrices):
    n = numMatrices + 1
    #M matrix to hold the cost for each matrix multiplication
    M = [[0 for x in range(n)] for y in range(n)]
    S = [[0 for n in range(n)] for y in range(n)] 

    #we start calculating matrixes with difference 1 for ex. A1* A2, A2*A3 then difference of 2 ex. A1*A3, A2*A4  until the difference is n-1
    for d in range(1, n-1):
        #i will track the rows
        for i in range(1, n-d):
            #j will track the column 
            j = i + d
            minimum = float('inf')
            #k will track how we parenthesize the matrixes. For n matrices there are n-1 ways to arrange the parenthesis. we take the k value that will give us the minimum cost 
            for k in range(i, j):
                cost =  M[i][k] + M[k+1][j] + (dimensions[i-1]*dimensions[k]*dimensions[j])
                if cost < minimum:
                    minimum = cost
                    S[i][j] = k

            print(minimum)
            M[i][j] = minimum    

    return M[1][n-1]

#using recursion and memoization
i=1
n = 4
M = [[0 for x in range(n+1)] for y in range(n+1)]

def matrixCM2(dimensions, i, j):
    if i == j:
        return 0
    minimum = float('inf')

    #if we have already calculated the value we just return that value
    if M[i][j] > 0:
        return M[i][j]

     # place parenthesis at different places  
    # between first and last matrix,  
    # recursively calculate count of 
    # multiplications for each parenthesis 
    # placement and return the minimum count 
    for k in range(i, j):
        cost = matrixCM2(dimensions,i, k) + matrixCM2(dimensions, k+1, j) + dimensions[i-1]*dimensions[k]*dimensions[j]
        if cost < minimum:
            minimum = cost
    return minimum

#dimensions for each matrix
# matrix1 = [5,4]
# matrix2 =[4,6]
# matrix3 = [6,2]
# matrix = [2,7]
dimensions = [5,4,6,2,7]
print(matrixCM2(dimensions, i,n))