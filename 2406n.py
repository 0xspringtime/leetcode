#priority queue
import heapq

def minGroupNumber(intervals):
    # First, we sort the intervals by their start times
    intervals.sort()
    # We use a priority queue to keep track of the end time of each group
    heap = []
    for interval in intervals:
        if heap and interval[0] > heap[0]:
            # The current interval does not overlap with the latest interval in the current group
            # So we can replace the end time of the current group with the end time of the current interval
            heapq.heapreplace(heap, interval[1])
        else:
            # The current interval overlaps with the latest interval in the current group
            # So we create a new group for the current interval
            heapq.heappush(heap, interval[1])
    # The number of groups is the size of the heap
    return len(heap)
#time O(nlogn)
#space O(n)
