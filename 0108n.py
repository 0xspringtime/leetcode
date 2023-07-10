# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # If the list is empty, return None
        if not nums:
            return None

        # Find the middle point
        mid = len(nums) // 2

        # Create a root node
        node = TreeNode(nums[mid])

        # Recursively build the left and right subtrees
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])

        return node
#time O(n)
#space O(logn)
