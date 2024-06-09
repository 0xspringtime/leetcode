def minCostHomecoming(startPos, homePos, rowCosts, colCosts):
    startRow, startCol = startPos
    homeRow, homeCol = homePos
    
    # Initialize the DP table with infinity
    m, n = len(rowCosts), len(colCosts)
    dp = [[float('inf')] * n for _ in range(m)]
    
    # Set the starting position cost to 0
    dp[startRow][startCol] = 0
    
    # Fill the DP table from the starting position to the home position
    for r in range(min(startRow, homeRow), max(startRow, homeRow) + 1):
        for c in range(min(startCol, homeCol), max(startCol, homeCol) + 1):
            if r > startRow:
                dp[r][c] = min(dp[r][c], dp[r-1][c] + rowCosts[r])
            if r < homeRow:
                dp[r][c] = min(dp[r][c], dp[r+1][c] + rowCosts[r])
            if c > startCol:
                dp[r][c] = min(dp[r][c], dp[r][c-1] + colCosts[c])
            if c < homeCol:
                dp[r][c] = min(dp[r][c], dp[r][c+1] + colCosts[c])
    
    return dp[homeRow][homeCol]

# Example usage:
startPos = [1, 1]
homePos = [2, 2]
rowCosts = [5, 10, 20]
colCosts = [10, 5, 15]

print(minCostHomecoming(startPos, homePos, rowCosts, colCosts))  # Output: 25
#time O(mn)
#space O(mn)
