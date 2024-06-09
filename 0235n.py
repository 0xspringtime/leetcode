#BST
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    while root:
        # If both p and q are greater than parent
        if root.val < p.val and root.val < q.val:
            root = root.right
        # If both p and q are lesser than parent
        elif root.val > p.val and root.val > q.val:
            root = root.left
        else:
            return root.val
    return None
#time O(h)
#space O(1)
