#dynamic programming
def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    # Initialize result array with 0's of length n + 1
    res = [0] * (n + 1)

    # Compute number of 1's for every number i from 1 to n
    for i in range(1, n + 1):
        # If i is even, then it has same number of 1's as i / 2.
        # If i is odd, then it has one more 1 than i - 1.
        res[i] = res[i >> 1] + (i & 1)

    return res
#time O(n)
#space O(n)
