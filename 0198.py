from typing import List
def rob(nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [1,2,3,1],
            "expected": 4 
        },
        {
            "name": "simple case 2",
            "input": [2,7,9,3,1],
            "expected": 12
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == rob(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
