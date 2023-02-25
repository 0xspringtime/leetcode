from typing import List

def singleNumber(nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res

def test():
    test_cases = [
        {
            "name": "example 1",
            "input": [2, 2, 1],
            "expected": 1
        },
        {
            "name": "example 2",
            "input": [4, 1, 2, 1, 2],
            "expected": 4
        },
        {
            "name": "example 3",
            "input": [1],
            "expected": 1
        }
    ]


    for test_case in test_cases:
        assert test_case["expected"] == singleNumber(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
