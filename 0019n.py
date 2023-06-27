#two pointer
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head

    first = second = dummy

    # Move the first pointer n steps ahead
    for _ in range(n+1):
        first = first.next

    # Move both pointers one step at a time until the first pointer reaches the end
    while first is not None:
        first = first.next
        second = second.next

    # At this point, the second pointer will be pointing at the node before the node we want to delete
    second.next = second.next.next

    return dummy.next
#time O(L)
#space O(1)
