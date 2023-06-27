#dictionary
def isValidMatrix(matrix):
    n = len(matrix)
    valid_set = set(range(1, n + 1))

    # Check each row
    for row in matrix:
        if set(row) != valid_set:
            return False

    # Check each column
    for col in zip(*matrix):
        if set(col) != valid_set:
            return False

    return True
#time O(n^2)
#space O(n)
