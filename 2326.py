def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
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
        assert test_case["expected"] == average(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))