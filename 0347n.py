#priority queue
import heapq
from collections import Counter

def topKFrequent(nums, k):
    # Step 1: Count the frequency of each element in the array
    counter = Counter(nums)

    # Step 2: Use a min-heap to keep track of the k most frequent elements
    heap = []
    for num, count in counter.items():
        # Push elements into the heap with their frequency as the key
        heapq.heappush(heap, (count, num))
        # If the heap size exceeds k, remove the element with the smallest frequency
        if len(heap) > k:
            heapq.heappop(heap)

    # Step 3: Build the result list from the heap
    result = []
    while heap:
        result.append(heapq.heappop(heap)[1])  # Add the element to the result list

    # Step 4: Reverse the result list to get the elements in descending order of frequency
    result.reverse()

    return result
#time O(n log k)
#space O(n)
