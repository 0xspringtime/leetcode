#DFS
def pacificAtlantic(heights):
    # Step 1: Initialize 2D boolean arrays
    m, n = len(heights), len(heights[0])
    pacific = [[False]*n for _ in range(m)]
    atlantic = [[False]*n for _ in range(m)]

    # Helper function for DFS
    def dfs(x, y, reachable):
        # Mark current cell as reachable
        reachable[x][y] = True
        # Four directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or reachable[new_x][new_y] or heights[new_x][new_y] < heights[x][y]:
                continue
            dfs(new_x, new_y, reachable)

    # Step 2: Perform DFS for each ocean
    for i in range(m):
        dfs(i, 0, pacific)
        dfs(i, n - 1, atlantic)
    for i in range(n):
        dfs(0, i, pacific)
        dfs(m - 1, i, atlantic)

    # Step 3: Find cells that can flow to both oceans
    result = []
    for i in range(m):
        for j in range(n):
            if pacific[i][j] and atlantic[i][j]:
                result.append([i, j])
                
    return result

