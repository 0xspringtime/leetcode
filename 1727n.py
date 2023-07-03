#dynamic programming
def largestSubmatrix(matrix):
    m, n = len(matrix), len(matrix[0])
    # pre-processing matrix
    for i in range(1, m):
        for j in range(n):
            if matrix[i][j] == 1:
                # count number of consecutive 1's in each column
                matrix[i][j] += matrix[i-1][j]

    ans = 0
    for i in range(m):
        # sort each row
        matrix[i].sort()
        for j in range(n):
            # compute the largest rectangle
            # height is matrix[i][j], width is n-j
            ans = max(ans, matrix[i][j] * (n - j))

    return ans
#time O(mnlogn)
#space O(1)
