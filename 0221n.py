#dynamic programming
def maximalSquare(matrix):
    # Dimensions of the matrix
    m, n = len(matrix), len(matrix[0])

    # Initialize the DP matrix
    dp = [[0] * n for _ in range(m)]

    # Variable to keep track of the maximum square side length
    max_side = 0

    # Iterate over the matrix
    for i in range(m):
        for j in range(n):
            # If the cell value is '1'
            if matrix[i][j] == '1':
                # If it's not on the first row or first column
                if i > 0 and j > 0:
                    # The side length of the square ending here is
                    # the minimum of the sides of the squares ending
                    # above, to the left, and above-left of this cell,
                    # plus one
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    # It's on the first row or first column, so the
                    # side length of the square ending here is 1
                    dp[i][j] = 1

                # Update max_side if necessary
                max_side = max(max_side, dp[i][j])

    # The area of the largest square is max_side squared
    return max_side ** 2
#time O(m * n)
#space O(m*n)
