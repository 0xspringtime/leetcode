def restoreMatrix(rowSum, colSum):
    # number of rows and columns
    num_rows, num_cols = len(rowSum), len(colSum)
    
    # initialize matrix of zeroes
    matrix = [[0]*num_cols for _ in range(num_rows)]
    
    # iterate through each cell in the matrix
    for i in range(num_rows):
        for j in range(num_cols):
            # take minimum of what is left in the current rowSum and colSum
            # this is the max amount we can put in this cell without violating the constraints
            matrix[i][j] = min(rowSum[i], colSum[j])
            
            # subtract the filled amount from rowSum and colSum
            rowSum[i] -= matrix[i][j]
            colSum[j] -= matrix[i][j]
    
    return matrix
#time O(m*n)
#space O(m*n)
