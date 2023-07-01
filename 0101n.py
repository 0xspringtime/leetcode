# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def isSymmetric(root):
    def isMirror(left, right):
        # if both are None, return True
        if left is None and right is None:
            return True
        
        # if only one of them is None, return False
        if left is None or right is None:
            return False
        
        # They are mirrors if:
        # 1. their values are the same,
        # 2. left's left subtree is a mirror of right's right subtree,
        # 3. and left's right subtree is a mirror of right's left subtree
        return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)
    
    # Call the helper function with root and root
    return isMirror(root, root)
#time O(n)
#space O(n)
