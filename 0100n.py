#tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSameTree(p, q):
    # If both trees are null
    if p is None and q is None:
        return True
    # If one of them is null
    if p is None or q is None:
        return False
    # If the values of the nodes are different
    if p.val != q.val:
        return False
    # Check left and right children
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
#time O(n)
#space O(h)
