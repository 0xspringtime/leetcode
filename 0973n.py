import heapq

def kClosest(points, k):
    # Function to calculate squared Euclidean distance
    def squared_distance(point):
        return point[0] ** 2 + point[1] ** 2
    
    # Initialize a max-heap
    max_heap = []
    
    for point in points:
        dist = squared_distance(point)
        # Use negative distance to simulate a max-heap using heapq (which is a min-heap)
        heapq.heappush(max_heap, (-dist, point))
        
        # If heap size exceeds k, remove the farthest point
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    
    # Extract points from the heap
    return [point for (_, point) in max_heap]

# Example usage:
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
print(kClosest(points, k))  # Output: [[-2, 2], [0, 1]]

points = [[3, 3], [5, -1], [-2, 4]]
k = 2
print(kClosest(points, k))  # Output: [[3, 3], [-2, 4]]
#time O(nlogk)
#space O(k)
