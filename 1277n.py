#dynamic programming
def countSquares(matrix):
    if not matrix: return 0

    # Initialize the DP table with the same size as the input matrix
    dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]

    # Initialize the count of squares
    squares = 0

    # Iterate over the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                # If the current cell is in the first row or first column, the maximum size of square it can be part of is 1
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    # The current cell can be part of a square with side length 1 plus the minimum side length of the squares that its top, left, and top-left cells can be part of
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

                # Add the side length of the square that the current cell can be part of to the total count of squares
                squares += dp[i][j]

    # Return the total count of squares
    return squares
#time O(m*n)
#space O(m*n)
