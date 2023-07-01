def numSpecial(mat):
    # Initialize the row and column count lists
    row_count = [0]*len(mat)
    col_count = [0]*len(mat[0])

    # Count the number of 1s in each row and column
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                row_count[i] += 1
                col_count[j] += 1

    # Check each 1 in the matrix to see if it's a 'special' position
    count = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                count += 1
    return count
#time O(m*n)
#space O(m+n)
