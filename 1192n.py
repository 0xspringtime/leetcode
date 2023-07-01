#Tarjan
#Biconnected Component
#DFS
from collections import defaultdict
def criticalConnections(n, connections):
    # Create an adjacency list representation of the graph
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize lists for discovery times and low links
    discovery = [-1] * n
    low = [0] * n

    # List for the critical connections
    out = []

    # DFS function
    def dfs(node, parent, time):
        # Update discovery time and low link value
        discovery[node] = time
        low[node] = time

        # For each neighbor of the current node
        for neighbor in graph[node]:
            # If the neighbor has not been visited
            if discovery[neighbor] == -1:
                # Recurse on the neighbor
                dfs(neighbor, node, time + 1)

                # If the lowest node reachable from the neighbor is only reachable through the current edge
                if low[neighbor] > discovery[node]:
                    out.append([node, neighbor])

            # If the neighbor is not the parent of the current node, update the low link of the current node
            elif neighbor != parent:
                low[node] = min(low[node], discovery[neighbor])

        # Update the low link of the current node based on the neighbors
        low[node] = min([low[node]] + [low[neighbor] for neighbor in graph[node] if neighbor != parent])

    # Start DFS from node 0 (assuming it's connected)
    dfs(0, -1, 0)

    # Return the critical connections
    return out
#time O(V+E)
#space O(V+E)
