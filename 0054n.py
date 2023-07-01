def spiralOrder(matrix):
    if not matrix:
        return []

    # Define the boundaries of the matrix.
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    # Define the result to store the matrix elements.
    result = []
    
    while True:
        # Traverse from left to right.
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        # Update the top boundary.
        top += 1
        # Check if the top boundary crosses the bottom boundary.
        if top > bottom:
            break

        # Traverse from top to bottom.
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        # Update the right boundary.
        right -= 1
        # Check if the right boundary crosses the left boundary.
        if left > right:
            break

        # Traverse from right to left.
        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        # Update the bottom boundary.
        bottom -= 1
        # Check if the bottom boundary crosses the top boundary.
        if top > bottom:
            break

        # Traverse from bottom to top.
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        # Update the left boundary.
        left += 1
        # Check if the left boundary crosses the right boundary.
        if left > right:
            break

    return result
#time O(m*n)
#space O(m*n)
