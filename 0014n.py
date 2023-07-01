#horizontal scanning
def longestCommonPrefix(strs):
    # If the list of strings is empty, return an empty string
    if not strs:
        return ""

    # Start from the first string in the list
    prefix = strs[0]

    # Compare this string with every other string in the list
    for i in range(1, len(strs)):
        # While the current string does not start with the current prefix
        while not strs[i].startswith(prefix):
            # Trim the last character off the prefix
            prefix = prefix[:-1]

            # If the prefix becomes empty, return an empty string
            if not prefix:
                return ""

    # Return the longest common prefix
    return prefix
#time O(S)
#space O(1)
