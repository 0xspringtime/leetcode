def shiftGrid(grid, k):
    # Flatten the grid into a 1D list
    m, n = len(grid), len(grid[0])
    flat = [grid[i // n][i % n] for i in range(m * n)]

    # Shift the 1D list k times
    k = k % len(flat)  # Only need to shift the remainder of k / len(flat)
    flat = flat[-k:] + flat[:-k]

    # Convert the 1D list back to a 2D grid
    return [[flat[i * n + j] for j in range(n)] for i in range(m)]
#time O(m*n)
#space O(m*n)
