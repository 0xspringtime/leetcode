def setZeroes(matrix):
    # Initialize variables to check if first row and column need to be set to 0's
    is_col = False
    R = len(matrix)
    C = len(matrix[0])

    # Iterating over the matrix
    for i in range(R):
        # Since first cell for both first row and first column is the same i.e. matrix[0][0]
        # We can use an additional variable for the first column
        # and matrix[0][0] for the first row
        if matrix[i][0] == 0:
            is_col = True

        # Iterate over the remaining columns
        for j in range(1, C):
            # If an element is zero, we set the first element of the corresponding row and column to 0
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    # Iterate over the matrix again and using the first row and first column, update the elements
    for i in range(1, R):
        for j in range(1, C):
            if not matrix[i][0] or not matrix[0][j]:
                matrix[i][j] = 0

    # Check if the first row needs to be set to zero
    if matrix[0][0] == 0:
        for j in range(C):
            matrix[0][j] = 0

    # Check if the first column needs to be set to zero
    if is_col:
        for i in range(R):
            matrix[i][0] = 0
#time O(m*n)
#space O(1)
