#Floyd
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def hasCycle(head):
    # Initialize two pointers at the head of the list
    tortoise = hare = head

    while hare and hare.next:  # Continue until we reach the end of the list
        tortoise = tortoise.next  # Tortoise moves one step
        hare = hare.next.next  # Hare moves two steps

        if tortoise == hare:  # If the two pointers meet, there is a cycle
            return True

    # If we reach here, hare has reached the end of the list, so there is no cycle
    return False

