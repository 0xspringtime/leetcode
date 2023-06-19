# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set()  # Set to keep track of visited nodes

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")  # Display the node
        visited.add(node)  # Mark node as visited
        for neighbour in graph[node]:  # Visit all its neighbours
            dfs(visited, graph, neighbour)

# Driver code
dfs(visited, graph, 'A')

"""
In this script, dfs is a function that implements the depth-first search. It takes a set visited to keep track of visited nodes, a graph represented as an adjacency list, and a node where the search starts.

In the function, if node is not in visited, it will print node, add node to visited, and call itself recursively on all neighbors of node. This will explore the graph as deep as possible along each branch before backtracking.

This approach can be adapted to solve various problems, such as finding a path between two nodes, checking if a graph is connected, or finding a cycle in a graph.
"""
