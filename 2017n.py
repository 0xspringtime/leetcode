#dynamic programming
def gridGame(grid):
    n = len(grid[0])

    # Prepare the dp tables
    dp1 = [[0]*n for _ in range(2)]
    dp2 = [[0]*n for _ in range(2)]

    # Populate dp1 table
    for r in range(2):
        for c in range(n):
            dp1[r][c] = grid[r][c] + max(dp1[r-1][c] if r > 0 else 0, dp1[r][c-1] if c > 0 else 0)

    # Populate dp2 table
    for r in range(1, -1, -1):
        for c in range(n-1, -1, -1):
            dp2[r][c] = grid[r][c] + min(dp2[r+1][c] if r < 1 else 0, dp2[r][c+1] if c < n-1 else 0)

    # Return the number of points collected by the second robot
    return min(max(dp1[0][c-1], dp2[0][c+1]) for c in range(1, n-1))
#time O(n)
#space O(n)
