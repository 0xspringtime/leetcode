#two pointer
def isSubsequence(s, t):
    # Initialize pointers for both strings
    i, j = 0, 0

    # While there are characters left in both strings
    while i < len(s) and j < len(t):
        # If the characters match, move both pointers forward
        if s[i] == t[j]:
            i += 1
        # If they don't match, only move the pointer of t forward
        j += 1

    # If we have traversed the entire length of s, s is a subsequence of t
    return i == len(s)
#time O(n)
#space O(1)
