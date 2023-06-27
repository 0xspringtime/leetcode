def generateMaxLocal(grid):
    # Initialize the maxLocal grid with the correct dimensions.
    maxLocal = [[0]*(len(grid) - 2) for _ in range(len(grid) - 2)]
    
    # Iterate over each cell in the original grid that can be the center of a 3x3 sub-grid.
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            # For each of these cells, find the maximum element in its corresponding 3x3 sub-grid.
            maxVal = max(
                grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1],
                grid[i][j - 1], grid[i][j], grid[i][j + 1],
                grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1]
            )
            # Add the maximum value to the maxLocal grid.
            maxLocal[i - 1][j - 1] = maxVal

    return maxLocal
#time O(n^2)
#space O(n^2)
