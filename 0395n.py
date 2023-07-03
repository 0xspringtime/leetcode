#divide and conquer
from collections import Counter

def longestSubstring(s, k):
    # Base case: if string length is less than k, return 0
    if len(s) < k:
        return 0

    # Count the frequency of each character in the string
    counter = Counter(s)

    # Divide the string at characters that appear less than k times
    for char in set(s):
        if counter[char] < k:
            return max(longestSubstring(t, k) for t in s.split(char))

    # If all characters appear at least k times, return the length of the string
    return len(s)
#time O(n^2)
#space O(n)
