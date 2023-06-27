#DFS
def maxAreaOfIsland(grid):
    # define the number of rows and columns
    m, n = len(grid), len(grid[0])

    # helper function to perform DFS on the grid
    def dfs(i, j):
        if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
            grid[i][j] = 0  # mark as visited
            return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)
        return 0

    # iterate through each cell in the grid
    return max(dfs(i, j) for i in range(m) for j in range(n))

