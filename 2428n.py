def maxHourglassSum(grid):
    # Initial max_sum to negative infinity
    max_sum = float("-inf")
    
    # The dimensions of the grid
    m, n = len(grid), len(grid[0])
    
    # Iterate through the grid
    for i in range(1, m - 1):  # Skip first and last row
        for j in range(1, n - 1):  # Skip first and last column
            # Calculate the hourglass sum
            hourglass_sum = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
            
            # Update max_sum if current hourglass_sum is greater
            max_sum = max(max_sum, hourglass_sum)
            
    return max_sum
#time O(m*n)
#space O(1)
