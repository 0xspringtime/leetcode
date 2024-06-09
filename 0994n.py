from collections import deque

def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_oranges = 0

    # Initialize the queue with all rotten oranges and count fresh oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh_oranges += 1

    # Directions for 4-directional movement (up, down, left, right)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    minutes_elapsed = 0

    # BFS to rot the fresh oranges
    while queue and fresh_oranges > 0:
        minutes_elapsed += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    queue.append((nx, ny))
                    fresh_oranges -= 1

    # If there are still fresh oranges left, return -1
    return minutes_elapsed if fresh_oranges == 0 else -1

# Example usage:
grid1 = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
print(orangesRotting(grid1))  # Output: 4

grid2 = [
    [2, 1, 1],
    [0, 1, 1],
    [1, 0, 1]
]
print(orangesRotting(grid2))  # Output: -1

grid3 = [
    [0, 2]
]
print(orangesRotting(grid3))  # Output: 0

