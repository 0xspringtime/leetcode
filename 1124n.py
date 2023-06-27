#prefix sums
def longestWPI(hours):
    """
    :type hours: List[int]
    :rtype: int
    """
    # initialize prefix sum array
    sums = [0]*(len(hours)+1)

    # initialize table to store first occurrence of each sum
    first_occurrence = {}

    # initialize answer
    ans = 0

    # calculate prefix sum array and maintain first_occurrence table
    for i in range(len(hours)):
        # modify hours to be 1 for tiring day, -1 otherwise
        sums[i+1] = sums[i] + (1 if hours[i] > 8 else -1)

        # if current prefix sum is positive, we have a well-performing interval
        if sums[i+1] > 0:
            ans = i + 1

        # if current prefix sum is not positive, and we have seen this sum before
        elif sums[i+1] not in first_occurrence:
            first_occurrence[sums[i+1]] = i+1

        # if we have seen sum - 1 before, we have a well-performing interval
        if sums[i+1]-1 in first_occurrence:
            ans = max(ans, i+1-first_occurrence[sums[i+1]-1])

    return ans
#time O(n)
#space O(n)
