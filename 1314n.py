#dynamic programming
def matrixBlockSum(mat: list, k: int) -> list:
    m, n = len(mat), len(mat[0])  # get the number of rows and columns

    # create a new matrix with additional rows and columns filled with 0
    range_sum = [[0] * (n + 1) for _ in range(m + 1)]

    # create the sum matrix
    for i in range(m):
        for j in range(n):
            range_sum[i + 1][j + 1] = mat[i][j] + range_sum[i][j + 1] + range_sum[i + 1][j] - range_sum[i][j]

    # create the answer matrix
    answer = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            r1, c1, r2, c2 = max(0, i - k), max(0, j - k), min(m, i + k + 1), min(n, j + k + 1)
            answer[i][j] = range_sum[r2][c2] - range_sum[r1][c2] - range_sum[r2][c1] + range_sum[r1][c1]

    return answer
#time O(m*n)
#space (m*n)
