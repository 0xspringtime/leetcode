#DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        # Recursive helper function to get the height of a node
        def height(node):
            if not node:
                return 0

            left_height, right_height = height(node.left), height(node.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            else:
                return max(left_height, right_height) + 1

        # Use the helper function to get the height of the root
        return height(root) != -1
#time O(n)
#space O(h)
