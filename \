#dynamic programming
def numDecodings(s):
    if not s:
        return 0

    # Create DP array
    dp = [0 for _ in range(len(s) + 1)]

    # base cases
    dp[0] = 1  # empty string can be decoded in one way
    dp[1] = 0 if s[0] == "0" else 1  # for string of length 1

    for i in range(2, len(s) + 1):
        # if current character is not '0', add number of ways to decode till previous index
        if s[i-1] != '0':
            dp[i] += dp[i-1]

        # if last two digits form a number less than or equal to 26, add number of ways to decode till previous to previous index
        two_digit = int(s[i-2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i-2]

    return dp[-1]  # return the number of ways to decode the full string
#time O(n)
#space O(n)
