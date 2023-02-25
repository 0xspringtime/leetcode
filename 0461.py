def hamming(x,y):
    return bin(x ^ y).count('1')

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": 1,
            "input1": 4,
            "expected": 2
        },
        {
            "name": "simple case 2",
            "input": 3,
            "input1": 1,
            "expected": 1 
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == hamming(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
