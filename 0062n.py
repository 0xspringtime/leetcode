#dynamic programming
def uniquePaths(m, n):
    # Initialize a 2D DP matrix with size m x n
    dp = [[0 for _ in range(n)] for _ in range(m)]

    # The robot can reach any cell in the first row or first column with only 1 path
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    # For each cell in the rest of the matrix, calculate the number of unique paths
    # by adding the number of unique paths to the cell above it and the cell to its left
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    # Return the number of unique paths to the bottom-right corner
    return dp[-1][-1]
#time O(m*n)
#space O(m*n)
