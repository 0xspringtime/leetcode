from typing import List
def add(num: List[int], k: int):
	return [int(i) for i in str(int(''.join([str(i) for i in num]))+k)]

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [1,2,0,0],
            "input1": 34,
            "expected": [1,2,3,4]
        },
        {
            "name": "simple case 2",
            "input": [2, 7, 4],
            "input1": 181,
            "expected": [4,5,5] 
        },
        {
            "name": "simple case 3",
            "input": [2,1,5],
            "input1": 806,
            "expected": [1,0,2,1] 
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == add(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
