#DFS
def solve(board):
    if not board or not board[0]:
        return
    m, n = len(board), len(board[0])

    def dfs(i, j):
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != 'O':
            return
        board[i][j] = 'D'
        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)

    # Iterate the border and do dfs for every 'O'
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                dfs(i, j)

    # Flip 'O' to 'X' and 'D' back to 'O'
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'D':
                board[i][j] = 'O'
#time O(n)
#space O(m*n)
