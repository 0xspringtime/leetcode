#BST
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def kthSmallest(root: TreeNode, k: int) -> int:
    # Initialize a counter for the number of visited nodes and a stack for the in-order traversal
    counter = 0
    stack = []

    # Start the in-order traversal
    while True:
        while root:
            # Push the current node into the stack and move to the left child
            stack.append(root)
            root = root.left

        # Pop the top node from the stack and visit it
        root = stack.pop()
        counter += 1

        # If this is the kth visited node, return its value
        if counter == k:
            return root.val

        # Move to the right child
        root = root.right
#time O(h+k)
#space O(h)
