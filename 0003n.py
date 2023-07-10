#sliding window
def lengthOfLongestSubstring(s):
    # Dictionary to store the last seen position of each character.
    seen = {}
    # Initialize the pointers and max_length
    left = max_length = 0

    for right in range(len(s)):
        # If the character is already in the dictionary (seen),
        # update the left pointer to the right of the last seen duplicate.
        if s[right] in seen:
            left = max(left, seen[s[right]] + 1)
        # Store/Update the index of current character.
        seen[s[right]] = right
        # Calculate the maximum length
        max_length = max(max_length, right - left + 1)

    return max_length
#time O(n)
#space O(min(m))
