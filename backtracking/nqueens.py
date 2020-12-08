def solveNQueens(row, N,  board, queens=[]):#queens will be an array that stores the positions of valid queens
    if row == N:
        #base case where if we have placed all our queens then we print the board
        printBoard(board, N)
        print("")
        return
    for col in range(N):#iterate through the columns to find a valid position for the queen in this row
        #if it is a valid position we place the queen and move to the next row 
        if isValid(queens,row, col): 
            board[row][col] = 1
            queens.append([row,col]) #we add the queen to the array 
            solveNQueens(row+1,N, board, queens)
            #we backtrack and take away the queen so we can find other solutions
            queens.pop() 
            board[row][col] = 0 
        

def isValid(queens, row, col):
    for queen in queens: #iterate through our array with all the positions of the queens      
        #checks to see if there are any queens on the same column or row
        if queen[0] == row or queen[1] == col:
            return False
        #checks to see if there are any queens on the same diagonal
        deltaRow = abs(row-queen[0])
        deltaCol = abs(col-queen[1])
        if deltaRow == deltaCol:
            return False
    return True


def printBoard(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print("")

N = 5

#our chess board
board = [[0 for i in range(N)] for j in range(N)]

solveNQueens(0, N, board)