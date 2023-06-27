#greedy
#hash
def partitionLabels(s):
    # A hash table to store the last occurrence of each character
    last = {char: i for i, char in enumerate(s)}

    # Initialize j and anchor to 0
    j = anchor = 0
    ans = []

    # Iterate the string
    for i, char in enumerate(s):
        # Update j to the maximum of j and the last occurrence of current character
        j = max(j, last[char])

        # If we reached the end of a partition
        if i == j:
            # Append the partition size to ans
            ans.append(i - anchor + 1)

            # Start a new partition
            anchor = i + 1

    return ans
#time O(n)
#space O(1)
