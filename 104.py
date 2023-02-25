#recursive DFS
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
root = TreeNode([3,9,20])
root.left=TreeNode([9, None, None])
root.right=TreeNode([20,15,7])
root.left.right=TreeNode([15, None, None])
root.right.right=TreeNode([7, None, None])
print(Solution().maxDepth(root))
