#dynamic programming
def isMatch(s: str, p: str) -> bool:
    # Initialize a 2D table dp where dp[i][j] will be True if the first i characters
    # in string s can be matched by the first j characters in the string p.
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

    # The empty pattern can match the empty string.
    dp[-1][-1] = True

    # Fill up the table from bottom to top, from right to left.
    for i in range(len(s), -1, -1):
        for j in range(len(p) - 1, -1, -1):
            # Check if the current characters actually match.
            match = i < len(s) and p[j] in {s[i], '.'}

            # If the next character in the pattern is a '*', then we have two possibilities:
            # - We use the '*' to match zero of the current character in the pattern, so
            #   we ignore this character in the pattern and move on to the next one;
            # - We use the '*' to match one of the current character in the string, so
            #   we move on to the next character in the string.
            if j + 1 < len(p) and p[j + 1] == '*':
                dp[i][j] = dp[i][j + 2] or match and dp[i + 1][j]
            # Otherwise, the current characters in the string and in the pattern must match,
            # and the remaining strings must also match.
            else:
                dp[i][j] = match and dp[i + 1][j + 1]

    return dp[0][0]
#time O(SP)
#space O(SP)
