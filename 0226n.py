#greedy
from collections import defaultdict
def maxCoveredRows(matrix, numSelect):
    # get the dimensions of the matrix
    m, n = len(matrix), len(matrix[0])

    # Initialize a dictionary to store the rows covered by each column
    cols = defaultdict(set)

    # for each cell with value 1, add the row index to the corresponding column's set
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                cols[j].add(i)

    # sort the columns by the number of unique rows they cover, in descending order
    sorted_cols = sorted(cols.keys(), key=lambda x: len(cols[x]), reverse=True)

    # select the first numSelect columns from the sorted list
    selected_cols = sorted_cols[:numSelect]

    # create a set to store the rows covered by the selected columns
    covered_rows = set()
    for col in selected_cols:
        covered_rows.update(cols[col])

    # return the number of covered rows
    return len(covered_rows)
#time O(mn + nlog(n))
#space O(m*n)
