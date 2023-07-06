#Union Find
class Solution:
    def countComponents(self, n, edges):
        # Initialize the parent array (representing the parent of each node in its set)
        parent = list(range(n))

        # Function to find the set (root/parent) of a node
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression for efficiency
            return parent[x]

        # Function to merge the sets of two nodes
        def union(xy):
            x, y = map(find, xy)
            parent[x] = y  # Merge x's set with y's set

        # Apply union operation for each edge
        for edge in edges:
            union(edge)

        # Count the number of connected components
        return len(set(map(find, parent)))  # find() is called to make sure path compression is done
#time O(n+e)
#space O(n)
