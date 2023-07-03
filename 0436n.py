#binary search
def findRightInterval(intervals):
    # Create a sorted list of tuples, where each tuple is (start time, original index)
    sorted_intervals = sorted((interval[0], i) for i, interval in enumerate(intervals))

    res = []
    for interval in intervals:
        # Find the earliest start time that is greater than or equal to the end time of the current interval
        right_interval = binary_search(sorted_intervals, interval[1])

        # If a right interval is found, append its original index to the result list
        # Otherwise, append -1
        res.append(right_interval[1] if right_interval else -1)

    return res

def binary_search(sorted_intervals, target):
    left, right = 0, len(sorted_intervals) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_intervals[mid][0] < target:
            left = mid + 1
        else:
            right = mid - 1
    return sorted_intervals[left] if left < len(sorted_intervals) else None
#time O(nlogn)
#space O(n)
