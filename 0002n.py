#linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    # Create a dummy node to serve as the head of the result list
    dummy = ListNode()
    # Create a pointer to keep track of the current node in the result list
    curr = dummy
    # Initialize carry to 0
    carry = 0

    # Iterate through both input lists until they are exhausted
    while l1 or l2:
        # Get the values of the current nodes (if available)
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        # Compute the sum of the current digits along with the carry
        digit_sum = x + y + carry
        # Update the carry for the next iteration
        carry = digit_sum // 10
        # Create a new node with the ones digit of the sum
        curr.next = ListNode(digit_sum % 10)
        # Move the current pointer forward
        curr = curr.next
        # Move the input list pointers forward (if available)
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    # If there is still a carry remaining, add an additional node with the carry
    if carry > 0:
        curr.next = ListNode(carry)

    # Return the head of the result list (excluding the dummy node)
    return dummy.next
#time O(max(m, n))
#space O(max(m, n))

