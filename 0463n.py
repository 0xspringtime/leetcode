def islandPerimeter(grid):
    # initialize perimeter to 0
    perimeter = 0
    
    # get the dimensions of the grid
    rows, cols = len(grid), len(grid[0])
    
    # iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # if the cell is land
            if grid[i][j] == 1:
                # add 4 to the perimeter for each side of the square
                perimeter += 4
                
                # if the cell is not on the top edge and the cell above it is land, subtract 2 from the perimeter
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                
                # if the cell is not on the left edge and the cell to the left of it is land, subtract 2 from the perimeter
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
                    
    return perimeter
#time O(m*n)
#space O(1)
