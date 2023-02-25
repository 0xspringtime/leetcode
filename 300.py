from typing import List
def lengthOfLIS(nums: List[int]) -> int:
    LIS = [1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
    return max(LIS)
def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input":  [10,9,2,5,3,7,101,18],
            "expected": 4
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == lengthOfLIS(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))