#union find
def findRedundantConnection(edges):
    parent = list(range(len(edges) + 1))

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX == rootY:
            return False
        parent[rootX] = rootY
        return True

    for x, y in edges:
        if not union(x, y):
            return [x, y]
#time O(n)
#space O(n)
