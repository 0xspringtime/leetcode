def minUnfairness(cookies, k):
    def canDistribute(maxTotal):
        # Start with no child having any cookies
        childCount, childTotal = 0, 0
        # Iterate over the bags of cookies in descending order
        for cookie in reversed(cookies):
            # If adding this bag to the current child would exceed maxTotal
            if childTotal + cookie > maxTotal:
                # Start a new child and increment the child count
                childCount += 1
                childTotal = 0
            # Add the bag of cookies to the current child
            childTotal += cookie
        # One more child for the remaining cookies
        childCount += 1
        # Return whether we can distribute to at most k children
        return childCount <= k

    # Sort the bags of cookies
    cookies.sort()
    # Calculate the sum of cookies in all bags
    total = sum(cookies)
    # Binary search for the minimum total that allows distribution to k children
    left, right = total // k, total
    while left < right:
        mid = (left + right) // 2
        if canDistribute(mid):
            right = mid
        else:
            left = mid + 1

    return left
#time O(nlogn)
#space O(n)
