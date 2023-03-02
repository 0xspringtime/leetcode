def myPow(x: float, n: int) -> float:
    def helper(x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = helper(x * x, n // 2)
        return x * res if n % 2 else res

    res = helper(x, abs(n))
    return res if n >= 0 else 1 / res

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": 2.00000,
            "input1": 10,
            "expected": 1024.00000
        },
        {
            "name": "simple case 2",
            "input": 2.10000,
            "input1": 3,
            "expected": 9.261000000000001
        },
        {
            "name": "list with one item",
            "input": 2.00000,
            "input1": -2,
            "expected": 0.25
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == myPow(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    print(myPow(2.10000, 3))
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
