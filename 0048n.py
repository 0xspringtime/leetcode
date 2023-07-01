def rotate(matrix):
    # Step 1: Transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
#time O(n^2)
#space O(1)
