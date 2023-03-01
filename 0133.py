def cloneGraph(self, node: "Node") -> "Node":
    oldToNew = {}

    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]

        copy = Node(node.val)
        oldToNew[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy

    return dfs(node) if node else None

#O(V+E)

adjList = [[2,4],[1,3],[2,4],[1,3]]
print(Solution().cloneGraph(1))
