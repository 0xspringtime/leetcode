#dynamic programming
def isInterleave(s1, s2, s3):
    len1, len2, len3 = len(s1), len(s2), len(s3)

    # If the length of s3 is not equal to the sum of the lengths of s1 and s2,
    # s3 cannot be an interleaving of s1 and s2
    if len1 + len2 != len3:
        return False

    # Create a 2D boolean array dp where dp[i][j] will be True if s3 up to length i + j
    # is a valid interleaving of s1 up to length i and s2 up to length j
    dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]
    dp[0][0] = True

    # Populate the dp array
    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i > 0:
                dp[i][j] = dp[i][j] or (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
            if j > 0:
                dp[i][j] = dp[i][j] or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

    return dp[len1][len2]
#time O(m*n)
#space O(m*n
