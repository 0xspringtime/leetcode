#priority queue
import heapq

def lastStoneWeight(stones):
    # Python's heapq library implements a min-heap, so we add a minus sign before every weight to simulate a max-heap.
    stones = [-stone for stone in stones]

    # Heapify our list of stones. It is now a max-heap.
    heapq.heapify(stones)

    # While there is more than one stone left, we must continue smashing.
    while len(stones) > 1:
        # Pop (and negate) the first max weight (smallest number in min-heap)
        stone_weight_1 = -heapq.heappop(stones)

        # Pop (and negate) the second max weight (smallest number in min-heap)
        stone_weight_2 = -heapq.heappop(stones)

        # If the stone weights are not equal, push the remaining weight back into the heap
        if stone_weight_1 != stone_weight_2:
            remaining_weight = stone_weight_1 - stone_weight_2
            heapq.heappush(stones, -remaining_weight)

    # If there are no stones left, return 0. Otherwise, return the remaining stone's weight
    return -stones[0] if stones else 0
#time O(nlogn)
#space O(n)
