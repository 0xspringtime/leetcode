def list_to_linked_list(lst):
    dummy_head = ListNode()
    cur = dummy_head
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy_head.next
