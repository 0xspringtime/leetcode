#two pointer
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head):
    prev_node = None
    current_node = head

    while current_node is not None:
        # Store the next node
        next_node = current_node.next

        # Change direction of the current node
        current_node.next = prev_node

        # Move prev_node and current_node one step forward
        prev_node = current_node
        current_node = next_node

    return prev_node
#time O(n)
#space O(1)
