#linked list
#floyd
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reorderList(head):
    if not head:
        return

    # find the middle of linked list
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the second half
    prev, curr = None, slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # merge two sorted linked lists
    first, second = head, prev
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next

    return head
#time O(n)
#space O(1)
