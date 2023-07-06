def is_x_matrix(grid):
    # Get the size of the matrix
    n = len(grid)

    # Iterate over every cell in the matrix
    for i in range(n):
        for j in range(n):
            # If the cell is part of a diagonal
            if i == j or i == n - j - 1:
                # If the cell's value is zero, return False
                if grid[i][j] == 0:
                    return False
            # If the cell is not part of a diagonal
            else:
                # If the cell's value is non-zero, return False
                if grid[i][j] != 0:
                    return False

    # If we finish iterating without returning False, return True
    return True
#time O(n^2)
#space O(1)
