#priority queue
import heapq

def kthSmallest(matrix, k):
    n = len(matrix)

    # Initialize a min-heap with the smallest element from each row
    heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
    heapq.heapify(heap)

    # Pop the smallest element from the min-heap and push the next element from the same row into the min-heap
    # Repeat this process k times
    while k:
        val, row, col = heapq.heappop(heap)
        if col < n - 1:
            heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
        k -= 1

    return val
#time O(klogn)
#space O(n)
