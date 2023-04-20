def average(L):
    if not L:
        return None
    return sum(L)/len(L)

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": ["A","A","A","B","B","B"],
            "input2": 2;
            "expected": 8 
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == average(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
