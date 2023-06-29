#sorting
def merge(intervals):
    # First, sort the intervals based on their start time
    intervals.sort(key=lambda x: x[0])

    # Initialize the result array with the first interval
    merged = [intervals[0]]

    # Iterate through the remaining intervals
    for current_interval in intervals[1:]:
        # Get the last interval in the merged array
        last_interval = merged[-1]

        # If the current interval overlaps with the last interval in the merged array,
        # then we merge them by updating the end time of the last interval
        if current_interval[0] <= last_interval[1]:
            last_interval[1] = max(last_interval[1], current_interval[1])
        else:
            # If the current interval does not overlap with the last interval,
            # then we add it to the merged array
            merged.append(current_interval)

    return merged
#time O(nlogn)
#sapce O(n)
