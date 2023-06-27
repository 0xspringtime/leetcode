#sorting
def isCovered(ranges, left, right):
    # Sort the ranges
    ranges.sort()

    # Initialize coverage with `left`
    coverage = left

    # Check each range
    for start, end in ranges:
        # If the start of the range can extend the coverage
        if start <= coverage + 1:
            # Update the coverage
            coverage = max(coverage, end)
        # If the coverage is greater than `right`
        if coverage >= right:
            # Return True since we have covered the entire required range
            return True

    # If we have not returned True by now, not all integers are covered
    return False

#time O(nlogn)
#space O(1)
