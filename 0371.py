def getSum(a: int, b: int) -> int:
        def add(a, b):
            if not a or not b:
                return a or b
            return add(a ^ b, (a & b) << 1)

        if a * b < 0:  # assume a < 0, b > 0
            if a > 0:
                return self.getSum(b, a)
            if add(~a, 1) == b:  # -a == b
                return 0
            if add(~a, 1) < b:  # -a < b
                return add(~add(add(~a, 1), add(~b, 1)), 1)  # -add(-a, -b)

        return add(a, b)  # a*b >= 0 or (-a) > b > 0


def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": 1,
            "input1": 2,
            "expected": 3 
        },
        {
            "name": "simple case 2",
            "input": 2,
            "input1": 3,
            "expected": 5 
        } 
   ]

    for test_case in test_cases:
        assert test_case["expected"] == getSum(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
