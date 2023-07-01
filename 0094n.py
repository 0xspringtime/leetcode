# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def inorderTraversal(root):
    # Create the result list outside the helper function
    res = []
    
    def helper(root):
        # If the node is not null
        if root:
            # First recur for the left child
            helper(root.left)
            
            # Then append the value of the node
            res.append(root.val)
            
            # Finally recur for the right child
            helper(root.right)
    
    # Call the helper function on the root
    helper(root)
    
    return res
#time O(n)
#space O(n)
