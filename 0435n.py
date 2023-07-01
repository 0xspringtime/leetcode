#greedy
def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])  # Sort intervals based on end time
    count = 0
    end = intervals[0][1]  # Initialize the current end time

    for i in range(1, len(intervals)):
        if intervals[i][0] < end:  # Overlap detected
            count += 1
        else:
            end = intervals[i][1]  # Update the current end time

    return count
#time O(nlog(n))
#space O(1)
