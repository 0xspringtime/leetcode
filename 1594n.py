#dynamic programming
def maxProductPath(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # The dimensions of the grid
    m, n = len(grid), len(grid[0])

    # Initialize dp_max and dp_min with the same dimensions as the grid
    dp_max = [[0]*n for _ in range(m)]
    dp_min = [[0]*n for _ in range(m)]

    # The starting point would be the first element of the grid
    dp_max[0][0] = dp_min[0][0] = grid[0][0]

    # Precompute the first row and first column because they only have one option
    for i in range(1, m):
        dp_max[i][0] = dp_min[i][0] = dp_max[i-1][0] * grid[i][0]
    for j in range(1, n):
        dp_max[0][j] = dp_min[0][j] = dp_max[0][j-1] * grid[0][j]

    # Start from the cell (1, 1) and iterate the dp array
    for i in range(1, m):
        for j in range(1, n):
            # When grid[i][j] is negative, max_val should be the product of the minimum value before and itself.
            # Similarly, min_val should be the product of the maximum value before and itself.
            if grid[i][j] < 0:
                dp_max[i][j] = min(dp_min[i-1][j], dp_min[i][j-1]) * grid[i][j]
                dp_min[i][j] = max(dp_max[i-1][j], dp_max[i][j-1]) * grid[i][j]
            else:
                dp_max[i][j] = max(dp_max[i-1][j], dp_max[i][j-1]) * grid[i][j]
                dp_min[i][j] = min(dp_min[i-1][j], dp_min[i][j-1]) * grid[i][j]

    # Return the result, modulo 10^9+7
    return -1 if dp_max[-1][-1] < 0 else dp_max[-1][-1] % (10**9+7)
#time O(m*n)
#space O(m*n)
