#deque
#sliding window
from collections import deque

def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    deq = deque()
    res = []

    for i, n in enumerate(nums):
        # remove indices that are out of bound
        while deq and deq[0] < i - k + 1:
            deq.popleft()
        # remove from deq indices of all elements
        # which are smaller than current element nums[i]
        while deq and nums[deq[-1]] < n:
            deq.pop()
        deq.append(i)
        # deq[0] is the index of the maximum element of previous window
        # append that maximum element to the result
        if i >= k - 1:
            res.append(nums[deq[0]])
    return res
#time O(n)
#space O(k)
