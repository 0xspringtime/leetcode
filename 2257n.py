def unguarded_cells(m, n, guards, walls):
    # Initialize the grid with False
    grid = [[False] * n for _ in range(m)]

    # Mark the cells where guards are present
    for i, j in guards:
        grid[i][j] = True

    # Mark the cells where walls are present
    for i, j in walls:
        grid[i][j] = True

    # Directions for the guards to look (up, down, left, right)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Mark the cells that the guards can see
    for i, j in guards:
        for dx, dy in directions:
            x, y = i + dx, j + dy
            while 0 <= x < m and 0 <= y < n and not grid[x][y]:
                grid[x][y] = True
                x += dx
                y += dy

    # Count the unguarded cells
    unguarded_count = sum(row.count(False) for row in grid)

    return unguarded_count
#time O(mn)
#space O(mn)
