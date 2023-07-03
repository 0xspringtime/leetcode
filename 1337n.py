#priority queue
import heapq

def kWeakestRows(mat, k):
    # Initialize a heap
    heap = []

    # Iterate over the matrix
    for i in range(len(mat)):
        # Count the number of soldiers in the current row
        soldiers = sum(mat[i])

        # Add the row to the heap
        # The heap keeps track of the k weakest rows
        # We use -soldiers to turn the min heap into a max heap
        # And we use -i to break ties by row index
        heapq.heappush(heap, (-soldiers, -i))

        # If the size of the heap exceeds k, remove the strongest row
        if len(heap) > k:
            heapq.heappop(heap)

    # Return the indices of the k weakest rows
    return [-index for soldiers, index in sorted(heap)]
#time O(m * n + m * log k)
#space O(k)
