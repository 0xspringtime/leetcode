def matrixReshape(mat, r, c):
    # Calculate the total number of elements in the original matrix
    m, n = len(mat), len(mat[0])
    if m * n != r * c:
        return mat  # reshaping is not possible
    
    # Create an empty reshaped matrix
    reshaped_mat = [[0]*c for _ in range(r)]
    for i in range(m*n):
        # calculate the corresponding row and column indices 
        # in the reshaped matrix for the current element
        reshaped_mat[i//c][i%c] = mat[i//n][i%n]
        
    return reshaped_mat
#time O(m*n)
#space O(m*n)
