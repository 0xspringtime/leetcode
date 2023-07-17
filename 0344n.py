#two pointer
def reverseString(s):
    # Initialize the two pointers
    left = 0
    right = len(s) - 1

    # Loop until the two pointers meet
    while left < right:
        # Swap the characters at the positions of the two pointers
        s[left], s[right] = s[right], s[left]

        # Move the pointers towards the center
        left += 1
        right -= 1
#time O(n)
#space O(1)
