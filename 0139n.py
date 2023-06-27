#dynamic programming
def wordBreak(s, wordDict):
    # Create a set for faster lookup
    word_set = set(wordDict)

    # Create dp table, initialized to False
    dp = [False] * (len(s) + 1)

    # Base case: an empty string can always be segmented
    dp[0] = True

    # Fill dp table
    for i in range(1, len(s) + 1):
        for j in range(i):
            # If the substring s[j:i] is in word_set and dp[j] is True
            # Then we can form a valid word ending at i
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  # no need to check other j for this i

    # The last entry in dp table indicates whether the whole string can be segmented
    return dp[-1]
#time O(n^2)
#space O(n)
