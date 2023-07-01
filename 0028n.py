#sliding window
def strStr(haystack, needle):
    # If the needle is an empty string, return 0 according to the problem statement
    if not needle:
        return 0

    # Get the lengths of both strings
    len_haystack, len_needle = len(haystack), len(needle)

    # Iterate over the haystack string
    for i in range(len_haystack - len_needle + 1):
        # If the substring from the current position with the length of the needle string
        # is equal to the needle string, then we have found the first occurrence
        if haystack[i:i+len_needle] == needle:
            return i

    # If we have not returned from the function yet, then the needle string is not in the haystack string
    return -1
#time O(n)
#space O(1)
