"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        # Start with the root node. There are no next nodes at the root level.
        node = root

        # Traverse level by level
        while node.left:
            # For each node of this level, point to the next node
            cur = node
            while cur:
                # Connect left child to right child
                cur.left.next = cur.right

                # Connect right child to next node's left child, if it exists
                if cur.next:
                    cur.right.next = cur.next.left
                
                # Move to next node
                cur = cur.next
            
            # Move to next level
            node = node.left
        
        return root
#time O(n)
#space O(1)
