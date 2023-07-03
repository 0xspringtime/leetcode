#DFS
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: 'Node') -> 'Node':
    # Handle the case when the input node is None
    if node is None:
        return None

    # Initialize a dictionary to store the mapping from original nodes to their clones
    node_dict = {}

    # Define the DFS function
    def dfs(node):
        # If the node is already cloned, return the cloned node
        if node in node_dict:
            return node_dict[node]

        # Clone the node and store it in the dictionary
        clone = Node(node.val, [])
        node_dict[node] = clone

        # Visit all the neighbors
        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    # Call the DFS function on the input node
    return dfs(node)
#time O(n+m)
#space O(n+m)
