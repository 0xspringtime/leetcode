#DFS
#topological sort
def findOrder(numCourses, prerequisites):
    # Define a variable to store the result.
    result = []

    # Initialize the graph.
    graph = [[] for _ in range(numCourses)]
    visit = [0 for _ in range(numCourses)]

    # Create the adjacency list.
    for x, y in prerequisites:
        graph[x].append(y)

    # Define a DFS function.
    def dfs(i):
        # If we encounter a node already being visited, then there is a cycle.
        if visit[i] == -1:
            return False
        # If it is done visited, then do not visit again.
        if visit[i] == 1:
            return True
        # Mark as being visited.
        visit[i] = -1
        # Visit all the neighbours.
        for j in graph[i]:
            if not dfs(j):
                return False
        # After visit all the neighbours mark it as done visited.
        visit[i] = 1
        result.append(i)
        return True

    # Visit all the nodes.
    for i in range(numCourses):
        if not dfs(i):
            return []
    return result
#time O(n+m)
#space O(n+m)
