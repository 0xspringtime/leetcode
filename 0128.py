from typing import List
def longestConsecutive(nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0

    for n in nums:
        # check if its the start of a sequence
        if (n - 1) not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest
def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [100,4,200,1,3,2],
            "expected": 4
        },
        {
            "name": "simple case 2",
            "input": [0,3,7,2,5,8,4,6,0,1],
            "expected": 9
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == longestConsecutive(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
