#priority queue
# First we need to define the ListNode class, which will be used for the linked list nodes.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq

def mergeKLists(lists):
    """
    Merges k sorted linked lists into one sorted linked list.
    """
    # Create a dummy node, which will be the head of the merged linked list.
    dummy = ListNode(0)
    current = dummy

    # Initialize a heap. In Python, heapq is a min-heap by default.
    heap = []

    # For each list, if it is not empty, append the head node's value and the head node itself to the heap.
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i))
            # Move the head of this list to the next node.
            lists[i] = lists[i].next

    # While the heap is not empty.
    while heap:
        # Pop the node with the smallest value out of the heap.
        val, idx = heapq.heappop(heap)
        # Append this node to the merged linked list.
        current.next = ListNode(val)
        current = current.next

        # If the list from which this node was popped is not empty, append the new head node's value and the head node itself to the heap.
        if lists[idx]:
            heapq.heappush(heap, (lists[idx].val, idx))
            # Move the head of this list to the next node.
            lists[idx] = lists[idx].next

    return dummy.next
#time O(nlogk)
#space O(k)
