#priority queue
import heapq

class KthLargest:
    def __init__(self, k, nums):
        # initialize k and heap
        self.k = k
        self.heap = nums
        # turn nums into a min heap
        heapq.heapify(self.heap)
        # keep the heap size k, by popping out the smallest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        # add new value to the heap
        heapq.heappush(self.heap, val)
        # if size of heap is larger than k, pop out the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # return the smallest (root) of the heap
        return self.heap[0]
#time O(nlogn)
#space O(k)
