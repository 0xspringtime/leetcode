#priority queue
import heapq

def kClosest(points, K):
    heap = []
    for (x, y) in points:
        # Push the negative of distance and point itself into the heap
        dist = -(x*x + y*y)
        heapq.heappush(heap, (dist, x, y))
        # If heap size exceeds K, pop out the farthest point
        if len(heap) > K:
            heapq.heappop(heap)

    # The heap now contains K closest points to the origin, return them
    return [(x,y) for (dist,x,y) in heap]
#time O(nlogk)
#space O(k)
