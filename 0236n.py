# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if root in (None, p, q): 
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root  # if p and q are respectively in the left and right subtrees of root, then root is their LCA
    else:
        return left if left else right  # either one of p,q is in the subtree of root, or none is. If none is, this will eventually return None
#time O(n)
#space O(n)
