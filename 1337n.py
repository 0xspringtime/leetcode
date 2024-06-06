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

def kWeakestRows(mat, k):
    # Step 1: Count the number of soldiers in each row
    soldier_counts = [(sum(row), idx) for idx, row in enumerate(mat)]

    # Step 2: Sort the rows based on the number of soldiers and row index
    soldier_counts.sort(key=lambda x: (x[0], x[1]))

    # Step 3: Extract the indices of the first k rows
    weakest_rows = [idx for _, idx in soldier_counts[:k]]

    return weakest_rows
