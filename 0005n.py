#dynamic programming
def longest_palindrome(s):
    # Initialize a dp list
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    
    # Initialize the start and end indices of longest palindrome substring
    start = end = 0
    
    # Loop over the string from end to start
    for i in range(n-1, -1, -1):
        # For each character, loop from this character to the end of the string
        for j in range(i, n):
            # Check if the substring between these two indices is a palindrome
            if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                dp[i][j] = True
                
                # If this palindrome is longer than the previous longest, update the start and end indices
                if end - start < j - i:
                    start, end = i, j
                    
    # Return the longest palindrome substring
    return s[start:end+1]
#time O(n^2)
#space O(n^2)
