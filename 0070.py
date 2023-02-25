def climbStairs(n: int) -> int:
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": 2,
            "expected": 2
        },
        {
            "name": "simple case 2",
            "input": 3,
            "expected": 3
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == climbStairs(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
