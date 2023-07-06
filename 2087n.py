#dynamic programming
#BFS
import heapq

def minCostToHome(m, n, startPos, homePos, rowCosts, colCosts):
    # Initialize cost matrix with all infinity
    cost = [[float('inf')] * n for _ in range(m)]
    # Set the cost of the starting cell to 0
    cost[startPos[0]][startPos[1]] = 0

    # Directions for movement
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

    # Priority queue for BFS, initialized with the starting cell
    queue = [(0, startPos[0], startPos[1])]

    while queue:
        current_cost, x, y = heapq.heappop(queue)  # Pop the cell with smallest cost

        # If we have reached the home cell, return its cost
        if [x, y]
#time O(mnlog(mn))
#space O(mn)
