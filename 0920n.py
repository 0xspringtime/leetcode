def canAttendMeetings(intervals):
    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Iterate over the intervals starting from the second one
    for i in range(1, len(intervals)):
        # If the start time of the current meeting is less than the end time of the previous meeting,
        # it means the person cannot attend all meetings, so return False
        if intervals[i][0] < intervals[i-1][1]:
            return False
    # If no conflict occurs, return True
    return True
#time O(n log n)
#space O(1)
