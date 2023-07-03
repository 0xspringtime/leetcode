import heapq

def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # Create a max heap of the first k elements
    heap = [-num for num in nums[:k]]
    heapq.heapify(heap)

    # For each remaining element, if it is smaller than the heap's root
    # remove the root and add the new element
    for num in nums[k:]:
        if num > -heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, -num)

    # The root of the heap is now the kth largest element
    return -heap[0]
#time O(nlogk)
#space O(k)
