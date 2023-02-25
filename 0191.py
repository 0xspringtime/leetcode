def ham(n: int):
    res = 0
    while n:
        n &= n-1
        res +=1
    return res

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": 0o11111111111111111111111111111101,
            "expected": 31 
        },
        {
            "name": "simple case 2",
            "input": 0o00000000000000000000000010000000,
            "expected": 1 
        },
        {
            "name": "case 3",
            "input": 0o00000000000000000000000000001011,
            "expected": 3
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == ham(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
