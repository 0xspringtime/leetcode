def searchMatrix(matrix, target):
    # Check if the matrix is empty
    if not matrix or not matrix[0]:
        return False

    # Get the dimensions of the matrix
    m, n = len(matrix), len(matrix[0])

    # Start from the top-right corner of the matrix
    row, col = 0, n - 1

    # Perform binary search
    while row < m and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1

    # Target not found
    return False
#time O(m+n)
#space O(1)
