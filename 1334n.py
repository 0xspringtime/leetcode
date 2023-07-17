#floyd
def findTheCity(n, edges, distanceThreshold):
    # Define a large number which represents the infinity in the context of this problem
    INF = 10**6

    # Initialize a distance matrix
    distance = [[INF]*n for _ in range(n)]

    # For each vertex, the distance to itself is 0
    for i in range(n):
        distance[i][i] = 0

    # Update the distance matrix with the given edges
    for u, v, w in edges:
        distance[u][v] = distance[v][u] = w

    # Apply the Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # If the distance from vertex i to vertex j through vertex k is smaller
                # than the current distance from vertex i to vertex j, then update the distance
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    # Find the city that has the smallest number of reachable cities with a distance at most distanceThreshold
    min_reachable = INF
    city = -1
    for i in range(n):
        # Count the number of reachable cities from city i
        count = sum(d <= distanceThreshold for d in distance[i])
        # If the number of reachable cities from city i is smaller than the current minimum
        # or city i is greater than the current city (when there are multiple cities with the same minimum),
        # then update the city and the minimum
        if count <= min_reachable:
            min_reachable = count
            city = i

    # Return the city
    return city
#time O(n^3)
#space O(n^2)
