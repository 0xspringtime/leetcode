#BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def levelOrder(root):
    # check if root is None
    if not root:
        return []

    # Create a queue to hold nodes at each level
    queue = [root]
    result = []

    while queue:
        level = []
        for i in range(len(queue)):
            # remove the first node from the queue
            node = queue.pop(0)

            # add the node's value to the current level's list
            level.append(node.val)

            # add the node's children to the queue, if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # add the current level's list to the final result
        result.append(level)

    return result
#time O(n)
#space O(n)
