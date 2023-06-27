#DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        self.depth(root)
        return self.diameter

    def depth(self, node):
        if node is None:
            return 0
        left = self.depth(node.left)
        right = self.depth(node.right)

        # update the diameter if the path through the root is larger
        self.diameter = max(self.diameter, left + right)

        # the depth of the node is the maximum depth of its children plus 1
        return max(left, right) + 1
#time O(n)
#space O(h)
