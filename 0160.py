from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    l1, l2 = headA, headB
    while l1 != l2:
        l1 = l1.next if l1 else headB
        l2 = l2.next if l2 else headA
    return l1

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [1, 2, 3],
            "expected": 2.0
        },
        {
            "name": "simple case 2",
            "input": [1, 2, 3, 4],
            "expected": 2.5
        },
        {
            "name": "list with one item",
            "input": [100],
            "expected": 100.0
        },
        {
            "name": "empty list",
            "input": [],
            "expected": None
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == getIntersectionNode(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
