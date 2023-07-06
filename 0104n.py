#DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # If the node doesn't exist, return 0
        if root is None:
            return 0

        # Calculate the maximum depth of the left and right subtrees,
        # then return the maximum of these values plus 1
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1
#time O(n)
#space O(h)
