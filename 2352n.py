def countEqualRowsColumns(grid):
    # Get the rows
    rows = grid

    # Get the columns using list comprehension
    cols = [[row[i] for row in grid] for i in range(len(grid))]

    # Count the number of equal rows and columns
    count = sum(row in cols for row in rows)

    return count
#time O(n^3)
#space O(n^2)
