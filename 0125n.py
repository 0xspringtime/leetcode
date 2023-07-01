#two pointer
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """

    # Initialize two pointers at the beginning and end of s
    i, j = 0, len(s) - 1

    while i < j:
        # Move the pointers until they point to alphanumeric characters
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1

        # If the characters at the pointers aren't equal (ignoring case), return False
        if s[i].lower() != s[j].lower():
            return False

        # Move the pointers inward
        i, j = i + 1, j - 1

    # If the entire string was traversed without finding unequal characters, return True
    return True
#time O(n)
#space O(1)
