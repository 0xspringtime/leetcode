class ListNode:
    def __init__(self, x=0, next=None):
        self.x = x
        self.next = None

def list_to_linked_list(lst):
    dummy_head = ListNode()
    cur = dummy_head
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy_head.next

def reverseList(head: ListNode) -> ListNode:
    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

print(reverseList(list_to_linked_list([1,2,3,4,5])))
