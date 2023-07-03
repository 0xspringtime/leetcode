def allCellsDistOrder(rows, cols, rCenter, cCenter):
    # Initialize an empty list to store all cells
    cells = []
    
    # Iterate through all cells in the matrix
    for i in range(rows):
        for j in range(cols):
            # Append the cell to the list along with its distance from the center cell
            cells.append((i, j, abs(i - rCenter) + abs(j - cCenter)))
    
    # Sort the cells by their distance from the center cell
    cells.sort(key=lambda x: x[2])
    
    # Return the cells without their distances
    return [(i, j) for i, j, _ in cells]
#time O(rows * cols * log(rows * cols))
#space O(rows * cols)
