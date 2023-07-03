#dynamic programming
def largest1BorderedSquare(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0]*(n+1) for _ in range(m+1)]
    dp2 = [[0]*(n+1) for _ in range(m+1)]
    ans = 0

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if grid[i][j] == 1:
                # Calculate the side length of the largest square sub-grid ending at this cell
                dp[i][j] = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]) + 1
                # If the side length of the square is 1, we know that the square only contains the cell itself
                dp2[i][j] = 1
                # If the side length of the square is greater than 1
                if dp[i][j] > 1:
                    # Check if the rightmost column and bottom row of the square are all 1s
                    l = dp[i][j]
                    if dp2[i][j+l-1] >= l and dp2[i+l-1][j] >= l:
                        dp2[i][j] = l
                    else:
                        dp2[i][j] = max(min(dp2[i+1][j], dp2[i][j+1])+1, dp2[i][j])
                ans = max(ans, dp2[i][j])
    return ans*ans
#time O(m*n)
#space O(m*n)
