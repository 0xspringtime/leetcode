def searchMatrix(matrix, target):
    # If the matrix is empty, return False
    if not matrix:
        return False

    # Initialize the pointers for the row and column
    row = 0
    col = len(matrix[0]) - 1

    # Loop until the pointers are within the boundaries of the matrix
    while row < len(matrix) and col >= 0:
        # If the target is found, return True
        if matrix[row][col] == target:
            return True
        # If the current cell value is greater than the target, move one cell to the left
        elif matrix[row][col] > target:
            col -= 1
        # If the current cell value is less than the target, move one cell down
        else:
            row += 1

    # If the target is not found, return False
    return False
#time O(m+n)
#space O(1)
