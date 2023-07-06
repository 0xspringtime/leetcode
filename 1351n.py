def countNegatives(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # Initialize the row and column indices and the negative number count
    row, col, count = 0, len(grid[0]) - 1, 0

    # Continue until we have processed all rows and columns
    while row < len(grid) and col >= 0:
        # If the current number is negative, count all the numbers to the left and move down
        if grid[row][col] < 0:
            count += col + 1
            row += 1
        # If the current number is non-negative, move left
        else:
            col -= 1

    return count
#time O(m+n)
#space O(1)
