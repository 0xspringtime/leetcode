class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    # create a dummy node
    dummy = ListNode(0)
    
    # tail always points to the last node in the merged list
    tail = dummy
    
    while True:
        
        # if either list ends, use the other list
        if l1 is None:
            tail.next = l2
            break
        if l2 is None:
            tail.next = l1
            break
            
        # Compare the data of the lists and whichever is smaller is appended to the tail 
        # and the pointer is moved to the next node of that list
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        
        # advance the tail
        tail = tail.next
        
    # return the merged list
    return dummy.next
#time O(n+m)
#space O(1)
