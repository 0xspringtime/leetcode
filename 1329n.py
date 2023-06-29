#stack
from collections import defaultdict

def diagonalSort(mat):
    # Use a defaultdict where each key is the difference between the row and column indexes.
    # This difference is constant for each diagonal.
    diagonals = defaultdict(list)

    # Iterate through the matrix, appending each value to the appropriate diagonal.
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            diagonals[i - j].append(mat[i][j])

    # Sort each list of diagonal values.
    for key in diagonals:
        diagonals[key].sort(reverse = True)

    # Write the sorted values back to the matrix.
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = diagonals[i - j].pop()

    return mat
#time O(mnlog(min(m, n)))
#space O(m*n)
