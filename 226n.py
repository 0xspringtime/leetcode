#tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: TreeNode) -> TreeNode:
    # Base case: if the node is None, simply return it.
    if root is None:
        return None

    # Swap the left and right children of the current node.
    root.left, root.right = root.right, root.left

    # Recursively invert the left and right children.
    invertTree(root.left)
    invertTree(root.right)

    return root
#time O(n)
#spaceO(n)
