def isToeplitzMatrix(matrix):
    # Iterate over the matrix up to the second last row
    for i in range(len(matrix) - 1):
        # Iterate over each row up to the second last column
        for j in range(len(matrix[0]) - 1):
            # If an element is not equal to its lower-right neighbor, return False
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return False

    # If all elements were equal to their lower-right neighbors, return True
    return True
#time O(m*n)
#space O(1)
