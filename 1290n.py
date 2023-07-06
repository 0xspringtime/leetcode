# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head):
        # Initialize the decimal value to 0
        decimal_value = 0

        # Traverse the linked list
        node = head
        while node is not None:
            # Multiply the current decimal value by 2 (as we're going to the next bit)
            decimal_value *= 2

            # Add the current node's value to the decimal value
            decimal_value += node.val

            # Go to the next node
            node = node.next

        # Return the decimal value
        return decimal_value
#time O(n)
#space O(1)
