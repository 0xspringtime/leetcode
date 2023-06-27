#tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSubtree(root, subRoot):
    # If the root tree is null, then there can't be a subtree
    if root is None:
        return False

    # Return True if the subtree matches the tree,
    # or if the subtree matches any of the subtrees of the tree
    return isSame(root, subRoot) or isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

def isSame(t1, t2):
    # If both trees are null, they are the same
    if t1 is None and t2 is None:
        return True
    # If one of the trees is null and the other is not, they are not the same
    if t1 is None or t2 is None:
        return False
    # If the values of the roots of both trees are the same, and their left and right children are the same,
    # then the trees are the same
    return t1.val == t2.val and isSame(t1.left, t2.left) and isSame(t1.right, t2.right)
#time O(m*n)
#space O(n)
