#merge sort
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case for recursive calls
        if not head or not head.next:
            return head

        # Use two pointer technique to find the middle node
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Divide the list into two halves from middle
        start = slow.next
        slow.next = None

        # Sort the two halves individually
        left, right = self.sortList(head), self.sortList(start)

        # Merge the two sorted halves
        return self.merge(left, right)

    def merge(self, l1, l2):
        # Create a dummy node and a current node
        dummy = cur = ListNode(0)

        # Merge nodes of first and second lists to dummy list
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        # Append remaining nodes of l1 or l2
        cur.next = l1 or l2

        return dummy.next
#time O(nlogn)
#space O(logn)
