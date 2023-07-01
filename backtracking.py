#solutions to a problem that incrementally builds candidates for the solutions, and abandons a candidate as soon as it determines that the candidate cannot possibly be extended to a valid solution

#"try -> check -> undo if failed" is common in many backtracking problems

def solveNQueens(N):
    # Initialize the board with all 0s
    board = [[0 for j in range(N)] for i in range(N)]

    # Helper function to check if a queen can be placed at board[row][col]
    def canPlace(board, row, col):
        # Check this row on left side
        for i in range(col):
            if board[row][i] == 1:
                return False
        # Check upper diagonal on left side
        for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
            if board[i][j] == 1:
                return False
        # Check lower diagonal on left side
        for i,j in zip(range(row,N,1), range(col,-1,-1)):
            if board[i][j] == 1:
                return False
        return True

    # Recursive helper function to solve the problem
    def placeQueens(board, col):
        # Base case: If all queens are placed, return true
        if col >= N:
            return True
        # Consider this column and try placing queen in all rows one by one
        for i in range(N):
            if canPlace(board, i, col):
                # Place this queen at board[i][col]
                board[i][col] = 1
                # Recur to place rest of the queens
                if placeQueens(board, col + 1):
                    return True
                # If placing queen in board[i][col] doesn't lead to a solution, then remove queen from board[i][col]
                board[i][col] = 0
        # If queen can not be placed in any row in this column col then return false
        return False

    if not placeQueens(board, 0):
        print("Solution does not exist")
        return False
    else:
        print(board)
        return True

# Call the function
solveNQueens(4)


