# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA, pB = headA, headB

        while pA != pB:
            # If pA reached the end of list A, then redirect it to the head of list B.
            pA = pA.next if pA else headB
            
            # If pB reached the end of list B, then redirect it to the head of list A.
            pB = pB.next if pB else headA

        # pA/pB is the intersection node or None.
        return pA
#time O(n)
#space O(1)
