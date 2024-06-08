class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    # A helper function to build the tree
    def helper(in_left = 0, in_right = len(inorder)):
        nonlocal pre_idx
        # If there is no elements to construct subtrees
        if in_left == in_right:
            return None
            
        # Pick up pre_idx element as a root
        root_val = preorder[pre_idx]
        root = TreeNode(root_val)

        # Root splits inorder list into left and right subtrees
        index = idx_map[root_val]

        # Increment pre_idx
        pre_idx += 1

        # Build left and right subtrees
        # Be careful with the off-by-one to avoid overflows
        root.left = helper(in_left, index)
        root.right = helper(index + 1, in_right)
        return root
        
    # Start from the first preorder element
    pre_idx = 0
    # Build a hashmap to store value -> its index relations
    idx_map = {val:idx for idx, val in enumerate(inorder)} 
    return helper()
#time O(n)
#space O(n)
