import heapq

# 1. Initialize the priority queue (in Python, this is usually a list).
priority_queue = []

# 2. Add elements to the queue. 
# Each element is a tuple where the first element is the priority.
heapq.heappush(priority_queue, (priority1, item1))
heapq.heappush(priority_queue, (priority2, item2))

# 3. Remove and return the lowest priority item.
lowest_priority_item = heapq.heappop(priority_queue)

# 4. Check if the queue is empty.
if not priority_queue:
    print("The priority queue is empty.")

# 5. Remove and return the lowest priority item, or return a default value if the queue is empty.
lowest_priority_item = heapq.heappop(priority_queue) if priority_queue else default_item

#main advantage of priority queues is that they allow efficient access (and removal) of the element with the highest (or lowest) priority, rather than accessing the element in the order they were inserted
