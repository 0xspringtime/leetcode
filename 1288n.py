def removeCoveredIntervals(intervals):
    # Sort intervals based on end element in descending order and start element in ascending order.
    intervals.sort(key=lambda x: (x[1], -x[0]), reverse=True)

    # Initialize count to 0 and prev to the first interval.
    count = 0
    prev = []

    # Iterate over the intervals
    for interval in intervals:
        # If prev is empty or the start of the current interval is less than the start of the prev interval
        if not prev or interval[0] < prev[0]:
            # Increment count
            count += 1
            # Set prev to the current interval
            prev = interval

    # Return the count
    return count
#time O(nlogn)
#space O(1)
