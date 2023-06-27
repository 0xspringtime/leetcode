def insert(intervals, newInterval):
    # Initialize our results list and a pointer i to track our location in intervals.
    result = []
    i = 0

    # Iterate through all intervals that come before newInterval.
    # These intervals will not overlap with newInterval since they end before newInterval starts.
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge all overlapping intervals. As long as intervals[i] overlaps with newInterval, merge them.
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    # Append the merged newInterval.
    result.append(newInterval)

    # Append all remaining intervals that come after newInterval.
    while i < len(intervals):
        result.append(intervals[i])
        i += 1

    return result

#time O(n)
#space O(n)
