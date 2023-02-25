from typing import List
def maxSubArray(nums: List[int]) -> int:
        res = nums[0]

        total = 0
        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res


def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [-2,1,-3,4,-1,2,1,-5,4],
            "expected": 6 
        },
        {
            "name": "simple case 2",
            "input": [1],
            "expected": 1 
        },
        {
            "name": "case 3",
            "input": [5,4,-1,7,8],
            "expected": 23
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == maxSubArray(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
