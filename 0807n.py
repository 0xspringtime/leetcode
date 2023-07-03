def maxIncreaseKeepingSkyline(grid):
    # Determine the skyline from the north or south (maximum height of each column)
    north_south_skyline = [max(col) for col in zip(*grid)]
    
    # Determine the skyline from the east or west (maximum height of each row)
    east_west_skyline = [max(row) for row in grid]
    
    # The maximum possible height for a building without changing the skyline is determined by the minimum 
    # of the maximum heights from the north/south and east/west skylines
    total_increase = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            total_increase += min(north_south_skyline[j], east_west_skyline[i]) - grid[i][j]
    
    return total_increase
#time O(n^2)
#space O(n)
