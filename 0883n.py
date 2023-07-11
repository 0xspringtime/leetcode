def projectionArea(grid):
    # Initialize total area to zero
    total_area = 0

    # The xz (or yz) projection is the sum of the max height of cubes in each row (or column)
    total_area += sum(max(row) for row in grid) # xz projection
    total_area += sum(max(col) for col in zip(*grid)) # yz projection using zip to transpose grid

    # The xy projection is simply the count of cells that have cubes
    total_area += sum(val > 0 for row in grid for val in row)

    return total_area
#time O(n^2)
#space O(1)
