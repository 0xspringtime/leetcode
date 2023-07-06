#zig-zag traversal
def findDiagonalOrder(mat):
    # If the input matrix mat is empty, return an empty array
    if not mat or not mat[0]:
        return []

    # Get the dimensions of the input matrix
    m, n = len(mat), len(mat[0])

    # Initialize the output array with size m*n
    result = [0] * (m * n)

    # Define the indices
    row, col = 0, 0

    # Define the directions for "up" and "down"
    directions = [(1, -1), (-1, 1)]

    # The direction_index variable switches between the values 0 and 1.
    # This allows us to alternate between the "up" direction and the "down" direction.
    direction_index = 0

    for i in range(m * n):
        result[i] = mat[row][col]
        row += directions[direction_index][0]
        col += directions[direction_index][1]

        # If we go past the last column, then we need to switch direction and move down to the next row
        if col == n:
            col = n - 1
            row += 2
            direction_index = 1 - direction_index

        # If we go past the last row, then we need to switch direction and move to the next column
        elif row == m:
            row = m - 1
            col += 2
            direction_index = 1 - direction_index

        # If we go past the first column, then we need to switch direction
        elif col < 0:
            col = 0
            direction_index = 1 - direction_index

        # If we go past the first row, then we need to switch direction
        elif row < 0:
            row = 0
            direction_index = 1 - direction_index

    return result
#time O(m*n)
#space O(m*n)
