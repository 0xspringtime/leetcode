from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked_list(lst):
    dummy_head = ListNode()
    cur = dummy_head
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy_head.next

def spiralMatrix(m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
    num = m * n
    res = [[-1 for j in range(n)] for i in range(m)]
    x, y = 0, 0
    dx, dy = 1, 0
    while head:
        res[y][x] = head.val
        if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= m or res[y + dy][x + dx] != -1:
            dx, dy = -dy, dx
        x = x + dx
        y = y + dy
        head = head.next
    return res

def test():
    test_cases = [
        {
            "name": "example 1",
            "input": 3,
            "input2": 5,
            "input3": list_to_linked_list([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]),
            "expected": [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
        },
        {
            "name": "example 2",
            "input": 1,
            "input2": 4,
            "input3": list_to_linked_list([0, 1, 2]),
            "expected": [[0,1,2,-1]]
        }
    ]


    for test_case in test_cases:
        assert test_case["expected"] == spiralMatrix(test_case["input"], test_case["input2"], test_case["input3"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
