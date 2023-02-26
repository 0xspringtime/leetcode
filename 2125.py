def numberOfBeams(bank) -> int:
    ans = prev = 0
    for s in bank:
        c = s.count('1')
        if c:
            ans += prev * c
            prev = c
    return ans

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": ["011001","000000","010100","001000"],
            "expected": 8
        },
        {
            "name": "simple case 2",
            "input": ["000","111","000"],
            "expected": 0
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == numberOfBeams(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
