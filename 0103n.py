#BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def zigzagLevelOrder(root):
    if not root: return []  # return empty list if the tree is empty

    res = []
    queue = [root]
    is_left_to_right = True  # Flag variable to control direction of traversal

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)  # Dequeue a node
            if is_left_to_right:
                level.append(node.val)
            else:
                level.insert(0, node.val)  # prepend if right-to-left

            if node.left:  # enqueue left child
                queue.append(node.left)
            if node.right:  # enqueue right child
                queue.append(node.right)

        res.append(level)
        is_left_to_right = not is_left_to_right  # flip direction for next level

    return res
#time O(n)
#space O(n)
